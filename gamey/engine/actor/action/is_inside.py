# Checks if particle is inside the rest area
class InsideRectangleAction:
    def __init__(self):
        self.types = [""]
        self.entity_state = None
        self.name = "inside_rectangle_action"
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
            for i in range(0,len(data.acceleration)):
                if data.position[i][0] < self.entity_state.pos[0]:
                    continue
                if data.position[i][0] > self.entity_state.length + self.entity_state.pos[0]:
                    continue
                if data.position[i][1] < self.entity_state.pos[1]:
                    continue
                if data.position[i][1] > self.entity_state.width + self.entity_state.pos[1]:
                    continue
                self.children[0].act(data,i)
            if self.verbose:
                print( self.name + " for " + self.entity_state.name)
        return
