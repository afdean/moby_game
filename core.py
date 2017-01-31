"""
File containing main functions to run the game
"""

import sys
import math
import random
import time
import pygame
import numpy
from pygame.locals import *

class GameWorld():

    """
    Overarching structure holding the screen, actors, objects, etc.
    """

    def __init__(self, seed, worlddimensions, screendimensions):
        #initialize random seed
        self.time = time.time()
        random.seed(self.time)
        #initialize pygame and set up screen and background surface
        pygame.init()
        screen = pygame.display.set_mode(screendimensions)
        # Background surface that will hold everything
        background = pygame.Surface(worlddimensions)
        background = background.convert()
        background.fill((150, 0, 150))
        # Debug surface
        #debug = pygame.Surface(worlddimensions)
        #debug = debug.convert()
        #debug.fill((255, 255, 255))
        #background.blit(debug, (0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        #store stuff
        self.screen = screen
        self.seed = seed or self.time
        self.background = background
        #self.debug = debug
