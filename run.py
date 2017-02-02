"""
File where the game is executed
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
    world = GameWorld(None, (1224, 900), (1224, 900))
    world.run()

if __name__ == '__main__':
    run()
