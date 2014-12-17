'''
graphic library for storing image path and graphicl parameter for the seperated 
graphic fields and all items needed for drawing the interfaces to screen
'''

# python imports
import sys, os, time
import pygame
# internal imports
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
    '''class containing all functions for drawing the interfaces'''
    
    def __init__(self):
        # init the font
        self.size = DEFAULT_SIZE
        self.font = pygame.font.SysFont(DEFAULT_FONT, DEFAULT_SIZE)


    def get_font(self):
        ''' retrun actual loaded font '''
        return self.font

    def set_font(self, font_size):
        ''' set the a new font size '''
        self.font = pygame.font.SysFont(DEFAULT_FONT, font_size)

    def load_image(self, filename, colorkey = None):
        '''function for loading pictures with and without alpha channel'''
        # load picture or place holder
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
        ''' create a button with an image on the left side and some user defined 
        text on the right side'''
        # define new font size
        self.set_font(font_size)
        # draw the image to set position
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (width, height)), (posx, posy))
        # draw text after the image
        screen.blit(self.font.render(text, True, WHITE), 
            (width + 5 + posx, posy + (height-font_size)/2))

    def image_button(self, screen, image, xpos, ypos, width, height):
        ''' create a button with an image on it'''
        # draw icon
        screen.blit(pygame.transform.scale(image, (width, height)), (xpos, ypos))

    def continue_playback(self, screen, posx, posy, width, height, font_size, 
        image, title, artist, playtime):
        ''' create a little information field about the last played item ''' 
        # set new font size
        self.set_font(font_size)
        # draw title on field
        screen.blit(self.font.render("Continue Playback ?", True, WHITE), (10, 10))
        # draw some informations about last playback
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (110, 110)), (10, 65))
        self.title_field(screen, title, 10, 40, 300)
        self.artist_field(screen, artist, 135, 65)
        self.play_time_field(screen, playtime, 135, 120)
        return screen

    def title_field(self, screen, string, xpos, ypos, max_size):
        ''' generate title field '''
        # init actual needed size of the title string
        size = self.size
        # adjust font size until title string fits into display
        while self.font.size(string)[0] >= max_size and self.size >= 16:
            size -= 1
            self.set_font(size)
        # draw title string
        screen.blit(self.font.render(string, True, WHITE), (xpos, ypos))
        # set font size to default
        self.set_font(DEFAULT_SIZE)
        return screen

    def cover_field(self, screen, image, size_x, size_y, xpos, ypos):
        ''' load and draw cover to screen '''
        screen.blit(pygame.transform.scale(self.load_image(image), 
            (size_x, size_y)), (xpos, ypos))
        return screen

    def play_time_field(self, screen, playtime, xpos, ypos):
        ''' draw playtime to screen'''
        screen.blit(self.font.render('Time:', True, WHITE), (xpos, ypos))
        screen.blit(self.font.render(str(playtime) + " min", True, WHITE), 
            (xpos, ypos + 25))
        return screen

    def artist_field(self, screen, artist, xpos, ypos):
        ''' draw artist name to screen '''
        screen.blit(self.font.render('Artist:', True, WHITE), (xpos, ypos))
        screen.blit(self.font.render(artist, True, WHITE), (xpos, ypos + 25))
        return screen

    def play_bar(self, screen, total, pos):
        ''' add usable playbar to screen showing the progress of the actual played 
            audio file'''
        # calculate factor for progress
        factor = str2time(total)/300
        if pos == -1: pos = 0
        # write Time string to display
        screen.blit(self.font.render('Time:', True, WHITE), (10, 135))
        screen.blit(self.font.render(time2str(pos) + '/' + total, True, 
            WHITE), (70, 135))
        # draw actual position as moving vertical rectangle to screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect((pos/factor) + 10, 160, 5, 25), 0)
        # draw actual progress on screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect(10, 165, (pos/factor), 15), 0)
        # draw frame of Playbar to screen
        pygame.draw.rect(screen, WHITE, 
            pygame.Rect(10, 165, 300, 15), 1)
        return screen

    def chapter_field(self, screen, actualChapter, totalChapter, xpos, ypos):
        ''' draw actual played chapter and total number of chapter to screen ''' 
        screen.blit(self.font.render('Chapter:', True, WHITE), (xpos, ypos))
        screen.blit(self.font.render(" %d/%d" % (actualChapter, totalChapter), 
            True, WHITE), (xpos + 75, ypos))
        return screen

    def seperator_line(self, screen):
        ''' draw a WHITE seperator line for dividing the interface and the 
        navigation buttons '''
        pygame.draw.rect(screen, WHITE, pygame.Rect(10, 187, 300, 1), 1)
        return screen