#
# HUD UI Element
#
class HUD:
    def __init__(self, font="Comic Sans MS", font_size = 20, color=(128,128,128), name="hud", ):
        self.font = font
        self.font_size = font_size
        self.color = color
        self.pos = (20,20)
        self.total_message = "Total: 1"
        self.success_message = "Success: 0"
        #self.message = msg # Member variable for the message in a message button
        self.template = None # Member variable for the image template in a template button
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return