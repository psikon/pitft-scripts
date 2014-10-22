#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# imports
import sys, os
import pygame
from graphics import Graphics



WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class AudioBook(pygame.font.Font):
    
    def __init__(self, name, played, duration, cover):
      self.name = name
      self.played = played
      self.duration = duration
      self.cover = cover

    def getName(self):
      return self.name
    
    def getPlaytime(self):
      return self.played

    def getDuration(self):
      return self.duration

    def getCover(self):
      return self.cover


class Player:

    def __init__(self, screen, string):
      self.screen = screen
      self.clock = pygame.time.Clock()
      self.graphics = Graphics()
      print string

    def __del__(self):
      pass
        
 
    def interface(self):
      # create background
      self.screen.fill((64,64,64))
      self.screen.blit(self.graphics.loadImage("images/bg_alpha.png"),(0,0))
      # create interface
      back = self.graphics.loadImage('images/previous.png')
      pause = self.graphics.loadImage('images/pause.png')
      play = self.graphics.loadImage('images/play.png')
      self.screen.blit(pygame.transform.scale(back, (30,30)), (10,200))
      self.screen.blit(pygame.transform.scale(pause, (30,30)), (45,200))
      self.screen.blit(pygame.transform.scale(play, (30,30)), (80,200))

    def TitleField(self, name):
      self.screen.blit(self.font.render(name, True, WHITE), (10, 10))

    def CoverField(self, image):
      cover = self.graphics.loadImage('music/'+ image)
      self.screen.blit(pygame.transform.scale(cover, (150,150)), (155,40))

    def PlayedField(self, playtime):
      self.screen.blit(self.font.render('Played:', True, WHITE), (10, 45))
      self.screen.blit(self.font.render(str(playtime) + "min",
        True, WHITE), (10, 70))

    def DurationField(self, duration):
      self.screen.blit(self.font.render('Duration:', True, WHITE), (10, 100))
      self.screen.blit(self.font.render(str(duration) + "min",
        True, WHITE), (10, 125))

    def run(self):
        mainloop = True
        index = 0
        while mainloop:
            # Limit frame speed to 30 FPS
            self.clock.tick(30)
            self.interface()
            pygame.display.flip()
 
            
            


 

