import time
#
# Timer class
#
class Timer:
    def __init__(self, name="basic_button"):
        self.start_time =  time.time()
        self.current_time = time.time() # (r,g,b)
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
    
    def tick(self):
        self.current_time = time.time()

    def elapsed_time(self):
        return self.current_time - self.start_time