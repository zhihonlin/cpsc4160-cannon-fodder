import pygame
class DrawHUDAction():
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_HUD_action"
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
            
        totalObj = pygame.font.SysFont(self.entity_state.font, self.entity_state.font_size)
        total = totalObj.render(self.entity_state.total_message, True, self.entity_state.color)

        ##Create pygame text objects
        successObj = pygame.font.SysFont(self.entity_state.font, self.entity_state.font_size)
        success = successObj.render(self.entity_state.success_message, True, self.entity_state.color)

        ##Draws the HUD text to the screen
        screen.blit(total, (self.entity_state.pos))
        screen.blit(success, (self.entity_state.pos[0],self.entity_state.pos[1] +50))
        return