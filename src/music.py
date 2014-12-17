'''
music class contains all needed functions for control the music of the pygame
module including the functionalities for the play bar
'''

# python imports
import sys, os
import pygame

# internal imports
from interfaces import Interface
from utils import save_progress, str2time, timer

# action when a played song finish
NEXT_CHAPTER = pygame.USEREVENT

class Player:

	def __init__(self, book):
		# init the mixer of pygame module
		self.mixer = pygame.mixer
		self.mixer.init()
		# init the interface module
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
		''' start playing '''
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
		# save to cache file
		save_progress(self.book.get_path(), self.get_chapter(), 
			pygame.mixer.music.get_pos(), self.book.get_cover())
		# stop the music
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
		''' get actual played chapter '''
		return self.chapter

	def previous_chapter(self):
		''' select previous chapter '''
		if not self.chapter == 0: 
			self.chapter -= 1
			self.position = 0
			self.play()
		else:
			self.stop()
		
	def next_chapter(self):
		''' select next chapter '''
		if not self.chapter == len(self.book.get_path()) - 1: 
			self.chapter += 1
			self.position = 0
			self.play()
		else:
			self.stop()

	def play_next_chapter(self):
		''' play the next chapter in path array at the selected position'''
		self.mixer.music.load(self.book.get_path()[self.get_chapter()])
		self.mixer.music.play(1, self.position)