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

def save_progress(path, position):
	''' save the progress of an audiobook after stop to a file containing 
	path and actual position at stop '''
	# create new config parser object
	Config = ConfigParser.ConfigParser()
	# open the save file in write mode
	progress = open('cache/progress.txt','w')
	# create section and arguments
	Config.add_section('Progress')
	Config.set('Progress','path',path)
	Config.set('Progress','position', position)
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
	path = Config.get('Progress','path')
	position = Config.get('Progress', 'position')
	return [path, position]

def timer():
	''''''
	pass

def create_library():
	''''''
	pass

def find_cover():
	''''''
	pass

def pressed():
	'''get x and y coordinated of a touchscreen press'''
	return (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])