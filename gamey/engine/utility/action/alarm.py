from pygame.locals import * 
import time

class Alarm: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "Alarm_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, event): 
        if self.entity_state == None: 
            return False 
        if self.entity_state.active == False: 
            return False 
        if self.entity_state.elapsed_time() >= 1.2:
            return True
        return False 
 
    def act(self, event): 
        if self.condition_to_act(event):
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return