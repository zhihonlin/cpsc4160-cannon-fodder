from multiprocessing.dummy import active_children
import sys,os
sys.path.append(os.path.abspath('../..'))
print(sys.path)
#import gamey.engine.play as pl
import gamey.engine.play as pl

import random

import gamey.engine.ui as ui
import gamey.engine.utility as ut
import gamey.engine.sound as sd

# Whackabox Specific Action
class Move: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "move_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        return True 
 
    def act(self, event): 
        if self.condition_to_act(event):
            # Generate random x,y coordinates for button position
            random_x = random.randint(0, 1200)
            random_y = random.randint(0, 600)

            # Generate random rgb value for button color
            random_r = random.randint(0, 255)
            random_g = random.randint(0, 255)
            random_b = random.randint(0, 255)

            self.entity_state.bounds = (random_x,random_y,150,100)
            self.entity_state.color = (random_r,random_g,random_b)
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " is moving")
        return

class GenerateMessage: 
    def __init__(self, total_counter, success_counter): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "generate_message_action" 
        self.children = [] 
        self.verbose = False
        self.total_counter = total_counter
        self.success_counter = success_counter 
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        return True 
 
    def act(self, event): 
        if self.condition_to_act(event):
            self.entity_state.total_message = "Total: " + str(self.total_counter.count)
            self.entity_state.success_message = "Success: " + str(self.success_counter.count)
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " is generating message")
        return


################## Viewer #############################################
viewer = pl.make_frame_viewer(1280, 720)

viewer.insert_action(pl.make_terminate_action())
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [viewer]

################## Environment(s) #############################################

###
### Moles
###
hanger_color = (255, 30, 30)


#Generate random starting position 
random_start_x = random.randint(0, 1200)
random_start_y = random.randint(0, 600)

test_bound = (random_start_x,random_start_y,150,100)
test = ui.make_basic_button(test_bound, hanger_color)
test.name= "testing"

test.insert_action(ui.make_draw_button_action())

key_press_action = ui.make_button_pressed_action()
test.insert_action(key_press_action)

## Mole Moving
move_action = Move()
test.insert_action(move_action)

key_press_action.children.append(move_action)

###
### Create counters
###
total_count = ut.make_total_counter()
success_count = ut.make_success_counter()

total_increment = ut.make_increment_action()
success_increment = ut.make_increment_action()

key_press_action.children.append(success_increment)


total_count.insert_action(total_increment)
success_count.insert_action(success_increment)


###
### Create timer
###
timer = ut.make_timer()
start_timer_action = ut.make_start_timer_action()
update_timer_action = ut.make_update_timer_action()
alarm_action = ut.make_alarm_action()

timer.insert_action(start_timer_action)
timer.insert_action(update_timer_action)
timer.insert_action(alarm_action)

# Activate/Deactivate the button depending on mouse click and alarm
activate_action = ut.make_activate_action()
deactivate_action = ut.make_deactivate_action()

test.insert_action(activate_action)
test.insert_action(deactivate_action)

key_press_action.children.append(deactivate_action)

alarm_action.children.append(activate_action)

# Everytime user presses mouse, resets timer
key_press_action.children.append(start_timer_action)

# Move alarm into the loop
update_timer_action.children.append(alarm_action)

# Alarm triggered, move the mole and reset timer
alarm_action.children.append(move_action)
alarm_action.children.append(start_timer_action)
alarm_action.children.append(total_increment)


game_content.append(timer)

###
### Create sound
###
success_sound = sd.make_emit_sound_action("../assets/sounds/boom.wav")
failed_sound = sd.make_emit_sound_action("../assets/sounds/hello.wav")

test.insert_action(success_sound)
timer.insert_action(failed_sound)


success_increment.children.append(success_sound)
alarm_action.children.append(failed_sound)

###
### Create HUD
###
hud_font =  'Arial'
hud_size = 30
hud_color = (255, 255,255)
hud = ui.make_hud(hud_font, hud_size, hud_color)
hud.insert_action(ui.make_draw_hud_action())

generate_message_action = GenerateMessage(total_count, success_count)
hud.insert_action(generate_message_action)

key_press_action.children.append(generate_message_action)
alarm_action.children.append(generate_message_action)

game_content.append(hud)

game_content.append(test)

################## Looper #############################################

game_looper = pl.make_game_looper( game_content )
game_looper.loop()