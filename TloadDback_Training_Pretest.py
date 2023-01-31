# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 09:07:45 2023

Author: Alyssa Bekai Rose

Purpose: For the Pilot Cognitive Inference (PCI) program. This script performs
    the TloadDback pretest sequence. 
"""
import os
import win32api # pip install pywin32
# import pygame
from win32api import GetSystemMetrics
import yaml
import pandas as pd
import tkinter as tk
from PIL import ImageTk
from PIL import Image
import numpy as np
import keyboard # pip install keyboard
from utils.cmd_utils import maximize_console, monitor_Hz, cmd_input_TEST, set_font_size, print_center
from utils.image_utils import display_instruction
import time
import ctypes
import datetime


series1         = [ 'L'  'A'  'A'  'R'  'N'  'N'  'R'  'T'  'E'  'E'  'N'  'U'  'N'  'N'  'N'  'P'  'P'  'R'  'E'  'E'  'T'  'U'  'T'  'R'  'R'  'A'  'L'  'L'  'P'  'P' ]
REPONSE_SERIES1 = [ '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1' ]

series2         = [ 'A'  'C'  'C'  'L'  'N'  'R'  'R'  'L'  'E'  'E'  'A'  'P'  'P'  'T'  'N'  'T'  'U'  'T'  'C'  'C'  'R'  'R'  'E'  'L'  'L'  'A'  'A'  'A'  'U'  'U' ]
REPONSE_SERIES2 = [ '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '1'  '0'  '1' ]

series3         = [ 'C'  'R'  'R'  'E'  'E'  'N'  'L'  'L'  'T'  'U'  'R'  'C'  'C'  'E'  'E'  'N'  'U'  'C'  'L'  'L'  'P'  'R'  'R'  'A'  'A'  'T'  'L'  'L'  'P'  'P' ]
REPONSE_SERIES3 = [ '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1' ]

series4         = [ 'N'  'N'  'E'  'L'  'L'  'C'  'U'  'C'  'C'  'R'  'L'  'P'  'P'  'A'  'A'  'N'  'R'  'R'  'L'  'U'  'U'  'L'  'C'  'E'  'C'  'C'  'P'  'P'  'N'  'N' ]
REPONSE_SERIES4 = [ '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1' ]

series5         = [ 'A'  'T'  'U'  'U'  'R'  'R'  'R'  'C'  'N'  'N'  'L'  'L'  'R'  'E'  'E'  'A'  'T'  'T'  'C'  'C'  'U'  'L'  'U'  'P'  'T'  'R'  'C'  'C'  'P'  'P' ]
REPONSE_SERIES5 = [ '0'  '0'  '0'  '1'  '0'  '1'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '0'  '0'  '1'  '0'  '1' ]

series6         = [ 'T'  'T'  'E'  'R'  'R'  'N'  'A'  'C'  'T'  'L'  'L'  'C'  'C'  'E'  'U'  'U'  'L'  'L'  'C'  'R'  'C'  'C'  'T'  'R'  'R'  'A'  'A'  'N'  'A'  'A' ]
REPONSE_SERIES6 = [ '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1' ]

series7         = [ 'L'  'C'  'C'  'E'  'E'  'A'  'C'  'L'  'L'  'U'  'R'  'N'  'N'  'P'  'A'  'T'  'P'  'P'  'C'  'C'  'U'  'U'  'L'  'E'  'R'  'R'  'T'  'T'  'A'  'A' ]
REPONSE_SERIES7 = [ '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1' ]

series8         = [ 'R'  'R'  'L'  'P'  'P'  'A'  'C'  'C'  'E'  'E'  'C'  'E'  'N'  'N'  'P'  'T'  'T'  'A'  'C'  'U'  'L'  'L'  'U'  'U'  'R'  'T'  'T'  'P'  'R'  'R' ]
REPONSE_SERIES8 = [ '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1' ]

series9         = [ 'U'  'L'  'L'  'A'  'T'  'T'  'E'  'E'  'R'  'R'  'R'  'C'  'C'  'R'  'A'  'U'  'U'  'A'  'A'  'L'  'P'  'P'  'C'  'U'  'R'  'R'  'T'  'E'  'U'  'N' ]
REPONSE_SERIES9 = [ '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0' ]

series10        = [ 'C'  'E'  'C'  'C'  'R'  'T'  'A'  'U'  'N'  'N'  'P'  'P'  'A'  'P'  'P'  'U'  'T'  'T'  'R'  'R'  'U'  'U'  'C'  'E'  'E'  'L'  'A'  'A'  'L'  'L' ]
REPONSE_SERIES10= [ '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1' ]

series11        = [ 'A'  'L'  'R'  'R'  'T'  'U'  'C'  'U'  'U'  'U'  'U'  'A'  'E'  'A'  'P'  'P'  'R'  'N'  'N'  'L'  'C'  'E'  'E'  'R'  'R'  'L'  'U'  'U'  'E'  'E' ];
REPONSE_SERIES11= [ '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '1'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1' ]

series12        = [ 'T'  'C'  'C'  'A'  'A'  'T'  'L'  'L'  'E'  'U'  'P'  'P'  'A'  'A'  'T'  'T'  'N'  'E'  'U'  'U'  'R'  'A'  'C'  'T'  'L'  'L'  'L'  'U'  'P'  'P' ];
REPONSE_SERIES12= [ '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '1'  '1'  '0'  '0'  '1' ]

series13        = [ 'A'  'A'  'R'  'R'  'T'  'U'  'U'  'E'  'E'  'N'  'P'  'A'  'A'  'A'  'P'  'T'  'T'  'T'  'N'  'N'  'C'  'E'  'N'  'N'  'P'  'L'  'U'  'C'  'C'  'C' ];
REPONSE_SERIES13= [ '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0' ]

series14        = [ 'E'  'E'  'T'  'A'  'U'  'U'  'T'  'R'  'R'  'R'  'L'  'L'  'U'  'E'  'T'  'P'  'P'  'A'  'L'  'P'  'A'  'A'  'C'  'A'  'A'  'C'  'C'  'N'  'R'  'R' ];
REPONSE_SERIES14= [ '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1' ]

series15        = [ 'U'  'C'  'R'  'R'  'C'  'C'  'L'  'N'  'N'  'U'  'U'  'R'  'A'  'A'  'T'  'L'  'L'  'E'  'U'  'U'  'R'  'A'  'C'  'T'  'T'  'N'  'N'  'U'  'U'  'E' ];
REPONSE_SERIES15= [ '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '0' ]

series16         = [ 'U'  'T'  'L'  'L'  'A'  'C'  'C'  'A'  'E'  'E'  'R'  'C'  'R'  'R'  'P'  'P'  'N'  'A'  'T'  'T'  'N'  'U'  'U'  'E'  'N'  'N'  'N'  'A'  'C'  'C' ]
REPONSE_SERIES16 = [ '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '1'  '0'  '0'  '1' ]

series17         = [ 'E'  'E'  'U'  'A'  'A'  'R'  'R'  'N'  'P'  'N'  'E'  'E'  'T'  'E'  'T'  'T'  'C'  'A'  'A'  'T'  'C'  'C'  'T'  'R'  'R'  'L'  'E'  'N'  'N'  'L' ]
REPONSE_SERIES17 = [ '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '1' ]

series18         = [ 'T'  'C'  'C'  'T'  'C'  'A'  'E'  'E'  'N'  'N'  'R'  'P'  'P'  'A'  'A'  'U'  'A'  'A'  'C'  'T'  'T'  'L'  'C'  'C'  'E'  'E'  'T'  'C'  'C'  'R' ]
REPONSE_SERIES18 = [ '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0' ]

series19         = [ 'N'  'N'  'L'  'A'  'N'  'U'  'U'  'T'  'R'  'R'  'A'  'A'  'R'  'P'  'L'  'T'  'T'  'E'  'A'  'U'  'U'  'N'  'A'  'T'  'T'  'N'  'C'  'C'  'C'  'C' ]
REPONSE_SERIES19 = [ '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '1'  '1' ]

series20         = [ 'C'  'T'  'T'  'E'  'R'  'E'  'E'  'U'  'U'  'N'  'P'  'P'  'A'  'C'  'C'  'A'  'T'  'R'  'R'  'N'  'N'  'P'  'U'  'U'  'L'  'L'  'P'  'L'  'L'  'E' ]
REPONSE_SERIES20 = [ '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0' ]


def separate_series(series: list):
    split_series = []
    for i in series[0]: 
        split_series.append(i)
        
    return split_series

def make_series_list():
    series_all = [series1, series2, series3, series4, series5, series6, 
                  series7, series8, series9, series10, series11, series12, 
                  series13, series14, series15, series16, series17, series18, 
                  series19, series20]
    
    response_all = [REPONSE_SERIES1, REPONSE_SERIES2, REPONSE_SERIES3, 
                    REPONSE_SERIES4, REPONSE_SERIES5, REPONSE_SERIES6, 
                    REPONSE_SERIES7, REPONSE_SERIES8, REPONSE_SERIES9, 
                    REPONSE_SERIES10, REPONSE_SERIES11, REPONSE_SERIES12, 
                    REPONSE_SERIES13, REPONSE_SERIES14, REPONSE_SERIES15, 
                    REPONSE_SERIES16, REPONSE_SERIES17, REPONSE_SERIES18, 
                    REPONSE_SERIES19, REPONSE_SERIES20]
    
    SERIES = []
    RESPONSES = []
    
    for i in range(len(series_all)):
        s = separate_series(series_all[i])
        SERIES.append(s)
        
        r = separate_series(response_all[i])
        RESPONSES.append(r)
    
    return SERIES, RESPONSES


def initialize_directory():
    dirs_to_make = ['Results_TloadDback_TRAINING', 
                    'Results_TloadDback_PRETEST']
    dirs_to_make = ["{}/results/{}".format(os.getcwd(), i) for i in dirs_to_make]
    
    for dir_path in dirs_to_make:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        else:
            print("Directory {} already exists. Skipping...".format(dir_path))
    print("\n\n\n")
    return dirs_to_make


def initialize_files(subject_info: dict):
    dirs_to_make = initialize_directory()
    file_dict = {}
    
    subject = subject_info["subject"]
    cond = subject_info["condition"]
    
    file_dict['Training'] = {"file_path": "{}/TRAINING_{}.csv".format(dirs_to_make[0], subject),
                             "dataframe": pd.DataFrame(columns=['Subject', 
                                                                'Subject_number', 
                                                                'Age', 
                                                                'Sex', 
                                                                'RESPONSE_LETTER', 
                                                                'RESPONSE_NUM',
                                                                'TYPE'])}
    
    file_dict['Pretest'] = {"file_path": "{}/PRETEST_{}.csv".format(dirs_to_make[1], subject),
                            "dataframe": pd.DataFrame(columns=['Subject', 
                                                               'Subject_number',
                                                               'Age',
                                                               'Sex', 
                                                               'PRETEST_HCL',
                                                               'PRETEST_LCL'])}

    return file_dict


def digit_training(subject_info, lines):
    # Show general instructions and digit instructions!
    os.system('cls')
    nums = ['9','1','2','8','4','6','7','8','9','3','1','6','4','2','7','4','1','3','9','2','3','4','1','9','3','6']
    
    for i in nums:
        print_center(i, lines)
        time.sleep(subject_info["stimulus_time_duration_pretest"])
        os.system('cls')
    
    print_center("Well Done! Digits Training Complete", lines)
    time.sleep(2)
    os.system('cls')


def letter_training(subject_info, lines):
    # Show the letter instructions
    letters = [ 'E', 'P', 'P', 'L', 'A', 'P', 'L', 'A', 'A', 'N', 'T', 'N', 'N', 'N', 'U', 'T', 'T', 'P', 'R', 'R' ]
    for i in letters:
        print_center(i, lines)
        time.sleep(subject_info["stimulus_time_duration_pretest"])
        os.system('cls')
        time.sleep(0.1)
        
    print_center("Well Done! Letter Training Complete", lines)
    time.sleep(2)
    os.system('cls')
        
def learning_loop(lines, 
                  SERIES: list, 
                  RESPONSES: list, 
                  subject_info: dict,
                  file_dict: dict):
    performance_holder = 0.4
    STD = subject_info["stimulus_time_duration_pretest"] # set for pretest regardless of user for some reason?
    
    while performance_holder <= 0.85:
        indx = np.random.choice(len(SERIES))
        sequence = SERIES[indx]
        response_ground_truth = RESPONSES[indx]
        
        DISTRIB_R_LETTRE = []
        DISTRIB_R_SERIE = []
        ANSWER_LETTER = [] 
        ANSWER_NUMBER = [] 
        REPONSE_LETTRE_CORR = []
        
        for value in range(len(sequence)):
            print_center(sequence[value], lines)
            
            START_TIME = time.time()
            secs = time.time()
            while secs - START_TIME < STD:  # making a loop
                secs = time.time()
                
                if keyboard.is_pressed("space"):  # space key pressed
                    response_key = "1"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    response_key = "0"
                    continue
                time.sleep(0.001)
            os.system('cls')
            
            
            RESPONSE_LETTER = "0"
            if int(response_key) == int(response_ground_truth[value]):
                RESPONSE_LETTER = "1"
            
            
            ANSWER_LETTER.append(int(RESPONSE_LETTER))
            
            DISTRIB_R_LETTRE.append(int(response_key))
            DISTRIB_R_SERIE.append(int(response_ground_truth[value]))
            
            
            vector = [DISTRIB_R_LETTRE[i] + DISTRIB_R_SERIE[i] for i in range(len(DISTRIB_R_SERIE))]
            
            busq = list(np.where(np.array(vector)==2)[0]) # key pressed at correct location
            busq2 = list(np.where(np.array(DISTRIB_R_SERIE)==1)[0]) # all times key should've been pressed
            
            if len(busq2) == 0:
                ANSWER_LETTER_TYPE1 = 0
            else:
                ANSWER_LETTER_TYPE1 = len(busq)/len(busq2)
                
            # Case 2: Subject did not press the key when they weren't 
            # supposed to press the key.
            busq3 = list(np.where(np.array(vector)==0)[0])  # 2 type of correct answer. no press when do not have to press
            busq4 = list(np.where(np.array(DISTRIB_R_SERIE)==0)[0])   # total of no answers
            
            # No instances of this key, prevent division by zero
            if len(busq4) == 0:
                ANSWER_LETTER_TYPE2 = 0
            else:
                ANSWER_LETTER_TYPE2 = len(busq3)/len(busq4)
            
            # NUMBERS TEST
            # we exclude 5 such that there is an equal number of odd and even
            number_options = [1, 2, 3, 4, 6, 7, 8, 9]
            numbers_choice = np.random.choice(number_options)
            print_center(str(numbers_choice), lines)
            
            START_TIME = time.time()
            secs = time.time()
            while secs - START_TIME < STD:
                secs = time.time()
                # Subject should press 2 for an even number
                if keyboard.is_pressed("2"):  
                    R_NUM = "2"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                # Subject should press 3 for an odd number
                elif keyboard.is_pressed("3"):
                    R_NUM = "3"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    R_NUM = "0"
                    continue
                time.sleep(0.001)
                
            os.system('cls')
            # Random number choice is odd
            if numbers_choice % 2 == 1:
                if R_NUM == "3":
                    RESPONSE_NUM = "1" # Correct entry
                else:
                    RESPONSE_NUM = "0"
            # Random number choice is even
            else: 
                if R_NUM == "2":
                    RESPONSE_NUM = "1"
                else:
                    RESPONSE_NUM = "0"
            ANSWER_NUMBER.append(int(RESPONSE_NUM))
            
            train_row = pd.DataFrame(columns=list(file_dict["Training"]["dataframe"].columns))
            train_row.loc[0, "Subject"] = subject_info["subject"]
            train_row.loc[0, "Subject_number"] = subject_info["subject_number"]
            train_row.loc[0, "Age"] = subject_info["age"]
            train_row.loc[0, "Sex"] = subject_info["sex"]
            train_row.loc[0, "RESPONSE_LETTER"] = RESPONSE_LETTER
            train_row.loc[0, "RESPONSE_NUM"] = RESPONSE_NUM
            train_row.loc[0, "TYPE"] = "learning loop"
            file_dict["Training"]["dataframe"] = pd.concat([file_dict["Training"]["dataframe"], train_row])
            
        ANSWER_LETTER_TOTAL = ANSWER_LETTER_TYPE1*0.65 + ANSWER_LETTER_TYPE2*0.35
        performance_holder = ANSWER_LETTER_TOTAL*0.65 + np.mean(ANSWER_NUMBER)*0.35
        
        if performance_holder > 0.85:
            break
       
        print_center("The training will run again.", lines)
        time.sleep(2)
        os.system('cls')
        print_center("Press the space bar to begin again.", lines)
        break_time = True
        while break_time:
            if keyboard.is_pressed("space"):  # space key pressed
                break_time = False
                time.sleep(1)
                os.system('cls')
                break  # finishing the loop
            else:
                continue
            time.sleep(0.001)
            
    return file_dict
        
    
def pretest_loop(lines, 
                 SERIES: list, 
                 RESPONSES: list, 
                 subject_info: dict,
                 file_dict: dict):
    
    print_center("The real pretest will now begin!", lines)
    time.sleep(2)
    os.system('cls')
    
    STD = subject_info["stimulus_time_duration_pretest"] - 0.1 # decreasing since they could handle 1.5
    
    error = 0
    accumu_error = 0
    PERFORMANCE_TOTAL = []
    PERFORMANCE = 0.99
    
    while PERFORMANCE >= 0.01:
        indx = np.random.choice(len(SERIES))
        sequence = SERIES[indx]
        response_ground_truth = RESPONSES[indx]
        
        DISTRIB_R_LETTRE = []
        DISTRIB_R_SERIE = []
        ANSWER_LETTER = [] 
        ANSWER_NUMBER = [] 
        REPONSE_LETTRE_CORR = []
        
        for value in range(len(sequence)):
            print_center(sequence[value], lines)
            
            START_TIME = time.time()
            secs = time.time()
            while secs - START_TIME < STD:  # making a loop
                secs = time.time()
                
                if keyboard.is_pressed("space"):  # space key pressed
                    response_key = "1"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    response_key = "0"
                    continue
                time.sleep(0.001)
            os.system('cls')
            
            
            RESPONSE_LETTER = "0"
            if int(response_key) == int(response_ground_truth[value]):
                RESPONSE_LETTER = "1"
            
            
            ANSWER_LETTER.append(int(RESPONSE_LETTER))
            
            DISTRIB_R_LETTRE.append(int(response_key))
            DISTRIB_R_SERIE.append(int(response_ground_truth[value]))
            
            
            vector = [DISTRIB_R_LETTRE[i] + DISTRIB_R_SERIE[i] for i in range(len(DISTRIB_R_SERIE))]
            
            busq = list(np.where(np.array(vector)==2)[0]) # key pressed at correct location
            busq2 = list(np.where(np.array(DISTRIB_R_SERIE)==1)[0]) # all times key should've been pressed
            
            if len(busq2) == 0:
                ANSWER_LETTER_TYPE1 = 0
            else:
                ANSWER_LETTER_TYPE1 = len(busq)/len(busq2)
                
            # Case 2: Subject did not press the key when they weren't 
            # supposed to press the key.
            busq3 = list(np.where(np.array(vector)==0)[0])  # 2 type of correct answer. no press when do not have to press
            busq4 = list(np.where(np.array(DISTRIB_R_SERIE)==0)[0])   # total of no answers
            
            # No instances of this key, prevent division by zero
            if len(busq4) == 0:
                ANSWER_LETTER_TYPE2 = 0
            else:
                ANSWER_LETTER_TYPE2 = len(busq3)/len(busq4)
            
            # NUMBERS TEST
            # we exclude 5 such that there is an equal number of odd and even
            number_options = [1, 2, 3, 4, 6, 7, 8, 9]
            numbers_choice = np.random.choice(number_options)
            print_center(str(numbers_choice), lines)
            
            START_TIME = time.time()
            secs = time.time()
            while secs - START_TIME < STD:
                secs = time.time()
                # Subject should press 2 for an even number
                if keyboard.is_pressed("2"):  
                    R_NUM = "2"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                # Subject should press 3 for an odd number
                elif keyboard.is_pressed("3"):
                    R_NUM = "3"
                    time.sleep(STD+START_TIME-secs)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    R_NUM = "0"
                    continue
                time.sleep(0.001)
                
            os.system('cls')
            # Random number choice is odd
            if numbers_choice % 2 == 1:
                if R_NUM == "3":
                    RESPONSE_NUM = "1" # Correct entry
                else:
                    RESPONSE_NUM = "0"
            # Random number choice is even
            else: 
                if R_NUM == "2":
                    RESPONSE_NUM = "1"
                else:
                    RESPONSE_NUM = "0"
            ANSWER_NUMBER.append(int(RESPONSE_NUM))
            
            train_row = pd.DataFrame(columns=list(file_dict["Training"]["dataframe"].columns))
            train_row.loc[0, "Subject"] = subject_info["subject"]
            train_row.loc[0, "Subject_number"] = subject_info["subject_number"]
            train_row.loc[0, "Age"] = subject_info["age"]
            train_row.loc[0, "Sex"] = subject_info["sex"]
            train_row.loc[0, "RESPONSE_LETTER"] = RESPONSE_LETTER
            train_row.loc[0, "RESPONSE_NUM"] = RESPONSE_NUM
            train_row.loc[0, "TYPE"] = "pretest loop"
            file_dict["Training"]["dataframe"] = pd.concat([file_dict["Training"]["dataframe"], train_row])
            
        ANSWER_LETTER_TOTAL = ANSWER_LETTER_TYPE1*0.65 + ANSWER_LETTER_TYPE2*0.35
        PERFORMANCE = ANSWER_LETTER_TOTAL*0.65 + np.mean(ANSWER_NUMBER)*0.35
        
        PERFORMANCE_TOTAL.append(PERFORMANCE)
        
        if PERFORMANCE < 0.85:
            error += 1
            print_center("ERROR: {}".format(error), lines)
            accumu_error += 1
            print_center("ACCUM: {}".format(accumu_error), lines)
            STD = STD #STD does not increase --> repeat block
            print_center("STD: {}".format(STD), lines)
            time.sleep(5)
            
            os.system('cls')
            print_center("Let's take a break.", lines)
            time.sleep(2)
            os.system('cls')
            print_center("Press the space bar to begin again when you're ready.", lines)
            break_time = True
            while break_time:
                if keyboard.is_pressed("space"):  # space key pressed
                    break_time = False
                    time.sleep(1)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    continue
                time.sleep(0.001)
            
        else:
            STD = STD - 0.10
            #STD = round(STD/cycleRefresh)*cycleRefresh; % To adapt the STD at the screen refreshing rate
            error = 0
            print_center("ERROR: {}".format(error), lines)
            print_center("ACCUM: {}".format(accumu_error), lines)
            print_center("STD: {}".format(STD), lines)
            time.sleep(5)
            print_center("Let's take a break.", lines)
            time.sleep(2)
            os.system('cls')
            print_center("Press the space bar to begin again when you're ready.", lines)
            break_time = True
            while break_time:
                if keyboard.is_pressed("space"):  # space key pressed
                    break_time = False
                    time.sleep(1)
                    os.system('cls')
                    break  # finishing the loop
                else:
                    continue
                time.sleep(0.001)
            
        # Loop repetition
        if error == 3: # they couldn't perform at this STD, so revert to previous
            PRETEST_HCL = STD + 0.10
            PRETEST_LCL = PRETEST_HCL + 0.5*PRETEST_HCL
            break
        
        if accumu_error == 3: # Although this value is fixed to 3 in Borragan & Slama,2017, increasing it at 5 might increase the pretest calibration
            PRETEST_HCL = STD
            PRETEST_LCL = PRETEST_HCL + 0.5*PRETEST_HCL
            break
    
    pre_row = pd.DataFrame(columns=list(file_dict["Pretest"]["dataframe"].columns))
    pre_row.loc[0, "Subject"] = subject_info["subject"]
    pre_row.loc[0, "Subject_number"] = subject_info["subject_number"]
    pre_row.loc[0, "Age"] = subject_info["age"]
    pre_row.loc[0, "Sex"] = subject_info["sex"]
    pre_row.loc[0, "PRETEST_HCL"] = PRETEST_HCL
    pre_row.loc[0, "PRETEST_LCL"] = PRETEST_LCL
    file_dict["Pretest"]["dataframe"] = pd.concat([file_dict["Pretest"]["dataframe"], pre_row])
    return file_dict
    
    
    
def main():
    set_font_size()
    cols, lines = maximize_console()
    os.system('cls')
    with open("configs/test_settings.yaml", 'r') as stream:
        subject_info = yaml.safe_load(stream)
        
    file_dict = initialize_files(subject_info)
    SERIES, RESPONSES = make_series_list()
        
    os.system('cls')
    print_center("Let's Begin!", lines)
    time.sleep(2)
    os.system('cls')
    display_instruction(image_path=r"images\pretest\General_Instructions_REMADE.bmp")
    display_instruction(image_path=r"images\pretest\Digits_Instructions_REMADE.bmp")
    os.system('cls')
    print_center("Digits Training is Beginning...", lines)
    time.sleep(3)
    os.system('cls')
    digit_training(subject_info, lines)
    
    display_instruction(image_path=r"images\pretest\Letters_Instructions_REMADE.bmp")
    os.system('cls')
    print_center("Letter Training is Beginning...", lines)
    time.sleep(3)
    os.system('cls')
    letter_training(subject_info, lines)
    
    # Allow the subject to learn the task
    display_instruction(image_path=r"images\pretest\Letters_Digits_Instructions_REMADE.bmp")
    os.system('cls')
    print_center("Letter and Digits Training is Beginning...", lines)
    time.sleep(3)
    os.system('cls')
    file_dict = learning_loop(lines, SERIES, RESPONSES, subject_info, file_dict)
    file_dict = pretest_loop(lines, SERIES, RESPONSES, subject_info, file_dict)
    
    for key in file_dict.keys():
        df = file_dict[key]["dataframe"]
        df.to_csv(file_dict[key]["file_path"])





if __name__ == "__main__":
    main()


