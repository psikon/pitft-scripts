#!/usr/bin/env python
'''book_selector creates a screen for selecting the ebooks from a list by showing 
the name, cover and supplemental informations on the screen. The books are scrollable 
with the cursor or pitft buttons'''

# python imports
import sys, os
import pygame
import eyeD3
# pi-gui imports
from graphics import Graphics

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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
        for audio in books:
          trackInfo = eyeD3.Mp3AudioFile(music_folder + os.sep + audio)
          tag = trackInfo.getTag()
          tag.link(music_folder + os.sep + audio)
          book = Book(tag.getTitle(), "2:36",trackInfo.getPlayTimeString(), "../images/unknown.jpg")
          self.books.append(book)

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
          self.function(self.books[index].getName())
        return(index)

    def on_click(self, index):
        click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
        #now check to see if button 1 was pressed
        if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
          index -=1
          # make negative index to max index to start new round
          if index == -1:
            index = len(self.books) -1
          return index
        #now check to see if button 2 was pressed
        if 65 <= click_pos[0] <= 110 and 190 <= click_pos[1] <= 235:
          index = index + 1
          # set max index to 0 for start new round 
          if index >= len(self.books):
            index = 0
          return index
        #now check to see if button 3 was pressed
        if 120 <= click_pos[0] <= 160 and 190 <= click_pos[1] <= 235:
          self.function(self.books[index].getName())
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
        # update display when button is pressed
        for event in pygame.event.get():
          self.graphics.list_interface(self.screen)
          click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
          # end program by quit signal
          if event.type == pygame.KEYDOWN:
            index = self.on_key(event, index)
            if event.key == pygame.K_BACKSPACE:
              mainloop = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
            index = self.on_click(index)
          # update actual audio book informations
          self.graphics.TitleField(self.screen, self.books[index].getName())
          self.graphics.PlayedField(self.screen, self.books[index].getPlaytime())
          self.graphics.DurationField(self.screen, self.books[index].getDuration())
          self.graphics.CoverField(self.screen, self.books[index].getCover(), self.folder)  
        # update display
        pygame.display.flip()
 
            
            


 

