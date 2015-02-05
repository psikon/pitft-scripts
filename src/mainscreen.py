#!/usr/bin/env python
'''
Generate the main window for the pi-gui program. The interface show the last played 
item with cover, title and supllemental informations that is interactive 
and two buttons for show up the library screen and exit the porgram itself. 
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# python imports
import sys, os
import pygame
# internal imports
from interfaces import Interface

YELLOW = (255, 255, 0)

class MainMenu():
    ''' generate the start interface for accessing all other screens'''
    def __init__(self, screen, funcs, hardware_instance, book):
    	# declare important variables
        self.screen = screen
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.interface = Interface()
        # functions for the menu items
        self.funcs = funcs
        # cached book for last played window
        self.book = book

    #define function that checks for mouse location
    def on_click(self):
        click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
        # select last played item
        if 10 <= click_pos[0] <= 310 and 120 <= click_pos[1] <= 185:
            self.funcs['Continue'](self.book)
        # go to library screen 
        if 10 <= click_pos[0] <= 205 and 190 <= click_pos[1] <= 230:
            self.funcs['Select Book']()
        # exit gui
        if 265 <= click_pos[0] <= 315 and 190 <= click_pos[1] <= 230:
            self.interface.exit_interface(self.screen)

    def run(self):
        '''run method for drawing the screen to dispay'''
        mainloop = True
        # use infinity loop for showing the screen
        while mainloop:
            # Limit frame speed to 30 FPS
            self.clock.tick(30)
            self.interface.main_interface(self.screen, self.book)
            # wait for a pressed button or exit infinity loop
            for event in pygame.event.get():
                # recognize mouse and touchscreen activity
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
                    self.on_click()
            # update the screen
            pygame.display.flip()

