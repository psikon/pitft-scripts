#!/usr/bin/env python
'''bibliothek creates a screen for selecting the ebooks from a list by showing 
the name, cover and supplemental informations on the screen. The books are scrollable 
with the cursor or pitft touchscreen'''

# python imports
import sys, os
import pygame
import eyeD3
# pi-gui imports
from interfaces import Interface
from id3tag import ID3Tag
from book import Book
from utils import pressed

YELLOW = (255, 255, 0)

class Library:
    '''generate a library screen for scrolling through the audiobooks'''

    def __init__(self, screen, library, function):
        # define screen variables
        self.screen = screen
        # define music folder
        self.library = library
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.interface = Interface()
        # declare functions
        self.function = function

    def on_click(self, index):
      '''recognize touchscreen and mouse selections to 
      run functionalities of buttons'''
      # get actual position of mouse click 
      click_pos = pressed()
      # go back to main screen
      if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
        return 999
      # scroll to left
      if 155 <= click_pos[0] <= 200 and 190 <= click_pos[1] <= 235:
        index -=1
        # make negative index to max index to start new round
        if index == -1:
          index = len(self.library) -1
        return index
      # scroll to right
      if 210 <= click_pos[0] <= 255 and 190 <= click_pos[1] <= 235:
        index = index + 1
        # set max index to 0 for start new round 
        if index >= len(self.library):
          index = 0
        return index
      # select a book
      if 265 <= click_pos[0] <= 310 and 190 <= click_pos[1] <= 235:
        # select actual book and go to play window
        self.function(self.library[index])
      return index

    def run(self):
      '''run method for drawing the screen to dispay'''
      mainloop = True
      # set index of list to first item
      index = 0
      # use infinity loop for drawing screen
      while mainloop:
        # Limit frame speed to 30 FPS
        self.clock.tick(30)
        for event in pygame.event.get():
          # draw interface on screen
          self.interface.list_interface(self.screen, 
            self.library[index].get_title(), self.library[index].get_artist(),
            self.library[index].get_total_playtime(), self.library[index].get_cover())
          # wit for touchscreen event
          if event.type == pygame.MOUSEBUTTONDOWN:
            # draw circle for touchscreen feedback
            pygame.draw.circle(self.screen, YELLOW, pressed(), 10, 0)
            # update index in library
            index = self.on_click(index)
            # exit mainloop
            if index == 999: mainloop = False
            
        # update display
        pygame.display.flip()
 
            
            


 

