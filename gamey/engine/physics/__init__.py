###
# Entities
###


def make_particles():
    import gamey.engine.physics.entity.particle as pc
    particle = pc.Particle()
    return particle

def make_gravity_force():
    import gamey.engine.physics.entity.gravity_force as gf
    gravity = gf.GravityForce()
    return gravity

def make_spring_force():
    import gamey.engine.physics.entity.spring_force as sf
    spring = sf.SpringForce()
    return spring

def make_drag_force():
    import gamey.engine.physics.entity.drag_force as df
    drag = df.DragForce()
    return drag

def make_rectangle_collider(llc, urc):
    import gamey.engine.physics.entity.rectangle_collider as rc
    rectangle_collider = rc.RectangleCollider(llc, urc)
    return rectangle_collider

###
### Actions
###

def make_gravity_action():
    import gamey.engine.physics.action.gravity_action as ga
    gravity_action = ga.GravityForceAction()
    return gravity_action

def make_spring_action():
    import gamey.engine.physics.action.spring_action as sa
    spring_action = sa.SpringForceAction()
    return spring_action

def make_drag_action():
    import gamey.engine.physics.action.drag_force_action as dfa
    drag_action = dfa.DragForceAction()
    return drag_action


def make_euler_solve():
    import gamey.engine.physics.action.euler_solve as es
    euler = es.EulerSolveAction()
    return euler

def make_position_solve():
    import gamey.engine.physics.action.position_solve as ps
    position = ps.PositionSolveAction()
    return position

def make_velocity_solve():
    import gamey.engine.physics.action.velocity_solve as vs
    velocity = vs.VelocitySolveAction()
    return velocity

def make_pick_position(index):
    import gamey.engine.physics.action.pick_position as pp
    pick = pp.PickPositionAction(index)
    return pick

def make_outside_rectangle_collision():
    import gamey.engine.physics.action.outside_rectangle_collision as oco
    outside_collision = oco.OutsideRectangleCollisionAction()
    return outside_collision

def make_inside_rectangle_collision():
    import gamey.engine.physics.action.inside_rectangle_collision as ico
    inside_collision = ico.InsideRectangleCollisionAction()
    return inside_collision
