###
# Entities
###


def make_frame_viewer(width, height):
    import gamey.engine.play.entity.frameviewer as fv
    view = fv.FrameViwer(width, height)
    return view

def make_game_looper( content ):
    import gamey.engine.play.entity.gameloop as gl
    loop = gl.GameLooper()
    loop.game_content = content
    for entity in content:
        loop.insert_entity(entity)
    return loop

###
### Actions
###

def make_screen_display_action():
    import gamey.engine.play.action.display as dp
    return dp.Display()

def make_terminate_action():
    import gamey.engine.play.action.terminate as tm
    return tm.Terminate()