#!/usr/bin/env python

'''
hardware class init the needed resources for the pitft display or init a normal 
display when no pitft is selected. It also define the size of the display and 
set the mouse cursor visibility.
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

import sys, os
import pygame

class hardware:

    def __init__(self, interface):
		# pitft is attached?
		self.interface = interface
		#set size of the screen
		size = width, height = 320, 240

		if self.interface:
			"Inititializes a new pygame screen using the framebuffer"
			# variables for pitft screen and touchscreen
			os.environ['SDL_FBDEV'] = '/dev/fb1'
			os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
			os.environ["SDL_MOUSEDRV"] = "TSLIB"
			# init pygame module
			pygame.init()
			# set size of the screen
			self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
			# set mouse visibility
			pygame.mouse.set_visible(False)
			pygame.display.update()
			
		else:
			# init normal pygame display
			pygame.init()
			# create a screen in defined size
			self.screen = pygame.display.set_mode(size)
			# set mouse visibility
			pygame.mouse.set_visible(True)
			#render the screen
			pygame.display.update()

    def get_screen(self):
    	''' return the actual used screen '''
    	return(self.screen)

    def update_screen(self):
    	pygame.display.update()
	



