class DragForceAction:
    def __init__(self):
        self.types = ["force"]
        self.entity_state = None
        self.name = "drag_force_action"
        self.verbose = False
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0,len(data.acceleration)):
              if data.active_particle[i]:
                data.acceleration[i][0] = data.acceleration[i][0] - data.velocity[i][0] * self.entity_state.drag_constant
                data.acceleration[i][1] = data.acceleration[i][1] - data.velocity[i][1] * self.entity_state.drag_constant
            # Handle collision via children
            for c in self.children:
                c.act(data)
            if self.verbose:
                print( self.name + " for " + self.entity_state.name)
        return
