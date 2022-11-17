class PositionSolveAction:
    def __init__(self, index):
        self.types = ["physics"]
        self.dt = 1.0
        self.entity_state = None
        self.name = "velocity_solve_action"
        self.verbose = False
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0, len(self.entity_state.acceleration)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.acceleration[i][0] = 0.0
                    self.entity_state.acceleration[i][1] = 0.0
            # Handle collision via children
            for c in self.children:
                c.act(self.entity_state)
            for i in range(0, len(self.entity_state.velocity)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.velocity[i][0] = self.entity_state.velocity[i][0] + self.dt * self.entity_state.acceleration[i][0]
                    self.entity_state.velocity[i][1] = self.entity_state.velocity[i][1] + self.dt * self.entity_state.acceleration[i][1]
            if self.verbose:
                print( self.name + " for " + self.entity_state.name)
        return
