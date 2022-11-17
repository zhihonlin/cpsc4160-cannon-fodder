import pygame
class DrawCircleButtonAction():
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_circle_button_action"
        return

    def condition_to_act(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self,data):
        if self.condition_to_act(data):
            self.draw(data)
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        if self.verbose:
            print("Currently drawing")
        pygame.draw.circle(screen, self.entity_state.color, self.entity_state.center, self.entity_state.radius)
        return