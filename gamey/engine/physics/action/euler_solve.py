class EulerSolveAction:
    def __init__(self):
        self.types = ["physics"]
        self.dt = 1.0
        self.entity_state = None
        self.name = "euler_solve_action"
        self.verbose = False
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        #If there are fewer than 2 children, then solver is unusable
        if len(self.children) < 2:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act(data)
            self.children[1].act(data)
            # Handle collision via children
            for c in self.children[2:]:
                c.act(data)
            if self.verbose:
                print( self.name + " for " + self.entity_state.name)
        return
