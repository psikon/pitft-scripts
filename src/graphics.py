'''
graphic library containing all functions needed for drawing interface 
to screen
'''

# python imports
import sys, os, time
import pygame
from utils import str2time, time2str

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

    def getFont(self):
        return self.font

    def setFont(self, font, font_size):
        self.font = pygame.font.SysFont(font, font_size)

    def loadImage(self, filename, colorkey = None):
        '''function for loading pictures with and without alpha channel'''
        # load picture
        try:
            image = pygame.image.load(filename)
        except:
            image = pygame.image.load('images/unknown.jpg')
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

    def makeTextButton(self, screen, text, posx, posy, width, height, 
        font, font_size):
        ''' create a button with an user defined text message'''
        self.setFont(font, font_size)
        screen.blit(self.font.render(text, True, WHITE), (posx, posy))

    def makeImagebutton(self, screen, image, xpos, ypos, width, height):
        ''' create a button with an image on it'''
        # draw icon
        screen.blit(pygame.transform.scale(image, (width, height)), (xpos, ypos))

    def Title(self, screen, name):
        '''generate title field'''
        screen.blit(self.font.render(name, True, WHITE), (10, 10))
        return screen

    def Cover(self, screen, image, size_x, size_y, xpos, ypos):
        '''load and draw cover to screen'''
        screen.blit(pygame.transform.scale(self.loadImage(image), 
            (size_x, size_y)), (xpos, ypos))
        return screen

    def PlayTime(self, screen, playtime):
        ''' print playtime to screen'''
        screen.blit(self.font.render('Time:', True, WHITE), (10, 100))
        screen.blit(self.font.render(str(playtime) + " min", True, WHITE), (10, 125))
        return screen

    def Artist(self, screen, artist):
        '''print duration to screen'''
        screen.blit(self.font.render('Artist', True, WHITE), (10, 45))
        screen.blit(self.font.render(artist, True, WHITE), (10, 70))
        return screen

    def PlayBar(self, screen, total, pos):
        '''add usable playbar to screen showing the progress of audio file'''
        # calcultate factor for progress
        factor = str2time(total)/300
        if pos == -1: pos = 0
        # write Time string to display
        screen.blit(self.font.render('Time: ', True, WHITE), (10, 135))
        screen.blit(self.font.render(time2str(pos) + '/' + total, True, 
            WHITE), (70, 135))
        # draw actual position as moving vertical rectangle to screen
        pygame.draw.rect(screen, (255,255,255), 
            pygame.Rect((pos/factor)+10, 160, 5, 25),0)
        # draw actual progress on screen
        pygame.draw.rect(screen, (255,255,255), 
            pygame.Rect(10, 165, (pos/factor), 15),0)
        # draw frame of Playbar to screen
        pygame.draw.rect(screen, (255,255,255), 
            pygame.Rect(10, 165, 300, 15), 1)
        return screen

    def spaceField(self, screen, hdd):
        '''draw disk usage status bar'''
        # write string to display
        screen.blit(self.font.render('HDD', True, WHITE), (10, 100))
        # draw rectangle indicating used disk space
        pygame.draw.rect(screen, (255, 255, 255), 
            pygame.Rect(75, 103, ((hdd[0]*100)/hdd[1])*2.35, 15), 0)
        # draw frame for visualize total disk space
        pygame.draw.rect(screen, (255, 255, 255), 
            pygame.Rect(75, 103, 235, 15), 1)
        return screen

    def cpuField(self, screen, cpu):
        '''draw status bar for cpu usage'''
        # write string to display
        screen.blit(self.font.render('CPU', True, WHITE), (10, 50))
        #draw status bar for cpu usage to screen 
        pygame.draw.rect(screen, (255 ,255, 255), 
            pygame.Rect(75, 53, ((cpu*100)/100)*2.35, 15), 0)
        pygame.draw.rect(screen, (255, 255, 255), 
            pygame.Rect(75, 53, 235, 15), 1)
        return screen

    def RAMField(self, screen, ram):
        '''draw status bar for ram usage'''
        # write string to display
        screen.blit(self.font.render('RAM ', True, WHITE), (10, 75))
        #draw status bar for ram usage to screen 
        pygame.draw.rect(screen, (255, 255, 255), 
            pygame.Rect(75, 78, ram*2.35, 15), 0)
        pygame.draw.rect(screen, (255, 255, 255), 
            pygame.Rect(75, 78, 235, 15), 1)
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




