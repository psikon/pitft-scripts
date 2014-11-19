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
from utils import pressed

YELLOW = (255, 255, 0)

class Book(pygame.font.Font):
    '''class for storing all relevant facts about an audio book'''

    def __init__(self, path, title, artist, album, playtime, position, cover):
      self.path = path
      self.title = title
      self.artist = artist
      self.album = album
      self.playtime = playtime
      self.position = float(position)
      self.cover = cover

    def getPath(self):
      return self.path

    def getTitle(self):
      return self.title
    
    def getArtist(self):
      return self.artist

    def getAlbum(self):
      return self.getAlbum

    def getPlaytime(self):
      return self.playtime

    def getPosition(self):
      return self.position

    def getCover(self):
      return self.cover

class Library:
    '''generate a library screen for scrolling through the audiobooks'''

    def __init__(self, screen, music_folder, function):
        # define screen variables
        self.screen = screen
        # define music folder
        self.folder = music_folder
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.interface = Interface()
        # declare functions
        self.function = function
        # create library
        self.books = self.create_inventory(self.folder)
        
    '''obsolete in future'''
    def create_inventory(self, music_folder):
      books = []
      # create a list of audio books
      for audio in os.listdir(music_folder):
          # select all files with specific ending
          if audio.endswith(".mp3"):
            # reconstruct path
            path = music_folder + os.sep + audio
            tag = ID3Tag(path)
            book = Book(path, tag.getTitle(), tag.getArtist(), tag.getAlbum(), 
              tag.getPlaytime(), 0, "images/unknown.jpg")
            books.append(book)
      return books

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
          index = len(self.books) -1
        return index
      # scroll to right
      if 210 <= click_pos[0] <= 255 and 190 <= click_pos[1] <= 235:
        index = index + 1
        # set max index to 0 for start new round 
        if index >= len(self.books):
          index = 0
        return index
      # select a book
      if 265 <= click_pos[0] <= 310 and 190 <= click_pos[1] <= 235:
        # select actual book and go to play window
        self.function(self.books[index])
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
            self.books[index].getTitle(), self.books[index].getArtist(),
            self.books[index].getPlaytime(), self.books[index].getCover())
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
 
            
            


 

