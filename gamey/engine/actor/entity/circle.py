#
# Rectangular basic button
#
class Circle:
    def __init__(self, color=(128, 128, 128), center=(0,0), radius=20, name="circle"):
        self.color = color # (r,g,b)
        #self.message = msg # Member variable for the message in a message button
        self.template = None # Member variable for the image template in a template button
        self.center = center
        self.radius = radius
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return