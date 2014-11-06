#!/usr/bin/env python
''''''

# python imports
import sys, os
import pygame

# pi-gui imports
from graphics import Graphics

class Player:

	def __init__(self, book):
		pygame.mixer.init()
		self.book = book
		pygame.mixer.music.load(book.getPath())
		

	def get_status(self):
		return self.playing

	def set_status(self, bool):
		self.playing = bool

	def play(self):
		if not pygame.mixer.music.get_busy():
			self.set_status(True)
			pygame.mixer.music.play()
		else:
			pygame.mixer.music.stop()
			self.set_status(False)

	def pause(self):
		if self.get_status():
			pygame.mixer.music.pause()
			self.set_status(False)
		else:
			pygame.mixer.music.unpause()
			self.set_status(True)

	def stop(self):
		self.set_status(False)
		pygame.mixer.music.stop()

	def played(self):
		return pygame.mixer.music.get_pos()

