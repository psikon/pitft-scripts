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
		self.font = pygame.font.SysFont('Arial', 20)
		self.graphics = Graphics()

	def getFont(self):
		''' return actual font '''
		return self.font

	def setFont(self, font, font_size):
		''' set new font and size '''
		self.font = pygame.font.SysFont(font, font_size)

	def main_interface(self, screen):
		''' drawing the main interface screen with three menu buttons '''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# create three text buttons
		self.graphics.makeTextButton(screen, "Last Played", 
			50, 20, 220, 55,'Arial', 40)
		self.graphics.makeTextButton(screen, "Select Book", 
			50, 90, 220, 55, 'Arial', 40)
		self.graphics.makeTextButton(screen, "Information", 
			50, 160, 220, 55, 'Arial', 40)
		return screen

	def list_interface(self, screen, title, artist, playtime, cover):
		'''generate screen for library interface'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# load button images
		back = self.graphics.loadImage(BACK)
		left = self.graphics.loadImage(LEFT)
		right = self.graphics.loadImage(RIGHT)
		select = self.graphics.loadImage(SELECT)
		# draw buttons to screen
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		self.graphics.makeImagebutton(screen, left, 155, 190, 45, 45)
		self.graphics.makeImagebutton(screen, right, 210, 190, 45, 45)
		self.graphics.makeImagebutton(screen, select, 265, 190, 45, 45)
		# update actual audio book informations
		self.graphics.Title(screen, title)
		self.graphics.Artist(screen, artist)
		self.graphics.PlayTime(screen, playtime)
		self.graphics.Cover(screen, cover, 150, 150, 155, 40)  
		return screen

	def player_interface(self, screen, title, artist, actualChapter, totalChapter,
		playtime, music_pos, cover):
		'''generate the interface for the audio player'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# load images for buttons
		back = self.graphics.loadImage(BACK)
		backward = self.graphics.loadImage(PREVIOUS)
		forward = self.graphics.loadImage(NEXT)
		pause = self.graphics.loadImage(PAUSE)
		play = self.graphics.loadImage(PLAY)
		stop = self.graphics.loadImage(STOP)
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

	def info_interface(self, screen, cpu, ram, hdd, ip):
		'''generate the system information screen interface'''
		# draw background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# draw title
		self.setFont('Arial', 30)
		screen.blit(self.font.render('System Information', True, WHITE), (10, 10))
		self.setFont('Arial', 14)
		# load and draw button interface
		back = self.graphics.loadImage(BACK)
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		exit = self.graphics.loadImage(EXIT)
		screen.blit(self.font.render('close gui', True, WHITE), (260, 170))
		self.graphics.makeImagebutton(screen, exit, 265, 190, 45, 45)
		self.setFont('Arial', 20)
		# draw system information fields
		self.graphics.cpuField(screen, cpu)
		self.graphics.RAMField(screen, ram)
		self.graphics.spaceField(screen, hdd) 
		self.graphics.ipField(screen, ip)
		self.graphics.authorField(screen)
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