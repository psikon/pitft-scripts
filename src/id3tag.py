''' load id3 tags from mp3 files and return the informations'''

# python imports
import sys, os
import pygame
import eyeD3

class ID3Tag:

	def  __init__(self, path):
		# load id3 tags from file
		try:
			self.id3 = eyeD3.Mp3AudioFile(path)
		except IOerror:
			print "Library is empty"

	def get_title(self):
		''' access title slot '''
		try:
			return self.id3.tag.getTitle()
		except: 
			return "No item in library"

	def get_album(self):
		''' access album slot '''
		try:
			return self.id3.tag.getAlbum()
		except:
			return "No item in library"

	def get_artist(self):
		''' access artist slot '''
		try:
			return self.id3.tag.getArtist()
		except:
			return "No item in library"

	def get_playtime(self):
		''' access playtime slot '''
		try:
			return self.id3.getPlayTimeString()
		except: 
			print "No item in library"

	def get_year(self):
		''' access year slot '''
		try:
			return self.id3.getYear()
		except:
			return "No item in library"