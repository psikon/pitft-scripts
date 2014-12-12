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
LIBRARY = "images/library.png"
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

    def menu_button(self, screen, text, posx, posy, width, height, 
        font_size, image):
        ''' create a button with an user defined text message'''
        self.set_font(font_size)
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (width, height)), (posx, posy))
        screen.blit(self.font.render(text, True, WHITE), 
            (width + 5 + posx, posy + (height-font_size)/2))

    def image_button(self, screen, image, xpos, ypos, width, height):
        ''' create a button with an image on it'''
        # draw icon
        screen.blit(pygame.transform.scale(image, (width, height)), (xpos, ypos))

    def continue_playback(self, screen, posx, posy, width, height, font_size, 
        image, title, artist, playtime):
        self.set_font(font_size)
        screen.blit(self.font.render("Continue Playback ?", True, WHITE), (10, 10))
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (120, 120)), (10, 65))
        self.title(screen, title, 10, 40, 300)
        self.artist(screen, artist, 135, 65)
        self.play_time(screen, playtime, 135, 120)
        return screen

    def title(self, screen, string, xpos, ypos, max_size):
        '''generate title field'''
        size = self.size
        while self.font.size(string)[0] >= max_size and self.size >= 16:
            size -= 1
            self.set_font(size)
        screen.blit(self.font.render(string, True, WHITE), (xpos, ypos))
        self.set_font(DEFAULT_SIZE)
        return screen

    def cover(self, screen, image, size_x, size_y, xpos, ypos):
        '''load and draw cover to screen'''
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (size_x, size_y)), (xpos, ypos))
        return screen

    def play_time(self, screen, playtime, xpos, ypos):
        ''' print playtime to screen'''
        screen.blit(self.font.render('Time:', True, WHITE), (xpos, ypos))
        screen.blit(self.font.render(str(playtime) + " min", True, WHITE), 
            (xpos, ypos + 25))
        return screen

    def artist(self, screen, artist, xpos, ypos):
        '''print duration to screen'''
        screen.blit(self.font.render('Artist:', True, WHITE), (xpos, ypos))
        screen.blit(self.font.render(artist, True, WHITE), (xpos, ypos + 25))
        return screen

    def play_bar(self, screen, total, pos):
        '''add usable playbar to screen showing the progress of audio file'''
        # calculate factor for progress
        factor = str2time(total)/300
        if pos == -1: pos = 0
        # write Time string to display
        screen.blit(self.font.render('Time:', True, WHITE), (10, 135))
        screen.blit(self.font.render(time2str(pos) + '/' + total, True, 
            WHITE), (70, 135))
        # draw actual position as moving vertical rectangle to screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect((pos/factor)+10, 160, 5, 25),0)
        # draw actual progress on screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect(10, 165, (pos/factor), 15),0)
        # draw frame of Playbar to screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect(10, 165, 300, 15), 1)
        return screen

    def chapter(self, screen, actualChapter, totalChapter, xpos, ypos):
        # draw chapter string
        screen.blit(self.font.render('Chapter:', True, WHITE), (xpos, ypos))
        # draw actual and total chapter number
        screen.blit(self.font.render(" %d/%d" % (actualChapter, totalChapter), 
            True, WHITE), (xpos + 75, ypos))
        return screen