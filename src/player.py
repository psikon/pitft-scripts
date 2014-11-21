'''
player created a screen containing various informations about the selected 
audio book and show the player interface on screen.
'''

# import python libraries
import sys, os
import pygame
# import pi-gui libraries
from interfaces import Interface
from music import Player
from utils import pressed

YELLOW = (255, 255, 0)

class PlayerInterface:

    def __init__(self, screen, book):
      self.screen = screen
      self.clock = pygame.time.Clock()
      self.interface = Interface()
      self.book = book
      self.music = Player(self.book)
      
    def __del__(self):
      pass

    def on_click(self):
      '''recognize touchscreen and mouse selections to 
      run functionalities of buttons'''
      click_pos = pressed()
      # stop music and return to previous screen
      if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
        self.music.stop()
        return False
      # pause/unpause the music
      if 155 <= click_pos[0] <= 200 and 190 <= click_pos[1] <= 235:
        self.music.pause()
      # stop the music the music        
      if 210 <= click_pos[0] <= 255 and 190 <= click_pos[1] <= 235:
        self.music.stop()
      # play the music
      if 265 <= click_pos[0] <= 310 and 190 <= click_pos[1] <= 235:
        self.music.play()
      # skip to selected position on the progress bar 
      if 10 <= click_pos[0] <= 310 and 160 <= click_pos[1] <= 185:
        self.music.set_pos(click_pos[0])
      return True

    def run(self):
      '''run method for drawing the screen to dispay'''
      mainloop = True
      while mainloop:
        # Limit frame speed to 30 FPS
        self.clock.tick(30)
        # draw interface to screen
        self.interface.player_interface(self.screen, self.book.getTitle(),
          self.book.getArtist(), self.book.getChapterPlaytime()[self.music.get_chapter()], 
          self.music.get_pos(), self.book.getCover())
        for event in pygame.event.get():
          # wait for touchscreen pressed
          if event.type == pygame.MOUSEBUTTONDOWN:
            # draw touchscreen feedback to screen
            pygame.draw.circle(self.screen, YELLOW, pressed(), 10, 0)
            # run functionalities
            mainloop = self.on_click()
        # update display
        pygame.display.flip()

 
            
            


 

