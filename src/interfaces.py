'''
interface library importing all graphical methods and generate for every screen 
the suitable interface
'''

# python imports
import sys, os, time
import pygame
# internal imports
from graphics import Graphics
from utils import time2str

# define colors
WHITE = (255, 255, 255)
GREY = (64,64,64)
# define path to icon images
BG_IMG = "images/bg_alpha.png"
LIBRARY = "images/library.ico"
BACK = 'images/library.ico'
EXIT = 'images/exit.ico'
LEFT = 'images/left.ico'
RIGHT = 'images/right.ico'
SELECT = 'images/select.ico'
NEXT = 'images/next.ico'
PREVIOUS = 'images/previous.ico'
STOP = 'images/stop.ico'
PAUSE = 'images/pause.ico'
PLAY = 'images/play.ico'

class Interface:

	def __init__(self):
		# init graphic library
		self.graphics = Graphics()

	def main_interface(self, screen, book):
		''' drawing the main interface to screen '''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG), (0, 0))
		# create continue playing field
		self.graphics.clock(screen)
		self.graphics.seperator_line(screen, 120)
		self.graphics.continue_playback(screen, 200, 50, 300, 120, 20, 
			book.get_cover(), book.get_title())
		# add seperator line
		self.graphics.seperator_line(screen)
		# add button for library
		self.graphics.menu_button(screen, "New Book", 10, 190, 48, 48, 
			30, LIBRARY)
		# add exit button
		self.graphics.menu_button(screen, "", 265, 190, 48, 48, 
			30, EXIT)
		return screen

	def list_interface(self, screen, title, artist, playtime, cover):
		''' generate screen for library interface '''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG), (0, 0))
		# load button images
		back = self.graphics.load_image(BACK)
		left = self.graphics.load_image(LEFT)
		right = self.graphics.load_image(RIGHT)
		select = self.graphics.load_image(SELECT)
		# add seperator line
		self.graphics.seperator_line(screen)
		# draw navigation buttons to screen
		self.graphics.image_button(screen, back, 10, 190, 48, 48)
		self.graphics.image_button(screen, left, 155, 190, 48, 48)
		self.graphics.image_button(screen, right, 210, 190, 48, 48)
		self.graphics.image_button(screen, select, 265, 190, 48, 48)
		# update actual audio book informations
		self.graphics.title_field(screen, title, 10, 10, 300)
		self.graphics.artist_field(screen, artist, 10, 45)
		self.graphics.play_time_field(screen, playtime, 10, 100)
		self.graphics.cover_field(screen, cover, 140, 140, 155, 40)  
		return screen

	def player_interface(self, screen, title, artist, actualChapter, totalChapter,
		playtime, music_pos, cover):
		''' generate the interface for the audio player '''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG), (0, 0))
		# load images for buttons
		back = self.graphics.load_image(BACK)
		backward = self.graphics.load_image(PREVIOUS)
		forward = self.graphics.load_image(NEXT)
		pause = self.graphics.load_image(PAUSE)
		play = self.graphics.load_image(PLAY)
		stop = self.graphics.load_image(STOP)
		# add seperator line
		self.graphics.seperator_line(screen)
		# draw navigation buttons to screen a
		self.graphics.image_button(screen, back, 10, 190, 48, 48)
		# draw playback buttons to screen
		self.graphics.image_button(screen, backward, 65, 190, 48, 48)
		self.graphics.image_button(screen, forward, 115, 190, 48, 48)
		self.graphics.image_button(screen, pause, 165, 190, 48, 48)
		self.graphics.image_button(screen, stop, 215, 190, 48, 48)
		self.graphics.image_button(screen, play, 265, 190, 48, 48)
		# update actual audio book informations
		self.graphics.title_field(screen, title, 10, 10, 300)
		self.graphics.artist_field(screen, artist, 10, 45)
		self.graphics.chapter_field(screen, actualChapter, totalChapter, 10, 100)
		self.graphics.cover_field(screen, cover, 80, 80, 220, 40)
		self.graphics.play_bar(screen, playtime, music_pos)
		return screen

	def exit_interface(self, screen):
		''' draw an little exit screen containing an exit message '''
		while True:
			# draw background
			screen.fill(GREY)
			# set a bigger font
			font = pygame.font.Font(None, 45)
			# draw exit message
			label = font.render("Good Bye!", 1, (WHITE))
			screen.blit(label, (85,100))
			# update display
			pygame.display.flip()
			# show message for to seconds and exit program
			time.sleep(2)
			sys.exit(0)
		