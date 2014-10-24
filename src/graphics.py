#!/usr/bin/env python

'''
graphic library containing all functions needed for drawing interface 
to screen
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# python imports
import sys, os
import pygame

# define colors
WHITE = (255, 255, 255)
GREY = (64,64,64)
# define path to images
BG_IMG = "images/bg_alpha.png"
PREVIOUS = 'images/previous.png'
NEXT = 'images/next.png'
SELECT = 'images/select.png'
PAUSE = 'images/pause.png'
PLAY = 'images/play.png'


class Graphics:
    '''class containing drawing functions for interfaces'''
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)

    def __del__(self):
        pass

    def loadImage(self, filename, colorkey = None):
        '''function for loading pictures with and without alpha channel'''
        # load picture
        image = pygame.image.load(filename)
        # convert picture with or without alpha channel
        if image.get_alpha() == None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        # set colorkey
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        # return loaded image
        return image

    def make_button(self, screen, text, image, xpo, ypo, colour):
        screen.blit(self.font.render(text, True, GREY),(xpo,ypo))
        pygame.draw.rect(screen, (xpo-5,ypo-5,110,35),1)

    def list_interface(self, screen):
        '''generate screen for book selector interface'''
        # create background
        screen.fill(GREY)
        screen.blit(self.loadImage(BG_IMG),(0,0))
        # load button images
        left = self.loadImage(PREVIOUS)
        right = self.loadImage(NEXT)
        select = self.loadImage(SELECT)
        # draw buttons to screen
        screen.blit(pygame.transform.scale(left, (30,30)), (10,200))
        screen.blit(pygame.transform.scale(right, (30,30)), (45,200))
        screen.blit(pygame.transform.scale(select, (30,30)), (80,200))
        return screen

    def TitleField(self, screen, name):
        '''generate title field'''
        screen.blit(self.font.render(name, True, WHITE), (10, 10))
        return screen

    def CoverField(self, screen, image, folder):
        '''load and draw cover to screen'''
        cover = self.loadImage(folder + os.sep + image)
        screen.blit(pygame.transform.scale(cover, (150,150)), (155,40))
        return screen

    def PlayedField(self, screen, playtime):
        ''' print playtime to screen'''
        screen.blit(self.font.render('Played:', True, WHITE), (10, 45))
        screen.blit(self.font.render(str(playtime) + "min", True, WHITE), (10, 70))
        return screen

    def DurationField(self, screen, duration):
        '''print duration to screen'''
        screen.blit(self.font.render('Duration:', True, WHITE), (10, 100))
        screen.blit(self.font.render(str(duration) + "min", True, WHITE), (10, 125))
        return screen

    def player_interface(self, screen):
        '''generate the interface for the audio player'''
        # create background
        screen.fill(GREY)
        screen.blit(self.loadImage(BG_IMG),(0,0))
        # load images for buttons
        back = self.loadImage(PREVIOUS)
        pause = self.loadImage(PAUSE)
        play = self.loadImage(PLAY)
        # draw buttons to screen
        screen.blit(pygame.transform.scale(back, (30,30)), (10,200))
        screen.blit(pygame.transform.scale(pause, (30,30)), (45,200))
        screen.blit(pygame.transform.scale(play, (30,30)), (80,200))
        return screen

    def info_interface(self, screen, cpu, ram, hdd, ip, books):
        '''generate the information screen interface'''
        # draw background
        screen.fill(GREY)
        screen.blit(self.loadImage(BG_IMG),(0,0))
        # draw title
        screen.blit(self.font.render('System Information', True, WHITE), (10, 10))
        # load and draw button interface
        back = self.loadImage(PREVIOUS)
        screen.blit(pygame.transform.scale(back, (30,30)), (10,200))
        # draw system information fields
        self.cpuField(screen, cpu)
        self.RAMField(screen, ram)
        self.spaceField(screen, hdd) 
        self.ipField(screen, ip)
        self.bookField(screen, books)
        self.authorField(screen)
        return screen

    def spaceField(self, screen, hdd):
        '''draw disk usage status bar'''
        # write string to display
        screen.blit(self.font.render('HDD', True, WHITE), (10, 100))
        # draw rectangle indicating used disk space
        pygame.draw.rect(screen, (255,255,255),pygame.Rect(75, 103, ((hdd[0]*100)/hdd[1])*2.35, 15),0)
        # draw frame for visualize total disk space
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(75, 103, 235, 15), 1)
        return screen

    def cpuField(self, screen, cpu):
        '''draw status bar for cpu usage'''
        # write string to display
        screen.blit(self.font.render('CPU', True, WHITE), (10, 50))
        #draw status bar for cpu usage to screen 
        pygame.draw.rect(screen, (255,255,255),pygame.Rect(75, 53, ((cpu*100)/100)*2.35, 15),0)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(75, 53, 235, 15), 1)
        return screen

    def RAMField(self, screen, ram):
        '''draw status bar for ram usage'''
        # write string to display
        screen.blit(self.font.render('RAM ', True, WHITE), (10, 75))
        #draw status bar for ram usage to screen 
        pygame.draw.rect(screen, (255,255,255),pygame.Rect(75, 78, ram*2.35, 15),0)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(75, 78, 235, 15), 1)
        return screen

    def ipField(self, screen , ip):
        '''show ip on screen'''
        # write two strings to screen for ip 
        screen.blit(self.font.render('IP  ', True, WHITE), (10, 125))
        screen.blit(self.font.render(ip, True, WHITE), (75, 125))
        return screen

    def bookField(self, screen, count):
        '''count number of audio files in music folder and print it to info screen'''
        # display field name
        screen.blit(self.font.render('Books', True, WHITE), (10, 150))
        # display counted audio books
        screen.blit(self.font.render(str(count), True, WHITE), (75, 150))
        return screen

    def authorField(self, screen):
        '''add author information'''
        # print author information to screen
        screen.blit(self.font.render('Written by', True, WHITE), (10, 175))
        screen.blit(self.font.render('Philipp Sehnert', True, WHITE), (115, 175))
        return screen




