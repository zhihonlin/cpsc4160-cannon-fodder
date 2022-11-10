#
# Total counter of squares
#
class Total_Counter:
    def __init__(self,name="total_counter"):
        self.count = 1
        #self.message = msg # Member variable for the message in a message button
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return