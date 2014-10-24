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
from src.startscreen import MainMenu
from src.bookselector import BookSelector
from src.play import Player
from src.info import InfoScreen

# setup argument parser
parser = ArgumentParser(description = '%s -- audiobook interface for raspberry pi' % 
                           (os.path.basename(sys.argv[0])),
                          	epilog = 'created by Philipp Sehnert',
                          	add_help = True)
parser.add_argument('--version', action = 'version', version = '%s 1.0' % 
                     	(os.path.basename(sys.argv[0])))
parser.add_argument('-pi', dest = 'pi', default = False, 
  						action = 'store_true', help = 'choose interface')
parser.add_argument('-m', type = str, dest = 'music', default = "./music", 
  					help = 'destination of music folder')

# parse cmd arguments
args = parser.parse_args()

# initialize hardware
pitft = hardware(args.pi)

# define functions for main menu
def last_played():
	'''wrapper for the player window used by main menu'''
	player = Player(pitft.getScreen(), "Continue")
	player.run()

def information():
	'''wrapper for the system information screen'''
	info = InfoScreen(pitft.getScreen(), args.music)
	info.run()

def play_window(string):
	'''wrapper for player window used by book selector'''
	player = Player(pitft.getScreen(), string)
	player.run()

def book_selector():
	'''wrapper for media library screen'''
	# create inventory
	books = dict()
	# iterate through music folder
	for picture in os.listdir(args.music):
		# select all cover pictures
		if picture.endswith(".jpg"):
			# find corresponding audio books
			# must have the same name like cover
			for audio in os.listdir("./music"):
				if audio.endswith('.txt'):
					# add audio book to list
					if os.path.splitext(picture)[0] in os.path.splitext(audio)[0]:
						books.__setitem__(picture,audio)

	bs = BookSelector(pitft.getScreen(), books, args.music, play_window)
	bs.run()

def main(): 
	# register main menu functions
	funcs = {'Continue': last_played,
			'Select Book': book_selector,
			'Information': information}
	# create main menu object
	main_menu = MainMenu(pitft.getScreen(),
		['Continue','Select Book', 'Information'], funcs, pitft)
	# start main menu
	main_menu.run()

if __name__ == '__main__': 
	sys.exit(main())
