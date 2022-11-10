import pygame

class GameLooper():
    def __init__(self, name="Game looper"):
        self.game_content = None
        self.loop_content = []
        self.event_content = []
        self.display_content = []
        self.display_data = None
        self.name = name
        self.verbose = False
        self.active = True
        return

    def insert_entity(self, e):
        if self.verbose:
            print("inserting entity " + e.name)
        if e.name == "frameviewer":
            self.display_data = e.screen
        for a in e.actions:
            self.insert_action(a)
        return

    def insert_action(self, a):
        if "event" in a.types:
            self.event_content.append(a)
            if self.verbose:
                print( "\t" + self.name + " added " + a.name + " event action")
        elif "loop" in a.types:
            self.loop_content.append(a)
            if self.verbose:
                print( "\t" + self.name + " added " + a.name + " loop action")
        elif "display" in a.types:
            self.display_content.append(a)
            if self.verbose:
                print( "\t" + self.name + " added " + a.name + " display action")
        return
    
    def loop(self):
        #infinite looper
        while self.active:
            events = pygame.event.get()
            for e in events:
                for a in self.event_content:
                    a.act(e,self.game_content)
            for a in self.loop_content:
                a.act(None)
            for a in self.display_content:
                a.act(self.display_data)
            if self.verbose:
                print(self.name + " is using verbose mode")
        
        return
                