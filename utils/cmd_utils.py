# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:21:07 2023

Author: Alyssa Bekai Rose

Purpose: Helper script for command line functions.
"""

import ctypes
import msvcrt
import win32api # pip install pywin32
import os
import subprocess
from ctypes import wintypes


def maximize_console(lines=None):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SW_MAXIMIZE = 3

    kernel32.GetConsoleWindow.restype = wintypes.HWND
    kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
    kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
    user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
    
    os.system("cls")
    print_center("", lines)
    os.system("cls")
    return cols, lines

def monitor_Hz():
    device = win32api.EnumDisplayDevices()
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    cycleRefresh = getattr(settings, 'DisplayFrequency')
    
    return cycleRefresh

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

import shutil

def print_center(s, lines):
    print(("\n"*round(lines/2)) + "{}".format(s.center(shutil.get_terminal_size().columns)))

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]
    

def set_font_size(x=30, y=50):
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 0
    font.dwFontSize.X = x
    font.dwFontSize.Y = y
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Consolas"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))
    
    
def cmd_input_TEST():
    input_dict = {}
    
    Subject = input("What is participant's name/code?:  ")
    input_dict["subject"] = Subject
    print("\n")
    
    Subject_number = input("What is the subject's number? (e.g. subject 0, subject 1,...): ")
    print("\n")
    input_dict["subject_number"] = Subject_number
    
    Age = int(input("Subject's Age?:  "))
    if Age < 18 or Age > 99:
        while Age < 18 or Age > 99:
            print("\nError in age. Input a valid age. Try again...\n")
            Age = int(input("Subject's Age?:  "))
    print("\n")
    input_dict["age"] = Age
    
    
    Sex = int(input("Male (1) or Female (2):  "))
    if Sex != 1 and Sex != 2:
        while Sex != 1 and Sex != 2:
            print("\nError in sex. Input either 1 (Male) or 2 (Female). Try again...\n")
            Sex = int(input("Male (1) or Female (2):  "))
    input_dict["sex"] = Sex
    print("\n")
    
    Cond = str(input("HCL or LCL condition:  ")).lower()
    if Cond not in ["hcl", "lcl"]:
        while Cond not in ["hcl", "lcl"]:
            print("\nError in condition. Input either HCL or hcl for High Cognitive Load or LCL or lcl for Low Cognitive Load")
            Cond = str(input("HCL or LCL condition:  ")).lower()
    print("\n")
    input_dict["condition"] = Cond
    
    STD = float(input("Insert participant's STD with decimals (e.g. 0.9, 1.2, etc.): "))
    print("\n")
    input_dict["stimulus_time_duration"] = STD
    
    return input_dict
    
    
    
    
