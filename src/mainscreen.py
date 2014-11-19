#!/usr/bin/env python

'''
Generate the main window for the pi-gui program. The class generate a menu for the start
screen and add control options for the cursor keys and the pitft buttons.
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# python imports
import sys, os
import pygame
# pi-gui imports
from interfaces import Interface

YELLOW = (255, 255, 0)

class MainMenu():
    ''''''
    def __init__(self, screen, funcs, hardware_instance):
    	# declare important variables
        self.screen = screen
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.interface = Interface()
        # functions for the menu items
        self.funcs = funcs

    #define function that checks for mouse location
    def on_click(self):
        click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
        #now check to see if button 1 was pressed
        if 50 <= click_pos[0] <= 270 and 40 <= click_pos[1] <= 90:
            self.funcs['Continue']()
        #now check to see if button 2 was pressed
        if 50 <= click_pos[0] <= 270 and 100 <= click_pos[1] <= 150:
            self.funcs['Select Book']()
        #now check to see if button 3 was pressed
        if 50 <= click_pos[0] <= 270 and 160 <= click_pos[1] <= 210:
            self.funcs['Information']()
 
    def run(self):
        '''run method for drawing the screen to dispay'''
        mainloop = True
        # use infinity loop for showing the screen
        while mainloop:
            # Limit frame speed to 30 FPS
            self.clock.tick(30)
            # wait for a pressed button or exit infinity loop
            for event in pygame.event.get():
                self.interface.main_interface(self.screen)
                if event.type == pygame.KEYDOWN:
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
                    self.on_click()
            # update the screen
            pygame.display.flip()

