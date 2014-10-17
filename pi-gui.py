#!/usr/bin/python

from Tkinter import Frame, Tk, BOTH, Text, Menu, END
from ttk import Button, Style
import tkFileDialog 
from PIL import Image, ImageTk
import os, sys

class Window(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.MainUI()
    
    def MainUI(self):
      # init options
      self.parent.title("Main menu")
      self.pack(fill = BOTH, expand = 1)
      # set stylle
      style = Style()
      style.configure("TFrame", background = "#333")
      self.style.theme_use("default")
  
      fileButton = Button(self, text = "Select",
      					command = self.onOpen)
      fileButton.place(x = 100, y = 100)

    def onOpen(self):
      
        ftypes = [('mp3 Files', '*.mp3'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    


def main():
  
    root = Tk()
    root.geometry("320x240+0+0")
    app = Window(root)
    root.mainloop()  

sys.exit(main())
