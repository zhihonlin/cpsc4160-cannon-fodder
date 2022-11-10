from pygame.locals import *


class ButtonPressed:
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "button_pressed_action"
        self.children = []
        self.verbose = False

    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if event.type == MOUSEBUTTONDOWN:
            # check whether the mouse button is down inside the button area
            pos = event.pos
            mouse_is_inside = self.entity_state.is_inside(pos)
            return mouse_is_inside
        return False

    def act(self, event, game_content):
        if self.condition_to_act(event):

            for c in self.children:
                c.act(event)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return
