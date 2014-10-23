#!/usr/bin/env python

import sys, os, time
from argparse import ArgumentParser
import pygame
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
# parse cmd arguments
args = parser.parse_args()
# initialize hardware
pitft = hardware(args.pi)

def last_played():
    player = Player(pitft.getScreen(), "Continue")
    player.run()

def information():
	info = InfoScreen()
	sys.exit()


def play_window(string):
	player = Player(pitft.getScreen(), string)
	player.run()

def book_selector():
	# create inventory
	books = dict()
	for picture in os.listdir("./music"):
		if picture.endswith(".jpg"):
			for audio in os.listdir("./music"):
				if audio.endswith('.txt'):
					if os.path.splitext(picture)[0] in os.path.splitext(audio)[0]:
						books.__setitem__(picture,audio)

	bs = BookSelector(pitft.getScreen(), books, play_window)
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
