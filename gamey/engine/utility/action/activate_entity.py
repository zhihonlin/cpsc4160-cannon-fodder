from pygame.locals import * 
 
class ActivateEntity: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "Activate_entity_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        return True 
 
    def act(self, event): 
        if self.condition_to_act(event):
            self.entity_state.active = True
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return