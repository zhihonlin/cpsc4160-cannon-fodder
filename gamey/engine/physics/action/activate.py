from pygame.locals import * 
 
class Activate: 
    def __init__(self, particle_index): 
        self.types = [""] 
        self.particle_index = particle_index
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
 
    def act(self, data): 
        if self.condition_to_act(data):
            data.acceleration[self.particle_index][0] = data.acceleration[self.particle_index][0] - data.velocity[self.particle_index][0] * 0
            data.acceleration[self.particle_index][1] = data.acceleration[self.particle_index][1] - data.velocity[self.particle_index][1] * 0
            for c in self.children: 
                c.act(data) 
            if self.verbose: 
                print( self.name + " for " + self.entity_state.name) 
        return