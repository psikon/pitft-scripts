#!/usr/bin/env python
'''booklist-interface creates a screen for selecting the ebooks from a list by showing 
the name, cover and supplemental informations on the screen. The books are scrollable 
with the cursor or pitft buttons'''

# python imports
import sys, os
import pygame
import eyeD3
# pi-gui imports
from interfaces import Interface
from id3tag import ID3Tag

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Book(pygame.font.Font):
    ''' class for storing general informations of one audio book item'''

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

class BookSelector:
    '''generates the scrollable list screen'''

    def __init__(self, screen, music_folder, function):
        # define general variables
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.folder = music_folder
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.interface = Interface()
        # declare functions
        self.function = function
        self.books = self.create_inventory(self.folder)
        

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
          print self.books[index]
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
        # update display when button is pressed
        for event in pygame.event.get():
          # draw interface on screen
          self.interface.list_interface(self.screen, 
            self.books[index].getTitle(), self.books[index].getArtist(),
            self.books[index].getPlaytime(), self.books[index].getCover())
          click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

          if event.type == pygame.KEYDOWN:
            index = self.on_key(event, index)
            if event.key == pygame.K_BACKSPACE:
              mainloop = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
            index = self.on_click(index)
        # update display
        pygame.display.flip()
 
            
            


 

