#!/usr/bin/env python

# imports
import sys, os
import pygame
from graphics import Graphics

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Book(pygame.font.Font):
    
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

    def __init__(self, screen, books, function, font = None, font_size = 45,
                 font_color = BLACK):
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.graphics = Graphics()
        self.function = function
        self.books = []
        for picture, audio in books.items():
          book = Book(audio, "2:36","10:54", picture)
          self.books.append(book)
        
        self.cur_book = None
 
    def interface(self):
      # create background
      self.screen.fill((64,64,64))
      self.screen.blit(self.graphics.loadImage("images/bg_alpha.png"),(0,0))
      # create interface
      left = self.graphics.loadImage('images/previous.png')
      right = self.graphics.loadImage('images/next.png')
      select = self.graphics.loadImage('images/select.png')
      self.screen.blit(pygame.transform.scale(left, (30,30)), (10,200))
      self.screen.blit(pygame.transform.scale(right, (30,30)), (45,200))
      self.screen.blit(pygame.transform.scale(select, (30,30)), (80,200))

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
            for event in pygame.event.get():
              self.interface()
              if event.type == pygame.QUIT:
                  mainloop = False
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                  index -=1
                  if index == -1:
                    index = 0
                if event.key == pygame.K_RIGHT:
                  index = index + 1
                  if index >= len(self.books):
                    index = len(self.books) - 1 
                if event.key == pygame.K_RETURN:
                  self.function(self.books[index].getName())
              self.TitleField(self.books[index].getName())
              self.PlayedField(self.books[index].getPlaytime())
              self.DurationField(self.books[index].getDuration())
              self.CoverField(self.books[index].getCover())  
            pygame.display.flip()
 
            
            


 

