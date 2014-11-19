'''
information screen for display some system facts to the pi-gui system 
like disk space, cpu usage ... 
'''

# import python libraries
import sys, os, time
import psutil
import socket
import pygame
# import pi-gui functions
from interfaces import Interface
from utils import pressed

YELLOW = (255, 255, 0)

class InfoScreen:
	'''class for gathering system informations and displaying them'''
	
	def __init__(self, screen, music_folder):
		# init important variables
		self.screen = screen
		# needed for framerate
		self.clock = pygame.time.Clock()
		# containing all interface functions
		self.interface = Interface()

	def __del__(self):
		pass

	def hdd_info(self, path):
		'''get informations about free and total disk space'''
		# get space information
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
		''' get informations about ram usage'''
		# get percantage of used ram 
		return int(psutil.virtual_memory()[2])

	def ip_info(self):
		'''if connected to a network get the ip networking address'''
		try:
			# open sokect connection
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# ping www.google.com
			s.connect(('www.google.de', 0))
			# get ip string
			ip = s.getsockname()[0]
		except:
			ip = 'not connected to inet'
		return ip

	def exit(self):
		'''exit program and show a little exit message'''
		# create exit message
		self.interface.exit_interface(self.screen)
		pygame.display.flip()
		# wait 2 seconds and quit
		time.sleep(2)
		sys.exit()


	def run(self):
		'''run function for display information screen'''
		mainloop = True
		# use infinity loop for display
		while mainloop:
			# Limit frame speed to 120 FPS
			self.clock.tick(120)
			for event in pygame.event.get():
				# draw interface to diplay
				self.interface.info_interface(self.screen, self.cpu_info(), 
					self.ram_info(), self.hdd_info("/"), self.ip_info())
				# get actual mouse position
				click_pos = pressed()
				# draw touchscreen feedback
				pygame.draw.circle(self.screen, YELLOW, pressed(), 10, 0)
				# return to previous screen
				if 10 <= click_pos[0] <= 55 and 190 <= click_pos[1] <= 235:
					mainloop = False
				# exit program
				if 265 <= click_pos[0] <= 310 and 190 <= click_pos[1] <= 235:
					self.exit()
			# update display
			pygame.display.flip()