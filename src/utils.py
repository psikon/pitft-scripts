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
	# extract path and position
	path = Config.get('Progress','path').translate(None, "'[]").split(', ')
	chapter = Config.get('Progress','chapter')
	position = Config.get('Progress', 'position')
	cover = Config.get('Progress','cover')
	return [path, chapter, position, cover]

def timer():
	''''''
	pass

def create_library(music_folder):
	''''''
	library = []
	for root, dirs, files in os.walk(music_folder):
		chapter = []
		for file in files:
			if file.endswith('.mp3'):
				chapter.append(os.path.join(root, file))
		chapter.sort()
		totalPlaytime = 0 
		chapterPlaytime = []
		for item in chapter:
			id3 = ID3Tag(item)
			totalPlaytime += str2time(id3.getPlaytime())
			chapterPlaytime.append(id3.getPlaytime())
		library.append(Book(chapter, id3.getTitle(), id3.getArtist(), id3.getAlbum(), 
			0, chapterPlaytime, time2str(totalPlaytime), 0, find_cover(root)))	
	return library

def find_cover(path):
	for file in os.listdir(path):
		if file.endswith(('.png', '.jpg', '.jpeg')):
			return os.path.join(path, file)

def pressed():
	'''get x and y coordinated of a touchscreen press'''
	return (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])