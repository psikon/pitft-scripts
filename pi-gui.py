#!/usr/bin/env python
'''pi-gui is a little GUI based audio player specialised for audio books. The program 
is optimized for the pitft expansion board to fit inside the pitft resolution. It is 
capable to play audio books in defined formats, show some facts about them like the cover
image, scroll through a list of audiobooks and show some system informations about the 
system. Using pygame library makes the program independent from an running x server.'''

# python libraries
import sys, os, time
from argparse import ArgumentParser
import pygame
# pi-gui libraries
from src.hardware import hardware
from src.mainscreen import MainMenu
from src.library import Library, Book
from src.player import PlayerInterface
from src.systeminfo import InfoScreen
from src.id3tag import ID3Tag
from src.utils import load_progress, create_library, str2time

# setup argument parser
parser = ArgumentParser(description = '%s -- audiobook interface for raspberry pi' % 
                           (os.path.basename(sys.argv[0])),
                          	epilog = 'created by Philipp Sehnert',
                          	add_help = True)
# version output
parser.add_argument('--version', action = 'version', version = '%s 1.0' % 
                     	(os.path.basename(sys.argv[0])))
# select output to x or pitft
parser.add_argument('-pi', dest = 'pi', default = False, 
  						action = 'store_true', help = 'choose interface')
# select music folder
parser.add_argument('-m', type = str, dest = 'music', default = "./music", 
  					help = 'destination of music folder')

# parse cmd arguments
args = parser.parse_args()

# initialize hardware
pitft = hardware(args.pi)

# define functions for main menu
def last_played(book):
	'''load the last played song from cache file and go to player 
	window to resume '''
	# load cache file
	player = PlayerInterface(pitft.get_screen(), book)
	player.run()

def play_window(string):
	'''load the last played song from cache file and go to player 
	window to resume '''
	# load cache file
	player = PlayerInterface(pitft.get_screen(), string)
	player.run()
	
def book_selector():
	'''wrapper for media library screen'''
	bs = Library(pitft.get_screen(), 
		create_library(os.path.abspath(args.music)), 
		play_window)
	bs.run()

def load_cache():
	progress = load_progress()
	chapter_playtime = []
	total_playtime = 0
	for item in progress[0]:
		id3 = ID3Tag(item)
		total_playtime += str2time(id3.get_playtime())
		chapter_playtime.append(id3.get_playtime())
	# create id3tag object
	id3 = ID3Tag(progress[0][0])
	# create book object with id3 tags and actual position
	book = Book(progress[0], id3.get_title(), id3.get_artist(), id3.get_album(),
	 int(progress[1]), chapter_playtime, total_playtime, int(progress[2])/1000, 
	 progress[3])
	return book

def main(): 
	# register main menu functions
	funcs = {'Continue': last_played,
			'Select Book': book_selector}
	# create main menu object
	main_menu = MainMenu(pitft.get_screen(), funcs, pitft, load_cache())
	# start main menu
	main_menu.run()

if __name__ == '__main__': 
	sys.exit(main())
