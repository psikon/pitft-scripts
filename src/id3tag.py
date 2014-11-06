#!/usr/bin/env python
''''''

# python imports
import sys, os
import pygame
import eyeD3

class ID3Tag:

	def  __init__(self, path):
		self.id3 = eyeD3.Mp3AudioFile(path)


	def getTitle(self):
		return self.id3.tag.getTitle()

	def getAlbum(self):
		return self.id3.tag.getAlbum()

	def getArtist(self):
		return self.id3.tag.getArtist()

	def getPlaytime(self):
		return self.id3.getPlayTimeString()

	def getYear(self):
		return self.id3.getYear()