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
from graphics import Graphics

# define colors for menu
WHITE = (255, 255, 255)
GREY = (64,64,64)
BLUE = (0,0,139)
YELLOW = (255, 255, 0)

class MenuItem(pygame.font.Font):
    ''' class stroring informations for one menu item''' 
    def __init__(self, text, font = None, font_size = 60, 
        font_color = WHITE, (pos_x, pos_y) = (0, 0)):
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
        '''set position on screen for menu item'''
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        '''colorise menu item'''
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class MainMenu():
    '''generate menu items add them to screen, make them selectable and register functions to 
    them'''
    def __init__(self, screen, items, funcs, hardware_instance):
    	# declare important variables
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        # important for framerate
        self.clock = pygame.time.Clock()
        # contain all interface methods
        self.graphics = Graphics()
        # used for control - like pitft buttons
    	self.hardware = hardware_instance
        # functions for the menu items
        self.funcs = funcs
        # create empty menu stack
        self.items = []
        # generate menu items
        for index, item in enumerate(items):
        	# init new menu item
            menu_item = MenuItem(item)
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            # set postion of new item
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + (index * menu_item.height)
            menu_item.set_position(pos_x, pos_y)
            # add menu item to stack
            self.items.append(menu_item)
        # set current item to none
        self.cur_item = None

 
    def set_keyboard_selection(self, key):
        '''colorize the selected menu item, marked by left and right cursor keys or
        pitft buttons'''
        # make all menu items unselected
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
        # check for selected items
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
        # set selected items to italic and blue
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(BLUE)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()

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
                if event.type == pygame.KEYDOWN:
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    pygame.draw.circle(self.screen, YELLOW, pos, 10, 0)
                    self.on_click()
 
            # draw the background
            self.screen.fill(GREY)
            self.screen.blit(self.graphics.loadImage("images/bg_alpha.png"),(0,0))
            self.graphics.makeTextButton(self.screen, "Last Played", 50, 20, 220, 55,'Arial', 40)
            self.graphics.makeTextButton(self.screen, "Select Book", 50, 90, 220, 55, 'Arial', 40)
            self.graphics.makeTextButton(self.screen, "Information", 50, 160, 220, 55, 'Arial', 40)
            # draw menu items on screen
            #for item in self.items:
            #    self.graphics.makeTextButton(self.screen, item.text, item.position[0], item.position[1])
            #    #self.screen.blit(item.label, item.position)
            # update the screen
            pygame.display.flip()

