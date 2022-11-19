#
# Force entity
#
class DragForce:
    def __init__(self, name="drag_force"):
        self.drag_constant = 0.1
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
