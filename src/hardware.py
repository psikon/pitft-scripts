#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

import pygame

class hardware:

    def __init__(self, interface):
        if interface:
            print 'GUI in pitft mode'
        else:
            pygame.init()
            self.screen = pygame.display.set_mode((320,240))
            pygame.display.update()

    def __del__(self):
        pass

    def getScreen(self):
    	return(self.screen)
