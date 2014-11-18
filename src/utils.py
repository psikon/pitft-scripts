#!/usr/bin/env python

'''
Description
'''

# import python libraries
import sys, os
import pygame
import ConfigParser
from id3tag import ID3Tag

def str2time(string):
	x = string.split(':', 3)
	if len(x) < 3: x = ['00'] + x
	x = int(x[0])*3600000 + int(x[1])*60000 + int(x[2])*1000
	return x

def time2str(time):
	s = time/1000
	m,s = divmod(s, 60)
	h,m = divmod(m, 60)
	return '%d:%d:%d' % (h,m,s)

def save_progress(path, position):
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
	Config = ConfigParser.ConfigParser()
	Config.read('cache/progress.txt')
	path = Config.get('Progress','path')
	position = Config.get('Progress', 'position')
	return [path, position]

def timer():
	pass