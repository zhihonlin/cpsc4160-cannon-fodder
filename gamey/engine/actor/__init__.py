###
### Entities
###
def make_rectangle( length,width, color ):
    import gamey.engine.actor.entity.rectangle as rt
    result = rt.Rectangle(length,width,color)
    return result

def make_round(color, center, radius):
    import gamey.engine.actor.entity.circle as cr
    result = cr.Circle(color, center,radius)
    return result


###
### Actions
###
def make_draw_rectangle_action():
    import gamey.engine.actor.action.draw_rectangle as dr
    return dr.DrawRectButtonAction()

def make_draw_circle_action():
    import gamey.engine.actor.action.draw_circle as dc
    return dc.DrawCircleButtonAction()

def make_put_position_action():
    import gamey.engine.actor.action.put_position as ppos
    return ppos.PutPositionAction()

def make_inside_rectangle_action():
    import gamey.engine.actor.action.is_inside as ii
    return ii.InsideRectangleAction()