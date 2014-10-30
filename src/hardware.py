#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

import sys, os
import pygame

class hardware:

    def __init__(self, interface):
		self.interface = interface
		self.left = pygame.K_LEFT
		self.right = pygame.K_RIGHT
		self.select = pygame.K_RETURN
		if self.interface:
			"Ininitializes a new pygame screen using the framebuffer"
        	# Based on "Python GUI in Linux frame buffer"
        	# http://www.karoltomala.com/blog/?p=679
			disp_no = os.getenv("DISPLAY")
			if disp_no:
				print "I'm running under X display = {0}".format(disp_no)
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
			self.screen = pygame.display.set_mode((320,240), pygame.FULLSCREEN)
			pygame.mouse.set_visible(False)
			# Render the screen
			pygame.display.update()
		else:
			pygame.init()
			self.screen = pygame.display.set_mode((320,240))
			pygame.mouse.set_visible(True)
			pygame.display.update()

    def __del__(self):
        pass

    def getScreen(self):
    	return(self.screen)
	
	def LEFT(self):
		if GPIO.input(22):
			print "22"
		return self.left

	def RIGHT(self):
		return self.right

	def SELECT(self):
		return self.select
