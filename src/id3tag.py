'''id3tag load from mp3 files the tag informations and 
save them in a class structure'''

# python imports
import sys, os
import pygame
import eyeD3

class ID3Tag:

	def  __init__(self, path):
		# load id3 tags from file
		self.id3 = eyeD3.Mp3AudioFile(path)


	def get_title(self):
		return self.id3.tag.getTitle()

	def get_album(self):
		return self.id3.tag.getAlbum()

	def get_artist(self):
		return self.id3.tag.getArtist()

	def get_playtime(self):
		return self.id3.getPlayTimeString()

	def get_year(self):
		return self.id3.getYear()