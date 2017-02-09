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
    Considered to be like an abstract interface
    """

    #Note that this method might need to be renamed since sprite
    #Has an update method
    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def collision(self, thing):
        pass

class Mover(pygame.sprite.Sprite, Thing):

    """
    Base model for every movable object
    Still abstract class from Thing inheritance
    Mover should never be instantiated itself
    """

    def __init__(self, world, image, position, orientation, speed):
        # Every sprite must be initialized this way
        pygame.sprite.Sprite.__init__(self)

    #Put abstract methods every mover requires here

class Player(Mover):

    """
    Base model for agent a player can control
    May continue to be abstract due to more abstract methods as we decide on modelling later
    For now, PlayerAgent is instantiable
    """

    #Will include more arguments in constructor as required
    def __init__(self, world, image, position, orientation, speed):
        super(Player, self).__init__(world, image, position, orientation, speed)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        #Center of rect is directly in center of screen
        self.rect.center = position
        self.orientation = orientation
        self.speed = speed
        self.dist_x = 0
        self.dist_y = 0

    # Implement later
    def update(self, delta):
        self.dist_x = 0
        self.dist_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w] and keystate[pygame.K_a]:
            self.dist_x = -5
            self.dist_y = -5
        elif keystate[pygame.K_w] and keystate[pygame.K_d]:
            self.dist_x = 5
            self.dist_y = -5
        elif keystate[pygame.K_s] and keystate[pygame.K_a]:
            self.dist_x = -5
            self.dist_y = 5
        elif keystate[pygame.K_s] and keystate[pygame.K_d]:
            self.dist_x = 5
            self.dist_y = 5
        elif keystate[pygame.K_w]:
            self.dist_x = 0
            self.dist_y = -5
        elif keystate[pygame.K_a]:
            self.dist_x = -5
            self.dist_y = 0
        elif keystate[pygame.K_s]:
            self.dist_x = 0
            self.dist_y = 5
        elif keystate[pygame.K_d]:
            self.dist_x = 5
            self.dist_y = 0
        self.rect.x += self.dist_x
        self.rect.y += self.dist_y

    #Implement later
    def collision(self, thing):
        return None

class GameWorld():

    """
    Overarching structure holding the screen, actors, objects, etc.
    """

    def __init__(self):
        # Initialize random seed
        self.time = time.time()
        random.seed(self.time)

        # Initialize pygame and its attributes:
        # Screen, mixer, clock, sprites and background surface
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(CAPTION)
        clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        mover_sprites = pygame.sprite.Group()

        # Background surface that will hold everything
        background = pygame.Surface(WORLD_SIZE)
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
        self.seed = self.time
        self.background = background
        self.clock = clock
        self.all_sprites = all_sprites
        self.mover_sprites = mover_sprites

        #self.debug = debug

    def run(self):
        """
        Main game loop (inputs, update and render)
        """

        while self.running:
            # Update time
            self.clock.tick(TICK_RATE)
            delta = self.clock.get_rawtime()

            # Handle inputs
            self.handle_inputs()

            # Update game state
            # Consider/will? replacing this when objects concretely implement update
            self.all_sprites.update(delta)

            # Rendering
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def add_sprite(self, sprite):
        self.all_sprites.add(sprite)

    def add_mover(self, mover):
        self.add_sprite(mover)
        self.mover_sprites.add(mover)
