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
		self.mixer = pygame.mixer
		self.mixer.init()
		self.interface = Interface()
		# load actual audio book object
		self.book = book
		self.chapter = 0
		# set position to position in audio book class
		self.position = self.book.getPosition()
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
		self.mixer.music.load(self.book.getPath()[self.chapter])
		self.mixer.music.play(0, self.position)
		for num, song in enumerate(self.book.getPath()):
			if num == song:
				continue # already playing
			pygame.mixer.music.queue(song)
		
	def set_chapter(self, pos):
		print pos
		print str2time(self.book.getChapterPlaytime()[self.chapter])
		print self.chapter
		if pos == str2time(self.book.getChapterPlaytime()[self.chapter]):
			self.chapter +=1

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
		if pygame.mixer.music.get_busy():
			return (self.position * 1000) + pygame.mixer.music.get_pos()
		else:
			return 0

	def set_pos(self, pos):
		''' restart playing depending on selected position on playbar '''
		factor = str2time(self.book.getChapterPlaytime()[self.chapter])/300
		self.position = (pos-10)*factor/1000
		self.play()

	def get_chapter(self):
		return self.chapter
		

