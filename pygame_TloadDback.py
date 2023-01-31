# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:24:43 2023

@author: Rose.Alyssa
"""

import pygame
import sys
import os
import pandas as pd
import yaml
import time
import numpy as np
import keyboard
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

series11        = [ 'A'  'L'  'R'  'R'  'T'  'U'  'C'  'U'  'U'  'U'  'U'  'A'  'E'  'A'  'P'  'P'  'R'  'N'  'N'  'L'  'C'  'E'  'E'  'R'  'R'  'L'  'U'  'U'  'E'  'E' ]
REPONSE_SERIES11= [ '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '1'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1' ]

series12        = [ 'T'  'C'  'C'  'A'  'A'  'T'  'L'  'L'  'E'  'U'  'P'  'P'  'A'  'A'  'T'  'T'  'N'  'E'  'U'  'U'  'R'  'A'  'C'  'T'  'L'  'L'  'L'  'U'  'P'  'P' ]
REPONSE_SERIES12= [ '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '0'  '1'  '1'  '0'  '0'  '1' ]

series13        = [ 'A'  'A'  'R'  'R'  'T'  'U'  'U'  'E'  'E'  'N'  'P'  'A'  'A'  'A'  'P'  'T'  'T'  'T'  'N'  'N'  'C'  'E'  'N'  'N'  'P'  'L'  'U'  'C'  'C'  'C' ]
REPONSE_SERIES13= [ '0'  '1'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0' ]

series14        = [ 'E'  'E'  'T'  'A'  'U'  'U'  'T'  'R'  'R'  'R'  'L'  'L'  'U'  'E'  'T'  'P'  'P'  'A'  'L'  'P'  'A'  'A'  'C'  'A'  'A'  'C'  'C'  'N'  'R'  'R' ]
REPONSE_SERIES14= [ '0'  '1'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '1'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '0'  '0'  '1'  '0'  '0'  '1'  '0'  '1'  '0'  '0'  '1' ]

series15        = [ 'U'  'C'  'R'  'R'  'C'  'C'  'L'  'N'  'N'  'U'  'U'  'R'  'A'  'A'  'T'  'L'  'L'  'E'  'U'  'U'  'R'  'A'  'C'  'T'  'T'  'N'  'N'  'U'  'U'  'E' ]
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

class TloadTest():
    def __init__(self):
        self.SERIES = []
        self.RESPONSES = []
        
        with open("configs/test_settings.yaml", 'r') as stream:
            self.subject_info = yaml.safe_load(stream)
            
        pretest_conditions = pd.read_csv("{}/results/Results_TloadDback_PRETEST/PRETEST_{}.csv".format(os.getcwd(), self.subject_info["subject"]))
        if self.subject_info["condition"] == "HCL":
            self.subject_info["stimulus_time_duration"] = pretest_conditions["PRETEST_HCL"][0]
        else:
            self.subject_info["stimulus_time_duration"] = pretest_conditions["PRETEST_LCL"][0]
            
        # self.repetitions = round(16/self.subject_info["stimulus_time_duration"])
        self.make_series_list()
        self.initialize_directory()
        self.initialize_files()
        
    def separate_series(self, series: list):
        split_series = []
        for i in series[0]: 
            split_series.append(i)
            
        return split_series
    
    def make_series_list(self):
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

        for i in range(len(series_all)):
            s = self.separate_series(series_all[i])
            self.SERIES.append(s)
            
            r = self.separate_series(response_all[i])
            self.RESPONSES.append(r)
            
    def initialize_directory(self):
        dirs_to_make = ['Results_TloadDback_R_given', 
                        'Results_TloadDback_Performance',
                        'Results_TloadDback_Performance_Type_answer',
                        'Results_TloadDback_Performance_RTs',
                        'Results_TloadDback_Performance_Time']
        dirs_to_make = ["{}/results/{}".format(os.getcwd(), i) for i in dirs_to_make]
        
        if not os.path.isdir("{}/results".format(os.getcwd())):
            os.mkdir("{}/results".format(os.getcwd()))
            
        for dir_path in dirs_to_make:
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
        self.dirs = dirs_to_make


    def initialize_files(self):
        file_dict = {}
        
        subject = self.subject_info["subject"]
        cond = self.subject_info["condition"]
        
        file_dict["R_given"] = {"file_path": "{}/TloadDback_REPONSES_TASK_{}_{}.csv".format(self.dirs[0], subject, cond),
                                "dataframe": pd.DataFrame(columns=['subject', 
                                                                   'subject_number', 
                                                                   'age', 
                                                                   'sex',  
                                                                   'letter_shown', 
                                                                   'num_shown', 
                                                                   'response_letter', 
                                                                   'is_correct_letter',
                                                                   'response_num',
                                                                   'is_correct_num'])}
        
        file_dict["Performance"] = {"file_path": "{}/TloadDback_PERFORMANCE_TASK_{}_{}.csv".format(self.dirs[1], subject, cond),
                                    "dataframe": pd.DataFrame(columns=['subject', 
                                                                       'subject_number',
                                                                       'age',
                                                                       'sex', 
                                                                       'performance'])}
        
        file_dict["Performance_Type_answer"] = {"file_path": "{}/TloadDback_PERF_by_TofR_TASK_{}_{}.csv".format(self.dirs[2], subject, cond),
                                                "dataframe": pd.DataFrame(columns=['subject', 
                                                                                   'Correct_answer', 
                                                                                   'Correct_omSTDon', 
                                                                                   'OmSTDon', 
                                                                                   'FAs',
                                                                                   'Correct_answerNUM'])}
        
        file_dict["Performance_RTs"] = {"file_path": "{}/TloadDback_RTs_TASK_{}_{}.csv".format(self.dirs[3], subject, cond),
                                        "dataframe": pd.DataFrame(columns=['subject', 
                                                                           'Answer_Letter',
                                                                           'Given_Letter',
                                                                           'is_correct_letter',
                                                                           'RTs_Letter',
                                                                           'Shown_Num',
                                                                           'Given_Num', 
                                                                           'is_correct_num',
                                                                           'RTs_Num'])}
        
        file_dict["Performance_Time"] = {"file_path": "{}/BEGXP_ENDXP_{}_{}.csv".format(self.dirs[4], subject, cond),
                                         "dataframe": pd.DataFrame(columns=['subject', 
                                                                            'start_time',
                                                                            'end_time',
                                                                            'total_time'])}
        
        self.file_dict = file_dict
    
    def render_centered_text(self, text):
        # first, split the text into words
        words = text.split()
        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = self.font.size(' '.join(line_words + words[:1]))
                if fw > self.SCREEN_X_CENTER:
                    break
    
            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)
    
        # now we've split our text into lines that fit into the width, actually
        # render them
    
        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = self.font.size(line)
    
            # (tx, ty) is the top-left of the font surface
            tx = self.SCREEN_X_CENTER - fw / 2
            ty = self.SCREEN_Y_CENTER + y_offset
    
            font_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(font_surface, (tx, ty))
    
            y_offset += fh
        pygame.display.flip()
        
    def display_one_instruction(self, image_path):
        img = pygame.image.load_basic(image_path)
        img_rect = img.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(img, img_rect)
        pygame.display.flip()
        
        display_instr = True
        while display_instr:
            # Keep displaying the image until the space bar is pressed!
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen.fill((0, 0, 0))
                        display_instr = False
            time.sleep(0.001)
        # to prevent overly fast screen changes between instructions
        time.sleep(0.5)
        
        
    def test_sequence(self):
        RTsLet = []
        PERC_time_appui_TOTLet = []
        RTsNum = []
        PERC_time_appui_TOTNum = []
        
        PERFORMANCE = 0.3
        items_num = []
        items_let = []
        ANSWER_LETTER_TYPE1 = []    # press when have to press  70 % over 100% of ANSWER_LETTER
        ANSWER_LETTER_TYPE2 = []    # no press when do not have to press 30% over 100% of ANSWER_LETTER
        PERFORMANCE_TOTAL = []   
        
        BEGIN_TIME = time.time()
        for rep in range(self.subject_info["test_reps"]):
            indx = np.random.choice(len(self.SERIES))
            sequence = self.SERIES[indx]
            response_ground_truth = self.RESPONSES[indx]
            
            ANSWER_LETTER = [] 
            ANSWER_NUMBER = [] 
            REPONSE_LETTER_CORR = []
            
            DISTRIB_R_LETTRE = []
            DISTRIB_R_SERIE = []
            
            
            self.render_centered_text("STARTING TEST SEQUENCE...")
            time.sleep(3)
            self.screen.fill((0, 0, 0))
            
            
            for value in range(len(sequence)):
                self.render_centered_text(sequence[value])
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < self.subject_info["stimulus_time_duration"]:  # making a loop
                    secs = time.time()
                    
                    if keyboard.is_pressed("space"):  # space key pressed
                        response_key = "1"
                        time.sleep(self.subject_info["stimulus_time_duration"]+START_TIME-secs)
                        self.screen.fill((0, 0, 0))
                        break  # finishing the loop
                    else:
                        response_key = "0"
                        continue
                    time.sleep(0.001)
                    
                    
                self.screen.fill((0, 0, 0))
                
                # Record response time
                RTsLet.append(secs-START_TIME)
                time_appuiLet = secs-START_TIME
                PERC_time_appuiLet = time_appuiLet/self.subject_info["stimulus_time_duration"]
                PERC_time_appui_TOTLet.append(PERC_time_appuiLet)
                
                # Check for correct response
                RESPONSE_LETTER = "0"
                if int(response_key) == int(response_ground_truth[value]):
                    RESPONSE_LETTER = "1"
                
                
                
                ANSWER_LETTER.append(int(RESPONSE_LETTER))
                
                DISTRIB_R_LETTRE.append(int(response_key))
                DISTRIB_R_SERIE.append(int(response_ground_truth[value]))
                
                vector = [DISTRIB_R_LETTRE[i] + DISTRIB_R_SERIE[i] for i in range(len(DISTRIB_R_SERIE))]
                
                # Find all the possible correct answers
                
                # Case 1: Space bar pressed when it should've been pressed.
                busq = list(np.where(np.array(vector)==2)[0]) # key pressed at correct location
                busq2 = list(np.where(np.array(DISTRIB_R_SERIE)==1)[0]) # all times key should've been pressed
                
                # No instances of this key, prevent division by zero
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
                
                # Errors
                
                # Case 1: They should've pressed space but didn't within the
                # allotted time.
                busq5a = list(np.where(np.array(DISTRIB_R_SERIE) > np.array(DISTRIB_R_LETTRE))[0])
                busq5b = list(np.where(np.array(DISTRIB_R_SERIE)==1)[0])
                if len(busq5b) == 0:
                    ANSWER_LETTER_TYPE3 = 0
                else:
                    ANSWER_LETTER_TYPE3 = len(busq5a)/len(busq5b)
                
                # Case 2: They pressed space when they weren't supposed to
                busq6a = list(np.where(np.array(DISTRIB_R_SERIE) < np.array(DISTRIB_R_LETTRE))[0])
                busq6b = list(np.where(np.array(DISTRIB_R_SERIE)==0)[0])
                
                if len(busq6b) == 0:
                    ANSWER_LETTER_TYPE4 = 0
                else:
                    ANSWER_LETTER_TYPE4 = len(busq6a)/len(busq6b)
                
                # *************************************************************** #
                # *************************************************************** #
                # *************************************************************** #
                # NUMBERS TEST
                # we exclude 5 such that there is an equal number of odd and even
                number_options = [1, 2, 3, 4, 6, 7, 8, 9]
                numbers_choice = np.random.choice(number_options)
                self.render_centered_text(str(numbers_choice))
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < self.subject_info["stimulus_time_duration"]:
                    secs = time.time()
                    # Subject should press 2 for an even number
                    if keyboard.is_pressed("2"):  
                        R_NUM = "2"
                        time.sleep(self.subject_info["stimulus_time_duration"]+START_TIME-secs)
                        self.screen.fill((0, 0, 0))
                        break  # finishing the loop
                    # Subject should press 3 for an odd number
                    elif keyboard.is_pressed("3"):
                        R_NUM = "3"
                        time.sleep(self.subject_info["stimulus_time_duration"]+START_TIME-secs)
                        self.screen.fill((0, 0, 0))
                        break  # finishing the loop
                    else:
                        R_NUM = "0"
                        continue
                    time.sleep(0.001)
                    
                self.screen.fill((0, 0, 0))
                
                RTsNum.append(secs-START_TIME)
                time_appuiNum = secs-START_TIME
                PERC_time_appuiNum = time_appuiNum/self.subject_info["stimulus_time_duration"]
                PERC_time_appui_TOTNum.append(PERC_time_appuiNum)
                
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
                
            
                
                # Registering the items presented
                items_let.append(sequence[value])
                items_num.append(numbers_choice)
                
                # R GIVEN
                r_given_row = pd.DataFrame(columns=list(self.file_dict["R_given"]["dataframe"].columns))
                r_given_row.loc[0, "subject"] = self.subject_info["subject"]
                r_given_row.loc[0, "subject_number"] = self.subject_info["subject_number"]
                r_given_row.loc[0, "age"] = self.subject_info["age"]
                r_given_row.loc[0, "sex"] = self.subject_info["sex"]
                r_given_row.loc[0, "letter_shown"] = sequence[value]
                r_given_row.loc[0, "num_shown"] = numbers_choice
                r_given_row.loc[0, "response_letter"] = response_key
                r_given_row.loc[0, "is_correct_letter"] = RESPONSE_LETTER
                r_given_row.loc[0, "response_num"] = R_NUM
                r_given_row.loc[0, "is_correct_num"] = RESPONSE_NUM
                self.file_dict["R_given"]["dataframe"] = pd.concat([self.file_dict["R_given"]["dataframe"], r_given_row])
                
                
                # PERFORMANCE RTS
                perf_rts_row = pd.DataFrame(columns=list(self.file_dict["Performance_RTs"]["dataframe"].columns))
                perf_rts_row.loc[0, "subject"] = self.subject_info["subject"]
                perf_rts_row.loc[0, "Answer_Letter"] = response_ground_truth[value]
                perf_rts_row.loc[0, "Given_Letter"] = response_key
                perf_rts_row.loc[0, "is_correct_letter"] = RESPONSE_LETTER
                perf_rts_row.loc[0, "RTs_Letter"] = PERC_time_appuiLet
                perf_rts_row.loc[0, "Shown_Num"] = numbers_choice
                perf_rts_row.loc[0, "Given_Num"] = R_NUM
                perf_rts_row.loc[0, "is_correct_num"] = RESPONSE_NUM
                perf_rts_row.loc[0, "RTs_Num"] = PERC_time_appuiNum
                self.file_dict["Performance_RTs"]["dataframe"] = pd.concat([self.file_dict["Performance_RTs"]["dataframe"], perf_rts_row])
                
                
                
                ANSWER_LETTER_TOTAL = ANSWER_LETTER_TYPE1*0.65 + ANSWER_LETTER_TYPE2*0.35
                PERFORMANCE = ANSWER_LETTER_TOTAL*0.65 + np.mean(ANSWER_NUMBER)*0.35
                TOT_NUM = np.mean(ANSWER_NUMBER)
            
            
            PERFORMANCE_TOTAL.append(PERFORMANCE)
            
            # PERFORMANCE
            perf_row = pd.DataFrame(columns=list(self.file_dict["Performance"]["dataframe"].columns))
            perf_row.loc[0, "subject"] = self.subject_info["subject"]
            perf_row.loc[0, "subject_number"] = self.subject_info["subject_number"]
            perf_row.loc[0, "age"] = self.subject_info["age"]
            perf_row.loc[0, "sex"] = self.subject_info["sex"]
            perf_row.loc[0, "performance"] = PERFORMANCE
            self.file_dict["Performance"]["dataframe"] = pd.concat([self.file_dict["Performance"]["dataframe"], perf_row])
            
            
            # PERFORMANCE_TYPE_ANSWER
            perf_type_row = pd.DataFrame(columns=list(self.file_dict["Performance_Type_answer"]["dataframe"].columns))
            perf_type_row.loc[0, "subject"] = self.subject_info["subject"]
            perf_type_row.loc[0, "Correct_answer"] = ANSWER_LETTER_TYPE1
            perf_type_row.loc[0, "Correct_omSTDon"] = ANSWER_LETTER_TYPE2
            perf_type_row.loc[0, "OmSTDon"] = ANSWER_LETTER_TYPE3
            perf_type_row.loc[0, "FAs"] = ANSWER_LETTER_TYPE4
            perf_type_row.loc[0, "Correct_answerNUM"] = TOT_NUM
            self.file_dict["Performance_Type_answer"]["dataframe"] = pd.concat([self.file_dict["Performance_Type_answer"]["dataframe"], perf_type_row])
            
        self.screen.fill((0, 0, 0))
        END_TIME = time.time()  
        time_row = pd.DataFrame(columns=list(self.file_dict["Performance_Time"]["dataframe"].columns))
        time_row.loc[0, "subject"] = self.subject_info["subject"]
        time_row.loc[0, "start_time"] = str(datetime.datetime.fromtimestamp(BEGIN_TIME))
        time_row.loc[0, "end_time"] = str(datetime.datetime.fromtimestamp(END_TIME))
        time_row.loc[0, "total_time"] = END_TIME - BEGIN_TIME
        self.file_dict["Performance_Time"]["dataframe"] = pd.concat([self.file_dict["Performance_Time"]["dataframe"], time_row])
        
        
    def run_game(self):
        # Initializing the game parameters
        pygame.init()
        w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.font = pygame.font.Font(pygame.font.match_font('verdana'), 50)
        self.screen = pygame.display.set_mode(size=(w, h))
        self.SCREEN_X_CENTER, self.SCREEN_Y_CENTER = self.screen.get_rect().center
        
        
        text = "Let's Begin!"
        self.render_centered_text(text)
        time.sleep(2)
        self.screen.fill((0, 0, 0))
        
        self.display_one_instruction(r"images\test\Instructions_1_REMADE.bmp")
        self.display_one_instruction(r"images\test\Instructions_2_REMADE.bmp")
        self.display_one_instruction(r"images\test\Instructions_3_REMADE.bmp")
        
        self.test_sequence()
        
        for key in self.file_dict.keys():
            df = self.file_dict[key]["dataframe"]
            df.to_csv(self.file_dict[key]["file_path"], index=False)

        
        pygame.quit()
        sys.exit(0)
        
if __name__ == "__main__":
    test = TloadTest()
    test.run_game()
        