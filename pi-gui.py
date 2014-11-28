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
def last_played():
	'''load the last played song from cache file and go to player 
	window to resume '''
	# load cache file
	progress = load_progress()
	chapterPlaytime = []
	totalPlaytime = 0
	for item in progress[0]:
		id3 = ID3Tag(item)
		totalPlaytime += str2time(id3.getPlaytime())
		chapterPlaytime.append(id3.getPlaytime())
	# create id3tag object
	id3 = ID3Tag(progress[0][0])
	# create book object with id3 tags and actual position
	book = Book(progress[0], id3.getTitle(), id3.getArtist(), id3.getAlbum(),
	 int(progress[1]), chapterPlaytime, totalPlaytime, int(progress[2])/1000, progress[3])
	player = PlayerInterface(pitft.getScreen(), book)
	player.run()

def information():
	'''wrapper for the system information screen'''
	info = InfoScreen(pitft.getScreen(), args.music)
	info.run()

def play_window(string):
	'''wrapper for player window used by library'''
	player = PlayerInterface(pitft.getScreen(), string)
	player.run()

def book_selector():
	'''wrapper for media library screen'''
	bs = Library(pitft.getScreen(), 
		create_library(os.path.abspath(args.music)), 
		play_window)
	bs.run()

def main(): 
	# register main menu functions
	funcs = {'Continue': last_played,
			'Select Book': book_selector,
			'Information': information}
	# create main menu object
	main_menu = MainMenu(pitft.getScreen(), funcs, pitft)
	# start main menu
	main_menu.run()

if __name__ == '__main__': 
	sys.exit(main())
