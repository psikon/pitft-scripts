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
		if self.interface:
			"Inititializes a new pygame screen using the framebuffer"
        	# Based on "Python GUI in Linux frame buffer"
        	# http://www.karoltomala.com/blog/?p=679
			disp_no = os.getenv("DISPLAY")
			# print X window, wehre pitft is running
			if disp_no:
				print "I'm running under X display = {0}".format(disp_no)
			# variables for pitft screen
			os.putenv('SDL_FBDEV', '/dev/fb1') 
			# variables for touchscreen control
			os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
			os.environ["SDL_MOUSEDRV"] = "TSLIB"
			# Select frame buffer driver
			# Make sure that SDL_VIDEODRIVER is set
			driver = 'fbcon'
			if not os.getenv('SDL_VIDEODRIVER'):
				os.putenv('SDL_VIDEODRIVER', driver)
			try:
				pygame.init()
			except pygame.error:
				print 'Driver: {0} failed.'.format(driver)
				exit(0)
			# set size of the screen
			self.screen = pygame.display.set_mode((320,240), pygame.FULLSCREEN)
			# set mouse visibility
			pygame.mouse.set_visible(False)
			# Render the screen
			pygame.display.update()
		else:
			# init normal pygame display
			pygame.init()
			# create a screen in defined size
			self.screen = pygame.display.set_mode((320,240))
			# set mouse visibility
			pygame.mouse.set_visible(True)
			#render the screen
			pygame.display.update()

    def get_screen(self):
    	''' return the actual used screen '''
    	return(self.screen)
	

