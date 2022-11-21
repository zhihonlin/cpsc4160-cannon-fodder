from pygame.locals import * 
 
class Deactivate: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "Deactivate_force_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, data): 
        if self.entity_state == None: 
            return False
        return True 
 
    def act(self, data, index): 
        if self.condition_to_act(data):
            data.active_force[index] = False
            ''' data.acceleration[index][0] = -0.00000005
            data.acceleration[index][1] = -0.00000005 '''
            data.acceleration[index][0] = data.acceleration[index][0] - data.velocity[index][0] * self.entity_state.drag_constant
            data.acceleration[index][1] = data.acceleration[index][1] - data.velocity[index][1] * self.entity_state.drag_constant
            #print(data.acceleration[index][1])
            for c in self.children: 
                c.act(data) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return