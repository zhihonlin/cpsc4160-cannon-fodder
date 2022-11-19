#
# RectangleCollider entity
#
class RectangleCollider:
    def __init__(self, llc=[0.0,0.0], urc=[100.0,100.0], name="rectangle_collider"):
        self.llc = llc
        self.urc = urc
        # Default entity atrributes
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return