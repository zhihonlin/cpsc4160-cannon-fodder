import pygame
from pygame.locals import *


class FrameViwer():
    def __init__(self, width, height, mode=RESIZABLE | DOUBLEBUF, depth=32, title="Game Window", name="frameviewer"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), mode, depth)
        pygame.display.set_caption(title)
        self.dimention = [width, height]
        self.mode = mode
        self.depth = depth
        self.title = title
        self.answer = ""
        self.guessed_letter = ""        #Keep track of what letters are guessed
        self.actions = []          # The actions that dictate what happens with this entity
        self.name = name          # Names are handy for diagnostics and tracking
        self.verbose = False       # Useful for deciding to show info or not
        self.active = True        # Decide whether or not you want this entity to be active
        return

    def insert_action(self, a):     # append an input action to the self.actions list,
                                    # and set the input actions entity_state to this entity
        a.entity_state = self
        self.actions.append(a)
        return

    def terminate(self):
        from sys import exit
        if self.verbose:
            print(self.name + " terminating")
        pygame.quit()
        exit()

