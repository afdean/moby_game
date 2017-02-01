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

from constants import *

class GameWorld():

    """
    Overarching structure holding the screen, actors, objects, etc.
    """

    def __init__(self, seed, world_dimensions, screen_dimensions):
        # Initialize random seed
        self.time = time.time()
        random.seed(self.time)

        # Initialize pygame and set up screen and background surface
        pygame.init()
        screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption('Moby')

        # Background surface that will hold everything
        background = pygame.Surface(world_dimensions)
        background = background.convert()
        background.fill((150, 0, 150))

        # Debug surface
        #debug = pygame.Surface(world_dimensions)
        #debug = debug.convert()
        #debug.fill((255, 255, 255))

        #background.blit(debug, (0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Store information about the game
        self.screen = screen
        self.seed = seed or self.time
        self.background = background

        #self.debug = debug

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(TICK_RATE)
            delta = clock.get_rawtime()
            self.handleEvents()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            #elif event.type == KEYDOWN:
                #if event.key == K_ESCAPE:
                    #pygame.quit()
                    #sys.exit(0)
