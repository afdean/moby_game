"""
File containing main functions to run the game
"""
from __future__ import print_function
from abc import ABC, abstractmethod
import sys
import math
import random
import time
import pygame
import numpy
from pygame.locals import *
from constants import *

class Thing(ABC):

    """
    Base model for every 'tangible' object in the world
    """

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def collision(self, thing):
        pass

# class Mover(pygame.sprite.Sprite, Thing):

#     """
#     Base model for every movable object
#     """

#     def __init__(self, image, position, orientation, speed, world):
#         pygame.sprite.Sprite.__init__(self)

#class PlayerAgent(Mover):

class GameWorld():

    """
    Overarching structure holding the screen, actors, objects, etc.
    """

    def __init__(self, seed, world_dimensions, screen_dimensions):
        # Initialize random seed
        self.time = time.time()
        random.seed(self.time)

        # Initialize pygame and its attributes:
        # Screen, mixer, clock and background surface
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(CAPTION)
        clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()

        # Background surface that will hold everything
        background = pygame.Surface(world_dimensions)
        background = background.convert()
        background.fill(WHITE)

        # Debug surface
        #debug = pygame.Surface(world_dimensions)
        #debug = debug.convert()
        #debug.fill((255, 255, 255))

        #background.blit(debug, (0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Store game attributes
        self.running = True
        self.screen = screen
        self.seed = seed or self.time
        self.background = background
        self.clock = clock
        self.all_sprites = all_sprites

        #self.debug = debug

    def run(self):
        while self.running:
            #Update time
            self.clock.tick(TICK_RATE)
            delta = self.clock.get_rawtime()

            #Handle inputs
            self.handle_inputs()

            #Update game state

            #Rendering
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def set_player_agent(self, player_agent):
        self.all_sprites.add(player_agent)
