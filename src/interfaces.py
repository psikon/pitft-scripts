#!/usr/bin/env python

'''
graphic library containing all functions needed for drawing interface 
to screen
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# python imports
import sys, os, time
import pygame
from graphics import Graphics

# define colors
WHITE = (255, 255, 255)
GREY = (64,64,64)
# define path to images
BG_IMG = "images/bg_alpha.png"
PREVIOUS = 'images/previous.png'
NEXT = 'images/next.png'
SELECT = 'images/select.png'
PAUSE = 'images/pause.png'
PLAY = 'images/play.png'

class Interface:

	def __init__(self):
		self.font = pygame.font.SysFont('Arial', 20)
		self.graphics = Graphics()

	def getFont(self):
		return self.font

	def setFont(self, font, font_size):
		self.font = pygame.font.SysFont(font, font_size)

	def list_interface(self, screen, title, artist, playtime, cover):
		'''generate screen for book selector interface'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# load button images
		left = self.graphics.loadImage(PREVIOUS)
		right = self.graphics.loadImage(NEXT)
		select = self.graphics.loadImage(SELECT)
		# draw buttons to screen
		self.graphics.makeImagebutton(screen, left, 10, 190, 45, 45)
		self.graphics.makeImagebutton(screen, right, 65, 190, 45, 45)
		self.graphics.makeImagebutton(screen, select, 120, 190, 45, 45)
		# update actual audio book informations
		self.graphics.Title(screen, title)
		self.graphics.Artist(screen, artist)
		self.graphics.PlayTime(screen, playtime)
		self.graphics.Cover(screen, cover, 150, 150, 155, 40)  
		return screen

	def player_interface(self, screen, title, artist, playtime, music_pos, cover):
		'''generate the interface for the audio player'''
		# create background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# load images for buttons
		back = self.graphics.loadImage(PREVIOUS)
		pause = self.graphics.loadImage(PAUSE)
		play = self.graphics.loadImage(PLAY)
		# draw buttons to screen
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		self.graphics.makeImagebutton(screen, pause, 65, 190, 45, 45)
		self.graphics.makeImagebutton(screen, play, 120, 190, 45, 45)
		self.graphics.Title(screen, title)
		self.graphics.Artist(screen, artist)
		self.graphics.Cover(screen, cover, 80, 80, 220, 40)
		self.graphics.PlayBar(screen, playtime, music_pos)
		return screen

	def info_interface(self, screen, cpu, ram, hdd, ip):
		'''generate the information screen interface'''
		# draw background
		screen.fill(GREY)
		screen.blit(self.graphics.loadImage(BG_IMG),(0,0))
		# draw title
		self.setFont('Arial', 30)
		screen.blit(self.font.render('System Information', True, WHITE), (10, 10))
		self.setFont('Arial', 14)
		# load and draw button interface
		back = self.graphics.loadImage(PREVIOUS)
		self.graphics.makeImagebutton(screen, back, 10, 190, 45, 45)
		exit = self.graphics.loadImage(SELECT)
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
		screen.fill(GREY)
		font = pygame.font.Font(None, 45)
		label = font.render("Good Bye!", 1, (WHITE))
		screen.blit(label, (85,100))
		return screen