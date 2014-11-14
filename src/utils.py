#!/usr/bin/env python

'''
Description
'''
#@author: Philipp Sehnert
#@contact: philipp.sehnert[a]gmail.com

# import python libraries
import sys, os
import pygame

def str2time(string):
	x = string.split(':', 3)
	if len(x) < 3: x = ['00'] + x
	x = int(x[0])*3600000 + int(x[1])*60000 + int(x[2])*1000
	return x

def time2str(time):
	s = time/1000
	m,s = divmod(s, 60)
	h,m = divmod(m, 60)
	return '%d:%d:%d' % (h,m,s)

def save_progress():
	pass

def load_progress():
	pass

def timer():
	pass