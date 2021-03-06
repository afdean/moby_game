"""
Module where details of GameWorld are initialized and executed
"""

import sys
import math
import random
import time
import pygame
import numpy
from pygame.locals import *
from constants import *
from core import *

def run():
    """
    Method to pass details into GameWorld, and other game objects
    """

    world = GameWorld()
    player = Player(world, HERO, CENTER, None, None)
    world.add_mover(player)
    world.run()

if __name__ == '__main__':
    run()
