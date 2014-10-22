#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# imports
import sys, os
import pygame

class Graphics:

  def __init__(self):
    pass

  def __del__(self):
    pass

  def loadImage(self, filename, colorkey = None):
  # load picture
    image = pygame.image.load(filename)
    # load picture with or without alpha channel
    if image.get_alpha() == None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    # set colorkey
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    # return loaded image
    return image



