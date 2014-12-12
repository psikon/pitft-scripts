'''
utils contain various methods needed for the functionalies of the main program,
that do not fit in some of the classes or need to accessed by various class without
creating a new object or load the complete class object
'''

# import python libraries
import sys, os
import pygame
# needed for save methods
import ConfigParser
from threading import Timer
from id3tag import ID3Tag
from book import Book

def str2time(string):
	''' converts a string into an integer of milliseconds '''
	# split string at ':' into three parts
	x = string.split(':', 3)
	# when resulting x has no hours
	if len(x) < 3: x = ['00'] + x
	# convert to milliseconds
	x = int(x[0])*3600000 + int(x[1])*60000 + int(x[2])*1000
	return x

def time2str(time):
	''' converts milliseconds to a string of format hours:minutes:seconds '''
	# convert to seconds
	s = time/1000
	# convert to minutes 
	m,s = divmod(s, 60)
	# convert to hours
	h,m = divmod(m, 60)
	return '%d:%d:%d' % (h,m,s)

def save_progress(path, chapter, position, cover):
	''' save the progress of an audiobook after stop to a file containing 
	path and actual position at stop '''
	# create new config parser object
	Config = ConfigParser.ConfigParser()
	# open the save file in write mode
	progress = open('cache/progress.txt','w')
	# create section and arguments
	Config.add_section('Progress')
	Config.set('Progress','path', path)
	Config.set('Progress', 'chapter', chapter)
	Config.set('Progress','position', position)
	Config.set('Progress', 'cover', cover)
	# write settings to file
	Config.write(progress)
	# close file
	progress.close()
	
def load_progress():
	''' load the progress of an audiobook from file and return needed informations 
	for creating a new Book object '''
	# load Config Parser
	Config = ConfigParser.ConfigParser()
	# read the cache file
	Config.read('cache/progress.txt')
	# extract path. chapter, position and path to cover
	path = Config.get('Progress','path').translate(None, "'[]").split(', ')
	chapter = Config.get('Progress','chapter')
	position = Config.get('Progress', 'position')
	cover = Config.get('Progress','cover')
	return [path, chapter, position, cover]

def timeout():
	print "game over"

def timer():
	''''''
	t = Timer(1*5,timeout() )
	t.start

def create_library(music_folder):
	'''walk through the music folder, searching for audio books and 
	their chapters and create a library of all audio books'''
	# init empty library
	library = []
	# walk through the music folder
	for root, dirs, files in os.walk(music_folder):
		# init empty chapter list
		chapter = []
		# only add if folder is not empty
		if len(files) > 0:
			# find every file in folder
			for file in files:
				# select only audio files
				if file.endswith('.mp3'):
					# add every audio file to chapter arry
					chapter.append(os.path.join(root, file))
			# sort the chapters by chapter number in file name
			chapter.sort()
			# init total playtime and chapter playtimes
			total_playtime = 0 
			chapter_playtime = []
			# load for every audio file the id3 tags and determine 
			# the total and chapter playtimes
			for item in chapter:
				id3 = ID3Tag(item)
				total_playtime += str2time(id3.get_playtime())
				chapter_playtime.append(id3.get_playtime())
			# add audio book to library
			library.append(Book(chapter, id3.get_title(), id3.get_artist(), 
				id3.get_album(), 0, chapter_playtime, time2str(total_playtime), 
				0, find_cover(root)))	
	return library

def find_cover(path):
	'''search in actual folder for image files for showing cover'''
	# walk throuugh folder
	for file in os.listdir(path):
		# find image file
		if file.endswith(('.png', '.jpg', '.jpeg')):
			return os.path.join(path, file)

def pressed():
	'''get x and y coordinated of a touchscreen press'''
	return (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])