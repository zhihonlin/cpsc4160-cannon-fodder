from pygame.locals import * 
 
class Activate: 
    def __init__(self): 
        self.types = [""] 
        self.entity_state = None 
        self.name = "Aactivate_force_action" 
        self.children = [] 
        self.verbose = False
 
    def condition_to_act(self, data): 
        if self.entity_state == None: 
            return False 
        elif data.active_particle[self.particle_index] == False:
            return False
        return True 
 
    def act(self, data, index): 
        if self.condition_to_act(data):
            data.active_force[index] = True
            data.acceleration[index][0] = data.acceleration[index][0] - data.velocity[index][0] * 0.0
            data.acceleration[index][1] = data.acceleration[index][1] - data.velocity[index][1] * 0.0
            for c in self.children: 
                c.act(data) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return