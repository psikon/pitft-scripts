#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# imports
import sys, os
import pygame
from graphics import Graphics

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0,0,139)

class MenuItem(pygame.font.Font):
    def __init__(self, text, font = None, font_size = 30, font_color = WHITE, 
    			(pos_x, pos_y) = (0, 0)):
 		# init font
        pygame.font.Font.__init__(self, font, font_size)
        # declare variables
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 	
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class MainMenu():

    def __init__(self, screen, items, funcs, font = None, font_size = 45,
                 font_color = WHITE):
    	# declare important variables
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.graphics = Graphics()
        self.funcs = funcs
        # create empty menu stack
        self.items = []
        # generate menu items
        for index, item in enumerate(items):
        	# init new menu item
            menu_item = MenuItem(item, font, font_size, font_color)
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            # set postion of new item
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + (index * menu_item.height)
            menu_item.set_position(pos_x, pos_y)
            # add menu item to stack
            self.items.append(menu_item)
        self.cur_item = None

 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_LEFT and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_LEFT and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_RIGHT and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_RIGHT and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(BLUE)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()
 
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 30 FPS
            self.clock.tick(30)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.set_keyboard_selection(event.key)
 
            # Redraw the background
            self.screen.fill((64,64,64))
            self.screen.blit(self.graphics.loadImage("images/bg_alpha.png"),(0,0))
 
            for item in self.items:
                self.screen.blit(item.label, item.position)
 
            pygame.display.flip()

