import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath('../..'))
import gamey.engine.play as pl
import random
import gamey.engine.utility as ut
import gamey.engine.actor as at

print(sys.path)
#import gamey.engine.play as pl


################## Generate Circles #############################################
def get_circles(nx, ny, nb):
    circles = []
    radius = 10
    for i in range(0, nb):
        random_x = random.randint(0, nx)
        random_y = random.randint(0, ny)
        random_r = random.randint(0, 255)
        random_g = random.randint(0, 255)
        random_b = random.randint(0, 255)
        circle_bounds = (random_x, random_y)
        circle_color = (random_r, random_g, random_b)
        circle = at.make_round(circle_color, circle_bounds, radius)
        circle.name = "circle" + str(i)
        circle.insert_action(at.make_draw_circle_action())
        circles.append(circle)
    return circles

################## Physics helper #############################################
def get_particles(init_data):
    import gamey.engine.physics as ps
    particles = []

    parts = ps.make_particles()
    particles.append(parts)

    for d in init_data:
      position = list(d.center)
      velocity = [ (2.0*random.random() - 1.0), (2.0*random.random() - 1.0)]
      mass = 1.0
      parts.add_particle(position,velocity,mass)
    
    # Simple gravity force
    gravity = ps.make_gravity_force()
    gravity.gravity = [0.0,0.5]
    grav_action = ps.make_gravity_action()
    gravity.insert_action(grav_action)

    # Position Solve
    psolve = ps.make_position_solve()
    parts.insert_action(psolve)

    # Velocity Solve
    vsolve = ps.make_velocity_solve()
    parts.insert_action(vsolve)
    vsolve.children.append(grav_action)

    # Euler Solve
    esolve = ps.make_euler_solve()
    esolve.dt = 0.1
    parts.insert_action(esolve)
    esolve.children.append(psolve)
    esolve.children.append(vsolve)
    esolve.types.append("loop")

    # Connect particles positions to circle positions
    for i in range(0,len(init_data)):
      pick = ps.make_pick_position(i)
      put = at.make_put_position_action()

      parts.insert_action(pick)
      init_data[i].insert_action(put)
      pick.children.append(put)

      esolve.children.append(pick)

    return particles



################## Viewer #############################################
viewer = pl.make_frame_viewer(1280, 720)

viewer.insert_action(pl.make_terminate_action())
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [viewer]

################## Environment(s) #############################################

###
# Objects
###
circles = get_circles(1280, 720, 100)

particles = get_particles(circles)

game_content = game_content + circles + particles
  

hanger_color = (255, 30, 30)


# Generate random starting position
random_start_x = random.randint(0, 1200)
random_start_y = random.randint(0, 600)

test_bound = (random_start_x, random_start_y, 150, 100)
test = at.make_rectangle(test_bound, hanger_color)
test.name = "testing"

test.insert_action(at.make_draw_rectangle_action())
game_content.append(test)


###
# Create timer
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

game_looper = pl.make_game_looper(game_content)
game_looper.loop()
