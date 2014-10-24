#!/usr/bin/env python
'''book_selector creates a screen for selecting the ebooks from a list by showing 
the name, cover and supplemental informations on the screen. The books are scrollable 
with the cursor or pitft buttons'''

# python imports
import sys, os
import pygame
# pi-gui imports
from graphics import Graphics

class Book(pygame.font.Font):
    ''' class for storing general informations of one audio book item'''

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

class BookSelector:
    '''generates the scrollable list screen'''
    def __init__(self, screen, books, music_folder, function):
        # define general variables
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.folder = music_folder
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods6
        self.graphics = Graphics()
        # declare functions
        self.function = function
        # init empty audio book list
        self.books = []
        # create a list of audio books
        for picture, audio in books.items():
          book = Book(audio, "2:36","10:54", picture)
          self.books.append(book)

    def run(self):
      '''run method for drawing the screen to dispay'''
      mainloop = True
      # set index of list to first item
      index = 0
      # use infinity loop for drawing screen
      while mainloop:
        # Limit frame speed to 30 FPS
        self.clock.tick(30)
        # update display when button is pressed
        for event in pygame.event.get():
          self.graphics.list_interface(self.screen)
          # end program by quit signal
          if event.type == pygame.QUIT:
            mainloop = False
          if event.type == pygame.KEYDOWN:
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
              self.function(self.books[index].getName())
            if event.key == pygame.K_BACKSPACE:
              mainloop = False
          # update actual audio book informations
          self.graphics.TitleField(self.screen, self.books[index].getName())
          self.graphics.PlayedField(self.screen, self.books[index].getPlaytime())
          self.graphics.DurationField(self.screen, self.books[index].getDuration())
          self.graphics.CoverField(self.screen, self.books[index].getCover(), self.folder)  
        # update display
        pygame.display.flip()
 
            
            


 

