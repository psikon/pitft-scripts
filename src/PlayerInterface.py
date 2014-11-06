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
from player import Player



WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


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


class PlayerInterface:

    def __init__(self, screen, book):
      self.screen = screen
      self.clock = pygame.time.Clock()
      self.graphics = Graphics()
      self.book = book
      self.music = Player(self.book)
      

    def __del__(self):
      pass

    def on_key(self, event, index):
      # scroll to left
        if event.key == pygame.K_LEFT:
          index -=1
          # make negative index to max index to start new round
          if index == -1:
            index = len(self.books) -1
        # scroll to right
        if event.key == pygame.K_RIGHT:
          index = index + 1
          # set max index to 0 for start new round 
          if index >= len(self.books):
            index = 0
        # select item
        if event.key == pygame.K_RETURN:
          self.function(self.books[index])
        return(index)

    def on_click(self):
      click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
      #now check to see if button 1 was pressed
      if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
        self.music.stop()
        return False
      #now check to see if button 2 was pressed        
      if 65 <= click_pos[0] <= 110 and 190 <= click_pos[1] <= 235:
        self.music.pause()
      #now check to see if button 3 was pressed
      if 120 <= click_pos[0] <= 160 and 190 <= click_pos[1] <= 235:
        self.music.play()
      return True

    def run(self):
      mainloop = True
      while mainloop:
        # Limit frame speed to 30 FPS
        self.clock.tick(30)
        self.graphics.player_interface(self.screen)
        #self.graphics.TitleField(self.screen, self.music.getTitle())
        #self.graphics.ArtistField()
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
              mainloop = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
            mainloop = self.on_click()
        pygame.display.flip()

 
            
            


 

