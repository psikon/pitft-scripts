#!/usr/bin/env python

'''
information screen for display some system facts to the pi-gui system 
like disk space, cpu usage ... 
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# import python libraries
import sys, os
import psutil
import socket
import pygame
# import pi-gui functions
from src.graphics import Graphics


class InfoScreen:
	'''class for gathering system informations and displaying them'''
	
	def __init__(self, screen, music_folder):
		# init important variables
		self.screen = screen
		self.folder = music_folder
		# needed for framerate
		self.clock = pygame.time.Clock()
		# containing all interface functions
		self.graphics = Graphics()

	def __del__(self):
		pass

	def hdd_info(self, path):
		'''get informations about free and total disk space'''
		st = os.statvfs(path)
		# convert free and total to megabyte
		free = (st.f_bavail * st.f_frsize)/100000
		total = (st.f_blocks * st.f_frsize)/100000
		return (free, total)
	
	def cpu_info(self):
		'''get informations about cpu usage'''
		# load cpu usage informations every 1 seconds for every core
		cpu = psutil.cpu_percent(interval = 1, percpu = True)
		# return mean usage
		return sum(cpu)/len(cpu)
	
	def ram_info(self):
		# get percantage of used ram 
		return int(psutil.virtual_memory()[2])


	def ip_info(self):
		'''if connected get the ip networking address'''
		try:
			# open sokect connection
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# ping www.google.com
			s.connect(('www.google.de', 0))
			# get ip string
			ip = s.getsockname()[0]
		except:
			ip = 'not connected'
		return ip

	def book_info(self):
		'''counting number of audio files in music folder'''
		count = 0
		for book in os.listdir(self.folder):
			# find all files with specific audio ending
			if book.endswith(".txt"):
				count += 1
		return count 

	def run(self):
		'''run function for display information screen'''
		mainloop = True
		# use infinity loop for display
		while mainloop:
			# Limit frame speed to 30 FPS
			self.clock.tick(30)
			for event in pygame.event.get():
				# draw interface to diplay
				self.graphics.info_interface(self.screen, self.cpu_info(), 
				self.ram_info(), self.hdd_info("/"), 
				self.ip_info(), self.book_info())
				if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
					mainloop = False
			pygame.display.flip()