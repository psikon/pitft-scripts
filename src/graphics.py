'''
graphic library containing all functions needed for drawing interface 
to screen
'''

# python imports
import sys, os, time
import pygame
from utils import str2time, time2str

# define default font
DEFAULT_FONT = 'Arial'
DEFAULT_SIZE = 20
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
        self.size = DEFAULT_SIZE
        self.font = pygame.font.SysFont(DEFAULT_FONT, DEFAULT_SIZE)

    def __del__(self):
        pass

    def get_font(self):
        return self.font

    def set_font(self, font_size):
        self.font = pygame.font.SysFont(DEFAULT_FONT, font_size)

    def load_image(self, filename, colorkey = None):
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
        font_size):
        ''' create a button with an user defined text message'''
        self.set_font(font_size)
        screen.blit(self.font.render(text, True, WHITE), (posx, posy))

    def makeImagebutton(self, screen, image, xpos, ypos, width, height):
        ''' create a button with an image on it'''
        # draw icon
        screen.blit(pygame.transform.scale(image, (width, height)), (xpos, ypos))

    def Title(self, screen, string):
        '''generate title field'''
        size = self.size
        while self.font.size(string)[0] >= 300 and self.size >= 16:
            size -= 1
            self.set_font(size)
        screen.blit(self.font.render(string, True, WHITE), (10, 10))
        self.set_font(DEFAULT_SIZE)
        return screen

    def Cover(self, screen, image, size_x, size_y, xpos, ypos):
        '''load and draw cover to screen'''
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (size_x, size_y)), (xpos, ypos))
        return screen

    def PlayTime(self, screen, playtime):
        ''' print playtime to screen'''
        screen.blit(self.font.render('Time:', True, WHITE), (10, 100))
        screen.blit(self.font.render(str(playtime) + " min", True, WHITE), (10, 125))
        return screen

    def Artist(self, screen, artist):
        '''print duration to screen'''
        screen.blit(self.font.render('Artist:', True, WHITE), (10, 45))
        screen.blit(self.font.render(artist, True, WHITE), (10, 70))
        return screen

    def PlayBar(self, screen, total, pos):
        '''add usable playbar to screen showing the progress of audio file'''
        # calculate factor for progress
        factor = str2time(total)/300
        if pos == -1: pos = 0
        # write Time string to display
        screen.blit(self.font.render('Time:', True, WHITE), (10, 135))
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

    def Chapter(self, screen, actualChapter, totalChapter):
        screen.blit(self.font.render('Chapter:', True, WHITE), (10, 100))
        screen.blit(self.font.render(" %d/%d" % (actualChapter, totalChapter), True,
          WHITE), (85, 100))
        return screen