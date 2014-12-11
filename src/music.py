'''
music class contains all needed functions for control the music of the pygame
module including the functionalities for the play bar
'''

# python imports
import sys, os
import pygame

# pi-gui imports
from interfaces import Interface
from utils import save_progress, str2time, timer

NEXT_CHAPTER = pygame.USEREVENT

class Player:


	def __init__(self, book):
		# init the mixer of pygame module
		self.mixer = pygame.mixer
		self.mixer.init()
		self.interface = Interface()
		# load actual audio book object
		self.book = book
		self.chapter = self.book.get_chapter()
		# set position to position in audio book class
		self.position = self.book.get_pos()
		# set playing status
		self.playing = False
		
	def get_status(self):
		''' get mixer status '''
		return self.playing

	def set_status(self, bool):
		''' set new mixer status '''
		self.playing = bool

	def play(self):
		''' play or stop the music depending on play status '''
		pygame.mixer.music.set_endevent(pygame.USEREVENT)
		self.play_next_chapter()

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
		save_progress(self.book.get_path(), self.get_chapter(), 
			pygame.mixer.music.get_pos(), self.book.get_cover())
		pygame.mixer.music.stop()

	def get_pos(self):
		''' get actual position of audio book '''
		if pygame.mixer.music.get_busy():
			return (self.position * 1000) + pygame.mixer.music.get_pos()
		else:
			return 0

	def set_pos(self, pos):
		''' restart playing depending on selected position on playbar '''
		factor = str2time(self.book.get_chapter_playtime()[self.get_chapter()])/300
		self.position = (pos-10)*factor/1000
		self.play_next_chapter()

	def get_chapter(self):
		return self.chapter

	def previous_chapter(self):
		if not self.chapter == 0: 
			self.chapter -= 1
			self.position = 0
			self.play()
		else:
			self.stop()
		
	def next_chapter(self):
		if not self.chapter == len(self.book.get_path()) - 1: 
			self.chapter += 1
			self.position = 0
			self.play()
		else:
			self.stop()

	def play_next_chapter(self):
		self.mixer.music.load(self.book.get_path()[self.get_chapter()])
		self.mixer.music.play(1, self.position)