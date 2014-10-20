#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# imports
import sys, os
import RPi.GPIO as GPIO

class controls:

	def __init__():
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(22,GPIO.IN)
		GPIO.setup(21,GPIO.IN)
		GPIO.setup(18,GPIO.IN)

	def __del__():
		pass

	def button1():
		if GPIO.input(22):
        	print("22 gedrückt!")

	def button2():
		if GPIO.input(21):
        	print("21 gedrückt!")

    def button3():
    	if GPIO.input(18):
        	print("18 gedrückt!")
        	
GPIO.cleanup()