from multiprocessing.dummy import active_children
import sys,os
sys.path.append(os.path.abspath('../..'))
print(sys.path)
#import gamey.engine.play as pl
import gamey.engine.play as pl

import random

import gamey.engine.utility as ut
import gamey.engine.actor as at

################## Viewer #############################################
viewer = pl.make_frame_viewer(1280, 720)

viewer.insert_action(pl.make_terminate_action())
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [viewer]

################## Environment(s) #############################################

###
### Objects
###
hanger_color = (255, 30, 30)


#Generate random starting position 
random_start_x = random.randint(0, 1200)
random_start_y = random.randint(0, 600)

test_bound = (random_start_x,random_start_y,150,100)
test = at.make_rectangle(test_bound, hanger_color)
test.name= "testing"

test.insert_action(at.make_draw_rectangle_action())
game_content.append(test)


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

# Move alarm into the loop
update_timer_action.children.append(alarm_action)

# Alarm triggered, move the mole and reset timer
alarm_action.children.append(start_timer_action)


game_content.append(timer)

################## Looper #############################################

game_looper = pl.make_game_looper( game_content )
game_looper.loop()