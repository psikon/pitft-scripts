#!/usr/bin/env python
''''''

# python imports
import sys, os
import pygame

# pi-gui imports
from graphics import Graphics
from utils import save_progress

class Player:

	def __init__(self, book):
		pygame.mixer.init()
		self.book = book
		pygame.mixer.music.load(book.getPath())
		self.playing = pygame.mixer.music.get_busy()
		

	def get_status(self):
		return self.playing

	def set_status(self, bool):
		self.playing = bool

	def play(self):
		if not pygame.mixer.music.get_busy():
			self.set_status(True)
			print self.book.getPosition()
			pygame.mixer.music.play(-1, self.book.getPosition())
		else:
			self.stop()

	def pause(self):
		if self.get_status():
			pygame.mixer.music.pause()
			self.set_status(False)
		else:
			pygame.mixer.music.unpause()
			self.set_status(True)

	def stop(self):
		self.set_status(False)
		save_progress(self.book.getPath(), pygame.mixer.music.get_pos())
		pygame.mixer.music.stop()


	def get_pos(self):
		return pygame.mixer.music.get_pos()

