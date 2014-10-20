import pygame 
import sys, os, time
from pygame.locals import * 
import menu
import controls

def loadImage(filename, colorkey = None):
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

def init():
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    screen.blit(loadImage("images/bg.jpg"), (0, 0))
    pygame.display.update()


def event_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                sys.exit()

def main(): 
	init()
	event_loop()

# Check, if this is the main file 
if __name__ == '__main__': 
	sys.exit(main())