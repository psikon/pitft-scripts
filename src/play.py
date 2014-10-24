#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# import python libraries
import sys, os
import pygame
# import pi-gui libraries
from graphics import Graphics



WHITE = (255, 255, 255)


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
      self.book = string
      

    def __del__(self):
      pass

    def run(self):
      mainloop = True
      while mainloop:
        # Limit frame speed to 30 FPS
        self.clock.tick(30)
        self.graphics.player_interface(self.screen)
        self.graphics.TitleField(self.screen, self.book)
        #self.graphics.make_button(self.screen, 'zuruek', 'images/previous.png', 20, 20, (255,255,255))
        for event in pygame.event.get():
          
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
              mainloop = False
        pygame.display.flip()

 
            
            


 

