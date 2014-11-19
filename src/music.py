'''
music class contains all needed functions for control the music of the pygame
module including the functionalities for the play bar
'''

# python imports
import sys, os
import pygame

# pi-gui imports
from interfaces import Interface
from utils import save_progress, str2time

class Player:

	def __init__(self, book):
		# init the mixer of pygame module
		pygame.mixer.init()
		self.interface = Interface()
		# load actual audio book object
		self.book = book
		# set position to position in audio book class
		self.position = self.book.getPosition()
		# load actual audio book to mixer
		pygame.mixer.music.load(book.getPath())
		# set playing status
		self.playing = pygame.mixer.music.get_busy()
		

	def get_status(self):
		''' get mixer status '''
		return self.playing

	def set_status(self, bool):
		''' set new mixer status '''
		self.playing = bool

	def play(self):
		''' play or stop the music depnding on play status '''
		if not pygame.mixer.music.get_busy():
			self.set_status(True)
			pygame.mixer.music.play(-1, self.position)
		else:
			self.stop()

	def pause(self):
		''' pause or unpause music depending on play status '''
		if self.get_status():
			pygame.mixer.music.pause()
			self.set_status(False)
		else:
			pygame.mixer.music.unpause()
			self.set_status(True)

	def stop(self):
		''' stop actual playing an store path and position to cache file '''
		self.set_status(False)
		save_progress(self.book.getPath(), pygame.mixer.music.get_pos())
		pygame.mixer.music.stop()


	def get_pos(self):
		''' get actual position of audio book '''
		return pygame.mixer.music.get_pos()

	def set_pos(self, pos):
		''' restart playing depending on selected position on playbar '''
		factor = str2time(self.book.getPlaytime())/300
		self.position = (pos-10)*factor/1000
		self.play()

