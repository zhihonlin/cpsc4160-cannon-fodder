#
# Rectangular basic button
#
class Rectangle:
    def __init__(self, length, width, color=(128, 128, 128), name="rectangle"):
        self.length = length
        self.width = width
        self.color = color # (r,g,b)
        self.pos = [0,0]
        #self.message = msg # Member variable for the message in a message button
        self.template = None # Member variable for the image template in a template button
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return
 # Check whether a position is inside the bounds
    ''' def is_inside( self, pos):
        if pos[0] < self.bounds[0]:
            return False
        if pos[0] > self.bounds[2] + self.bounds[0]:
            return False
        if pos[1] < self.bounds[1]:
            return False
        if pos[1] > self.bounds[3] + self.bounds[1]:
            return False
        return True '''