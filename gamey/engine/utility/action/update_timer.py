from pygame.locals import * 

class UpdateTimer: 
    def __init__(self): 
        self.types = ["loop"] 
        self.entity_state = None 
        self.name = "Update_timer_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        return True 
 
    def act(self, event): 
        if self.condition_to_act(event):
            self.entity_state.tick()

            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return