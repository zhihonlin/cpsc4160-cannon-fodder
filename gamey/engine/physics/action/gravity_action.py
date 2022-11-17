class GravityForceAction:
    def __init__(self):
        self.types = ["force"]
        self.entity_state = None
        self.name = "gravity_force_action"
        self.verbose = False
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        #If there are fewer than 2 children, then solver is unusable
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0,len(data.acceleration)):
              if data.active_particle[i]:
                data.acceleration[i][0] = data.acceleration[i][0] + self.entity_state.gravity[0]
                data.acceleration[i][1] = data.acceleration[i][1] + self.entity_state.gravity[1] 
            # Handle collision via children
            for c in self.children:
                c.act(data)
            if self.verbose:
                print( self.name + " for " + self.entity_state.name)
        return
