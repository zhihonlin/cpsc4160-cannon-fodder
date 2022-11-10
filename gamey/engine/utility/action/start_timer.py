from pygame.locals import * 
import time

class StartTimer: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "Start_timer_action" 
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
            self.entity_state.start_time = time.time()
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return