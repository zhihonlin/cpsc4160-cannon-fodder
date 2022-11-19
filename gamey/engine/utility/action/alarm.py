from pygame.locals import * 
import time

class Alarm: 
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time 
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
        if self.entity_state.elapsed_time() >= self.alarm_time:
            return True
        return False 
 
    def act(self, event): 
        if self.condition_to_act(event):
            print(self.entity_state.name)
            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return