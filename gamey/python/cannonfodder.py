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
NX = 1280
NY = 720


################## Generate Circles #############################################
def get_circles(nx, ny, nb):
    circles = []
    radius = 10
    for i in range(0, nb):
        random_x = random.randint(0, nx/2+50)
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
def get_particles(init_data, boxes, nx, ny):
    import gamey.engine.physics as ps
    particles = []

    parts = ps.make_particles()
    particles.append(parts)

    for d in init_data:
      position = list(d.center)
      velocity = [ 10, 1]
      mass = 1
      parts.add_particle(position,velocity,mass)
    
    # Spring force
    spring = ps.make_spring_force()
    spring.spring_constant = 0.001
    spring_action = ps.make_spring_action()
    spring.insert_action(spring_action)

    # drag force
    drag = ps.make_drag_force()
    drag.drag_constant = 0.03

    # Simple gravity force
    gravity = ps.make_gravity_force()
    gravity.gravity = [0.0,0.05]
    grav_action = ps.make_gravity_action()
    gravity.insert_action(grav_action)

    # Position Solve
    psolve = ps.make_position_solve()
    parts.insert_action(psolve)

    # Velocity Solve
    vsolve = ps.make_velocity_solve()
    parts.insert_action(vsolve)
    vsolve.children.append(grav_action)
    vsolve.children.append(spring_action)

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

    # Collision with the window frame
    window_frame_collider = ps.make_rectangle_collider( [0,0], [nx, ny])
    collisions = ps.make_inside_rectangle_collision()
    window_frame_collider.insert_action(collisions)
    psolve.children.append(collisions)

    outside_boxes = []
    # Collision with the a rectangle in middle
    for count, b in enumerate(boxes):
        llc = list(b.pos)
        urc = list(llc)
        urc[0] = urc[0] + b.length
        urc[1] = urc[1] + b.width
        box_collider = ps.make_rectangle_collider(llc, urc)
        box_collider.name = box_collider.name + "_" + str(count) 
        outside_boxes.append(box_collider)
        ## outside collision actions
        outside_collisions = ps.make_outside_rectangle_collision()
        outside_collisions.name = outside_collisions.name + "_" + str(count)
        box_collider.insert_action(outside_collisions)
        psolve.children.append(outside_collisions)

    ###
    # Create timer and remove barrier at 9 seconds mark
    ###
    timer = ut.make_timer()
    start_timer_action = ut.make_start_timer_action()
    update_timer_action = ut.make_update_timer_action()
    alarm_action = ut.make_alarm_action(9)

    timer.insert_action(start_timer_action)
    timer.insert_action(update_timer_action)
    timer.insert_action(alarm_action)

    # Timer for closing off the barriers
    timer2 = ut.make_timer()
    start_timer_action2 = ut.make_start_timer_action()
    update_timer_action2 = ut.make_update_timer_action()
    alarm_action2 = ut.make_alarm_action(18)

    timer2.insert_action(start_timer_action2)
    timer2.insert_action(update_timer_action2)
    timer2.insert_action(alarm_action2)
    # Move alarm into the loop
    update_timer_action.children.append(alarm_action)
    update_timer_action.children.append(alarm_action2)
    # Set up activation/deactivation
    timer_deactivate = ut.make_deactivate_action()
    box_deactivate = ut.make_deactivate_action()
    box_collider_deactivate = ut.make_deactivate_action()
    box_activate = ut.make_activate_action()
    box_collider_activate = ut.make_activate_action()

    timer.insert_action(timer_deactivate)
    boxes[1].insert_action(box_deactivate)
    outside_boxes[1].insert_action(box_collider_deactivate)
    boxes[1].insert_action(box_activate)
    outside_boxes[1].insert_action(box_collider_activate)
    # Alarm triggered, move the mole and reset timer

    alarm_action.children.append(start_timer_action)
    alarm_action.children.append(box_deactivate)
    alarm_action.children.append(box_collider_deactivate)

    alarm_action2.children.append(timer_deactivate)
    alarm_action2.children.append(start_timer_action2)
    alarm_action2.children.append(box_activate)
    alarm_action2.children.append(box_collider_activate)

    particles.append(timer)
    particles.append(timer2)

    # Create rectangle at bottome
    deact_rect = at.make_rectangle(nx-(nx/2+200),ny,(0,0,0))
    deact_rect.fill = 1
    deact_rect.pos = [nx/2+200, 0]
    deact_rect.insert_action(at.make_draw_rectangle_action())
    is_inside = at.make_inside_rectangle_action()
    deact_rect.insert_action(is_inside)
    vsolve.children.append(is_inside)

    deact = ps.make_deactivate_action()
    drag.insert_action(deact)
    is_inside.children.append(deact)

    particles.append(deact_rect)


    ''' for count, b in enumerate(parts.acceleration):
        deact = ps.make_deactivate_action(count)
        drag.insert_action(deact)
        vsolve.children.append(deact) '''

    act_force =  ps.make_activate_action(0)
    drag.insert_action(act_force)
    vsolve.children.append(act_force)

    return particles

def get_boxes(nx,ny):
    boxes = []
    # Create rectangle on top
    top_rect = at.make_rectangle(100,ny/3,(255,255,255))
    top_rect.pos = [nx/2+100, 0]
    top_rect.insert_action(at.make_draw_rectangle_action())
    boxes.append(top_rect)
    
    # Create rectangle in middle
    mid_rect = at.make_rectangle(100,ny/8,(255,255,255))
    mid_rect.pos = [nx/2+100, ny/3]
    mid_rect.insert_action(at.make_draw_rectangle_action())
    boxes.append(mid_rect)

    # Create rectangle at bottome
    bot_rect = at.make_rectangle(100,ny-ny/8-ny/3,(255,255,255))
    bot_rect.pos = [nx/2+100, ny/3+ny/8]
    bot_rect.insert_action(at.make_draw_rectangle_action())
    boxes.append(bot_rect)

    # Create top rectangle inside non-gravity field 
    inside_top_rect = at.make_rectangle(200,20,(255,255,255))
    inside_top_rect.pos = [nx/2+350, ny-200]
    inside_top_rect.insert_action(at.make_draw_rectangle_action())
    boxes.append(inside_top_rect)

    # Create bottom rectangle inside non-gravity field 
    inside_bot_rect = at.make_rectangle(200,20,(255,255,255))
    inside_bot_rect.pos = [nx/2+250, ny-50]
    inside_bot_rect.insert_action(at.make_draw_rectangle_action())
    boxes.append(inside_bot_rect)
    return boxes
    
################## Viewer #############################################
viewer = pl.make_frame_viewer(NX, NY)

viewer.insert_action(pl.make_terminate_action())
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [viewer]

################## Environment(s) #############################################

###
# Objects
###
circles = get_circles(NX, NY, 100)


boxes = get_boxes(NX, NY)

particles = get_particles(circles,boxes,NX,NY)

''' redraw_boxes = get_boxes(NX,NY) '''

game_content = game_content + circles + particles + boxes

################## Looper #############################################

game_looper = pl.make_game_looper(game_content)
game_looper.loop()
