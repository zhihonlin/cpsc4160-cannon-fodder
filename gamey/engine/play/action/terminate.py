import pygame


class Terminate:
    def __init__(self):
        # one or more types to assign to this action
        # the specific types “event”, “loop”, “display”
        # are picked up and used by the game looper.
        # Any other types are for your organization convenience.
        self.types = ["event"]
        # This class variable is assigned by the entity’s insert_action call
        self.entity_state = None
        self.name = "terminate_action"            # Names are frequently useful
        self.verbose = False                    # verbose flags are handy
        # List of child actions that this action may choose to call
        self.children = []

    # Check whether conditions are right for running this action
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data.type == pygame.QUIT:
            return True
        if data.type == pygame.KEYDOWN:
            if data.key == pygame.K_ESCAPE:
                return True
        return False

    # Run this action if the conditions are right
    def act(self, data, game_content):
        # Check whether the conditions are right
        if self.condition_to_act(data):
            # … things to do that are specific to this action …
            pygame.quit()
            exit()
        return
