'''
interface library importing all graphic methods and providing functions
for the generation of every interface screen
'''

# python imports
import sys, os, time
import pygame
from graphics import Graphics

# define colors
WHITE = (255, 255, 255)
GREY = (64,64,64)
# define path to images
BG_IMG = "images/bg_alpha.png"
BACK = 'images/back.png'
EXIT = 'images/exit.png'
LEFT = 'images/left.png'
RIGHT = 'images/right.png'
SELECT = 'images/select.png'
NEXT = 'images/next.png'
PREVIOUS = 'images/previous.png'
STOP = 'images/stop.png'
PAUSE = 'images/pause.png'
PLAY = 'images/play.png'

class Interface:

	def __init__(self):
		self.graphics = Graphics()


	def main_interface(self, screen):
		''' drawing the main interface screen with three menu buttons '''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG),(0,0))
		# create three text buttons
		self.graphics.makeTextButton(screen, "Last Played", 
			50, 20, 220, 55, 40)
		self.graphics.makeTextButton(screen, "Select Book", 
			50, 90, 220, 55, 40)
		return screen

	def list_interface(self, screen, title, artist, playtime, cover):
		'''generate screen for library interface'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG),(0,0))
		# load button images
		back = self.graphics.load_image(BACK)
		left = self.graphics.load_image(LEFT)
		right = self.graphics.load_image(RIGHT)
		select = self.graphics.load_image(SELECT)
		# draw buttons to screen
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		self.graphics.makeImagebutton(screen, left, 155, 190, 45, 45)
		self.graphics.makeImagebutton(screen, right, 210, 190, 45, 45)
		self.graphics.makeImagebutton(screen, select, 265, 190, 45, 45)
		# update actual audio book informations
		self.graphics.Title(screen, title)
		self.graphics.Artist(screen, artist)
		self.graphics.PlayTime(screen, playtime)
		self.graphics.Cover(screen, cover, 140, 140, 155, 40)  
		return screen

	def player_interface(self, screen, title, artist, actualChapter, totalChapter,
		playtime, music_pos, cover):
		'''generate the interface for the audio player'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.load_image(BG_IMG),(0,0))
		# load images for buttons
		back = self.graphics.load_image(BACK)
		backward = self.graphics.load_image(PREVIOUS)
		forward = self.graphics.load_image(NEXT)
		pause = self.graphics.load_image(PAUSE)
		play = self.graphics.load_image(PLAY)
		stop = self.graphics.load_image(STOP)
		# draw buttons to screen
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		self.graphics.makeImagebutton(screen, backward, 65, 190, 45, 45)
		self.graphics.makeImagebutton(screen, forward, 115, 190, 45, 45)
		self.graphics.makeImagebutton(screen, pause, 165, 190, 45, 45)
		self.graphics.makeImagebutton(screen, stop, 215, 190, 45, 45)
		self.graphics.makeImagebutton(screen, play, 265, 190, 45, 45)
		# update actual audio book informations
		self.graphics.Title(screen, title)
		self.graphics.Artist(screen, artist)
		self.graphics.Chapter(screen, actualChapter, totalChapter)
		self.graphics.Cover(screen, cover, 80, 80, 220, 40)
		self.graphics.PlayBar(screen, playtime, music_pos)
		return screen

	def exit_interface(self, screen):
		''' draw an little exit screen with a little message '''
		# draw background
		screen.fill(GREY)
		# set a bigger font
		font = pygame.font.Font(None, 45)
		# draw exit message
		label = font.render("Good Bye!", 1, (WHITE))
		screen.blit(label, (85,100))
		return screen