import pygame, time
 
class EmitSound: 
    def __init__(self, sound_path = ""): 
        self.types = [""] 
        self.entity_state = None 
        self.sound_path = sound_path
        self.name = "emit_sound_action" 
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
            pygame.mixer.init()
            soundObj = pygame.mixer.Sound(self.sound_path)
            soundObj.play()

            for c in self.children: 
                c.act(event) 
            if self.verbose: 
                print( self.name + " has count of " + self.entity_state.count) 
        return