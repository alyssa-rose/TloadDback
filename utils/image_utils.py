# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:34:09 2023

@author: Rose.Alyssa
"""

import os
import tkinter as tk
from PIL import ImageTk
from PIL import Image
import numpy as np
from win32api import GetSystemMetrics
from tkinter.ttk import Label



screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)


IMG_PATHS_TEST = {1 : r"images\test\Instructions_1.bmp",
                  2 : r"images\test\Instructions_2.bmp",
                  3 : r"images\test\Instructions_3.bmp"}

IMG_PATHS_PRE = {1 : r"images\pretest\General_Instructions.bmp",
                 2 : r"images\pretest\Digits_Instructions.bmp",
                 3 : r"images\pretest\Letters_Instructions.bmp",
                 4 : r"images\pretest\Letters_Digits_Instructions.bmp"}


    

def display_instruction(image_path: str):
    root = tk.Tk()
    root.configure(background="black")
    root.focus_force()
    root.bind("<space>", lambda x: root.destroy())
    
    root.title('TloadDback Instructions')
    image1 = ImageTk.PhotoImage(Image.open(image_path))
    #w = image1.width()
    w = screen_width
    h = screen_height
    #h = image1.height()
    x = 0
    y = 0
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    panel1 = tk.Label(root, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')
    panel1.image = image1
    root.overrideredirect(True)
    
    root.mainloop()