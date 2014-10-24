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
        pygame.mouse.set_visible(False)

    def __del__(self):
        pass

    def getFont(self):
        return self.font

    def setFont(self, font, font_size):
        self.font = pygame.font.SysFont(font, font_size)

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

    def makeTextButton(self, screen, text, posx, posy, width, height, font, font_size):
        self.setFont(font, font_size)
        screen.blit(self.font.render(text, True, WHITE), (posx, posy))
        #pygame.draw.rect(screen, WHITE, (posx-5, posy-5, width , height), 1)

    def makeImagebutton(self, screen, image, xpos, ypos, width, height):
        # draw icon
        screen.blit(pygame.transform.scale(image, (width, height)), (xpos, ypos))
        # frame around icon
        #pygame.draw.rect(screen, WHITE, (xpos, ypos, 31, 31), 1)

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
        self.makeImagebutton(screen, left, 10, 190, 45, 45)
        self.makeImagebutton(screen, right, 65, 190, 45, 45)
        self.makeImagebutton(screen, select, 120, 190, 45, 45)
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
        self.makeImagebutton(screen, back, 10, 190, 45, 45)
        self.makeImagebutton(screen, pause, 65, 190, 45, 45)
        self.makeImagebutton(screen, play, 120, 190, 45, 45)
        return screen

    def info_interface(self, screen, cpu, ram, hdd, ip):
        '''generate the information screen interface'''
        # draw background
        screen.fill(GREY)
        screen.blit(self.loadImage(BG_IMG),(0,0))
        # draw title
        self.setFont('Arial', 30)
        screen.blit(self.font.render('System Information', True, WHITE), (10, 10))
        self.setFont('Arial', 14)
        # load and draw button interface
        back = self.loadImage(PREVIOUS)
        self.makeImagebutton(screen, back, 10, 190, 45, 45)
        exit = self.loadImage(SELECT)
        screen.blit(self.font.render('close gui', True, WHITE), (260, 170))
        self.makeImagebutton(screen, exit, 265, 190, 45, 45)
        self.setFont('Arial', 20)
        # draw system information fields
        self.cpuField(screen, cpu)
        self.RAMField(screen, ram)
        self.spaceField(screen, hdd) 
        self.ipField(screen, ip)
        self.authorField(screen)
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

    def authorField(self, screen):
        '''add author information'''
        # print author information to screen
        screen.blit(self.font.render('Written by', True, WHITE), (10, 150))
        screen.blit(self.font.render('Philipp Sehnert', True, WHITE), (115, 150))
        return screen




