class OutsideRectangleCollisionAction:
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "outside_rectangle_action"
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
        if self.condition_to_act (data):
            for i in range(0,len (data.position)): 
                if data.active_particle[i]:
                    # Step 1: make sure it is inside the rectangle
                    if data.position[i][0] > self.entity_state.llc[0] and data.position[i][0] < self.entity_state.urc[0]:
                        if data.position[i][1] > self.entity_state.llc[1] and data.position[i][1] < self.entity_state.urc[1]:
                            # Step 2 figure out which edge it passed through first
                            right_time = (data.position[i][0] - self.entity_state.llc[0])/data.velocity[i][0] 
                            if right_time < 0.0:
                                right_time = 100000000.0
                            left_time = (data.position[i][0] - self.entity_state.urc[0])/data.velocity[i][0]
                            if left_time < 0.0:
                                left_time = 100000000.0
                            top_time = (data.position[i][1] - self.entity_state.llc[1])/data.velocity[i][1]
                            if top_time < 0.0:
                                top_time = 100000000.0
                            bottom_time = (data.position[i][1] - self.entity_state.urc[1])/data.velocity[i][1]
                            if bottom_time < 0.0:
                                bottom_time = 100000000.0
                            minimum_time = min (right_time, left_time, top_time, bottom_time)
                            if right_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.llc[0] - data.position[i][0] 
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif left_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.urc[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif top_time == minimum_time:
                                data.position[i][1] = 2.0*self.entity_state.llc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
                            else:
                                data.position[1][1] = 2.0*self.entity_state.urc[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
            for c in self.children:
                c.act(data)
            if self.verbose:
                print(self.name +" for " + self.entity_state.name)
        return


