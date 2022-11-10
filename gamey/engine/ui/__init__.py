###
### Entities
###
def make_basic_button( bounds, color ):
    import gamey.engine.ui.entity.basic_button as bb
    result = bb.Basic_Button(bounds,color)
    return result


def make_hud(font,font_size,color):
    import gamey.engine.ui.entity.hud as hud
    result = hud.HUD(font,font_size,color)
    return result

###
### Actions
###
def make_draw_button_action():
    import gamey.engine.ui.action.draw_button as db
    return db.DrawBaiscButtonAction()

def make_draw_hud_action():
    import gamey.engine.ui.action.draw_hud as dh
    return dh.DrawHUDAction()

def make_button_pressed_action():
    import gamey.engine.ui.action.press_key as pk
    return pk.ButtonPressed()