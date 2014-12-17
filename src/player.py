'''
player created a screen containing various informations about the selected 
audio book and show the player interface on screen.
'''

# import python libraries
import sys, os
import pygame
# internal imports
from interfaces import Interface
from music import Player
from utils import pressed, timer

YELLOW = (255, 255, 0)

class PlayerInterface:

    def __init__(self, screen, book):
      self.screen = screen
      self.clock = pygame.time.Clock()
      # init interface 
      self.interface = Interface()
      # init books
      self.book = book
      # init the player 
      self.music = Player(self.book)

    def on_click(self):
      ''' recognize touchscreen and mouse selections to 
      run functionalities of buttons '''
      click_pos = pressed()
      # stop music and return to previous screen
      if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
        self.music.stop()
        return False
      # play previous chapter
      if 65 <= click_pos[0] <= 110 and 190 <= click_pos[1] <= 235:
        self.music.previous_chapter()
      # play next chapter
      if 115 <= click_pos[0] <= 160 and 190 <= click_pos[1] <= 235:
        self.music.next_chapter()
      # pause/unpause the music
      if 165 <= click_pos[0] <= 210 and 190 <= click_pos[1] <= 235:
        self.music.pause()
      # stop the music the music        
      if 215 <= click_pos[0] <= 260 and 190 <= click_pos[1] <= 235:
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
        self.interface.player_interface(self.screen, self.book.get_title(),
          self.book.get_artist(), self.music.get_chapter() + 1, self.book.get_num_chapter(),
          self.book.get_chapter_playtime()[self.music.get_chapter()], 
          self.music.get_pos(), self.book.get_cover())
        for event in pygame.event.get():
          if event.type == pygame.USEREVENT:
            # start playing next chapter when a song ends
            self.music.next_chapter()
          # wait for touchscreen pressed
          if event.type == pygame.MOUSEBUTTONDOWN:
            # draw touchscreen feedback to screen
            pygame.draw.circle(self.screen, YELLOW, pressed(), 10, 0)
            # run functionalities
            mainloop = self.on_click()
        # update display
        pygame.display.flip()

 
            
            


 

