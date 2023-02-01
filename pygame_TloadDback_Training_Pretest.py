# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:20:11 2023

Author: Alyssa Bekai Rose

This script runs the TloadDback pretest as specified with minimal modifications
in Borragan et al. (2017). The original code was implemented in MATLAB, found
here: https://osf.io/ay6er/, and converted to Python in a pygame format.

The pretest and test have only been tested on a Windows 10 OS.
"""

import pygame
import sys
import os
import pandas as pd
import yaml
import time
import numpy as np
import keyboard

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


class TloadPretest():
    """ 
    This class contains all functions and methods required
    for conducting the TloadDback pretest as outlined in Borragan et al. (2017)
    """
    def __init__(self):
        self.SERIES = []
        self.RESPONSES = []
        
        with open("configs/test_settings.yaml", 'r') as stream:
            self.subject_info = yaml.safe_load(stream)
            
        
        self.make_series_list()
        self.initialize_directory()
        self.initialize_files()
        
    def check_kill(self):
        """
        Checks if kill key pressed, and kills the game if yes.

        Returns
        -------
        None.

        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit(0)
        
    def separate_series(self, series: list):
        """
        Formats the series and responses into Pythonic lists.
        
        This function should not be called directly.

        Parameters
        ----------
        series : list
            Series or response list as seen above.

        Returns
        -------
        split_series : list
            The series or response in a Pythonic form list.

        """
        split_series = []
        for i in series[0]: 
            split_series.append(i)
            
        return split_series
    
    
    def make_series_list(self):
        """
        Converts the above series and responses into Pythonic lists.
        
        This function should not be called directly.
        
        Returns
        -------
        None.

        """
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
        """
        Initializes the directories needed for the pretest data.

        Returns
        -------
        None.

        """
        dirs_to_make = ['Results_TloadDback_TRAINING', 
                        'Results_TloadDback_PRETEST']
        dirs_to_make = ["results/{}".format(os.getcwd(), i) for i in dirs_to_make]
        
        if not os.path.isdir("results"):
            os.mkdir("results")
            
        for dir_path in dirs_to_make:
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
            else:
                print("Directory {} already exists. Skipping...".format(dir_path))
        self.dirs = dirs_to_make
    
    
    def initialize_files(self):
        """
        Initializes all of the dataframes which correspond to different CSV
        data sheets.

        Returns
        -------
        None.

        """
        file_dict = {}
        
        subject = self.subject_info["subject"]
        cond = self.subject_info["condition"]
        
        file_dict['Training'] = {"file_path": "{}/TRAINING_{}.csv".format(self.dirs[0], subject),
                                 "dataframe": pd.DataFrame(columns=['Subject', 
                                                                    'Subject_number', 
                                                                    'Age', 
                                                                    'Sex', 
                                                                    'RESPONSE_LETTER', 
                                                                    'RESPONSE_NUM',
                                                                    'TYPE'])}
        
        file_dict['Pretest'] = {"file_path": "{}/PRETEST_{}.csv".format(self.dirs[1], subject),
                                "dataframe": pd.DataFrame(columns=['Subject', 
                                                                   'Subject_number',
                                                                   'Age',
                                                                   'Sex', 
                                                                   'PRETEST_HCL',
                                                                   'PRETEST_LCL'])}
    
        self.file_dict = file_dict
        
    
    
    
    
    def display_one_instruction(self, image_path: str):
        """
        Displays the .BMP instruction files.

        Parameters
        ----------
        image_path : str
            Path to the location of the image. All instruction images should
            be stored in the 'images' subfolder.

        Returns
        -------
        None.

        """
        wait_condition = keyboard.is_pressed("y")
        while wait_condition:
            wait_condition = keyboard.is_pressed("y")
            time.sleep(0.001)
            
        img = pygame.image.load_basic(image_path)
        img_rect = img.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(img, img_rect)
        pygame.display.flip()
        
        display_instr = True
        while display_instr:
            self.check_kill()
            # Keep displaying the image until the space bar is pressed!
            if keyboard.is_pressed("y"):  # space key pressed
                display_instr = False
                break  # finishing the loop
            else:
                continue
            time.sleep(0.001)
        # to prevent overly fast screen changes between instructions
        time.sleep(0.5)
        self.screen.fill((0, 0, 0))  
        self.render_centered_text('')
        
        
    def render_centered_text(self, text: str):
        """
        Prints text to the center of the screen.

        Parameters
        ----------
        text : str
            The text to display

        Returns
        -------
        None.

        """
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
        
    
    def digit_training(self):
        """
        Runs the digits (pre) pre-test learning loop.

        Returns
        -------
        None.

        """
        # Show general instructions and digit instructions!
        nums = ['9','1','2','8','4','6','7','8','9','3','1','6']
        
        for i in nums:
            self.check_kill()
            self.render_centered_text(i)
            time.sleep(self.subject_info["stimulus_time_duration_pretest"])
            self.screen.fill((0, 0, 0))
            self.render_centered_text('')
            time.sleep(0.1)
        
        self.render_centered_text("Well Done! Digits Training Complete")
        time.sleep(2)
        self.screen.fill((0, 0, 0))
    
    
    def letter_training(self):
        """
        Runs the letters (pre) pre-test learning loop.

        Returns
        -------
        None.

        """
        # Show the letter instructions
        letters = [ 'E', 'P', 'P', 'L', 'A', 'P', 'L', 'A', 'A', 'N', 'T', 'N', 'N', 'N', 'U', 'T', 'T', 'P', 'R', 'R' ]
        for i in letters:
            self.check_kill()
            self.render_centered_text(i)
            time.sleep(self.subject_info["stimulus_time_duration_pretest"])
            self.screen.fill((0, 0, 0))
            self.render_centered_text('')

            time.sleep(0.1)
            
        self.render_centered_text("Well Done! Letter Training Complete")
        
        time.sleep(2)
        self.screen.fill((0, 0, 0))              
       
        
    def learning_loop(self):
        """
        Runs the digits and letters (pre) pre-test learning loop. The subject
        must meet at least an 85% performance value to continue to the 
        actual pretest.

        Returns
        -------
        None.

        """
        performance_holder = 0.4
        STD = self.subject_info["stimulus_time_duration_pretest"] # set for pretest regardless of user for some reason?
        
        while performance_holder <= 0.85:
            indx = np.random.choice(len(self.SERIES))
            sequence = self.SERIES[indx]
            response_ground_truth = self.RESPONSES[indx]
            
            DISTRIB_R_LETTRE = []
            DISTRIB_R_SERIE = []
            ANSWER_LETTER = [] 
            ANSWER_NUMBER = [] 
            REPONSE_LETTRE_CORR = []
            
            for value in range(len(sequence)):
                self.render_centered_text(sequence[value])
                self.check_kill()
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < STD:  # making a loop
                    secs = time.time()
                    
                    if keyboard.is_pressed("space"):  # space key pressed
                        response_key = "1"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        self.render_centered_text('')

                        break  # finishing the loop
                    else:
                        response_key = "0"
                        continue
                    time.sleep(0.001)
                self.screen.fill((0, 0, 0))  
                self.render_centered_text('')

                
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
                self.render_centered_text(str(numbers_choice))
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < STD:
                    secs = time.time()
                    # Subject should press 2 for an even number
                    if keyboard.is_pressed("2"):  
                        R_NUM = "2"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        break  # finishing the loop
                    # Subject should press 3 for an odd number
                    elif keyboard.is_pressed("3"):
                        R_NUM = "3"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        break  # finishing the loop
                    else:
                        R_NUM = "0"
                        continue
                    time.sleep(0.001)
                    
                self.screen.fill((0, 0, 0))  
                self.render_centered_text('')
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
                
                train_row = pd.DataFrame(columns=list(self.file_dict["Training"]["dataframe"].columns))
                train_row.loc[0, "Subject"] = self.subject_info["subject"]
                train_row.loc[0, "Subject_number"] = self.subject_info["subject_number"]
                train_row.loc[0, "Age"] = self.subject_info["age"]
                train_row.loc[0, "Sex"] = self.subject_info["sex"]
                train_row.loc[0, "RESPONSE_LETTER"] = RESPONSE_LETTER
                train_row.loc[0, "RESPONSE_NUM"] = RESPONSE_NUM
                train_row.loc[0, "TYPE"] = "learning loop"
                self.file_dict["Training"]["dataframe"] = pd.concat([self.file_dict["Training"]["dataframe"], train_row])
                
            ANSWER_LETTER_TOTAL = ANSWER_LETTER_TYPE1*0.65 + ANSWER_LETTER_TYPE2*0.35
            performance_holder = ANSWER_LETTER_TOTAL*0.65 + np.mean(ANSWER_NUMBER)*0.35
            
            if performance_holder > 0.85:
                break
           
            self.render_centered_text("The training will run again.")
            
            time.sleep(2)
            self.screen.fill((0, 0, 0))  
            self.render_centered_text("Press 'Y' to begin again.")
            
            break_time = True
            while break_time:
                if keyboard.is_pressed("y"):  # space key pressed
                    break_time = False
                    time.sleep(1)
                    self.screen.fill((0, 0, 0))  
                    break  # finishing the loop
                else:
                    continue
                time.sleep(0.001)
               
    def pretest_loop(self): 
        """
        The actual pretest. This test determines the HCL and LCL stimulus time
        duration values for the subject. As the subject continues to meet 
        a performance threshhold of 85%, the stimulus time duration decreases.

        Returns
        -------
        None.

        """
        self.render_centered_text("The real pretest will now begin!")
        time.sleep(2)
        self.screen.fill((0, 0, 0)) 
        
        STD = self.subject_info["stimulus_time_duration_pretest"] - 0.1 # decreasing since they could handle 1.5
        
        error = 0
        accumu_error = 0
        PERFORMANCE_TOTAL = []
        PERFORMANCE = 0.99
        
        while PERFORMANCE >= 0.01:
            indx = np.random.choice(len(self.SERIES))
            sequence = self.SERIES[indx]
            response_ground_truth = self.RESPONSES[indx]
            
            DISTRIB_R_LETTRE = []
            DISTRIB_R_SERIE = []
            ANSWER_LETTER = [] 
            ANSWER_NUMBER = [] 
            REPONSE_LETTRE_CORR = []
            
            for value in range(len(sequence)):
                self.check_kill()
                self.render_centered_text(sequence[value])
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < STD:  # making a loop
                    secs = time.time()
                    
                    if keyboard.is_pressed("space"):  # space key pressed
                        response_key = "1"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        break  # finishing the loop
                    else:
                        response_key = "0"
                        continue
                    time.sleep(0.001)
                self.screen.fill((0, 0, 0))  
                self.render_centered_text('')
                
                
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
                self.render_centered_text(str(numbers_choice))
                
                START_TIME = time.time()
                secs = time.time()
                while secs - START_TIME < STD:
                    secs = time.time()
                    # Subject should press 2 for an even number
                    if keyboard.is_pressed("2"):  
                        R_NUM = "2"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        break  # finishing the loop
                    # Subject should press 3 for an odd number
                    elif keyboard.is_pressed("3"):
                        R_NUM = "3"
                        time.sleep(STD+START_TIME-secs)
                        self.screen.fill((0, 0, 0))  
                        break  # finishing the loop
                    else:
                        R_NUM = "0"
                        continue
                    time.sleep(0.001)
                    
                self.screen.fill((0, 0, 0))  
                self.render_centered_text('')
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
                
                train_row = pd.DataFrame(columns=list(self.file_dict["Training"]["dataframe"].columns))
                train_row.loc[0, "Subject"] = self.subject_info["subject"]
                train_row.loc[0, "Subject_number"] = self.subject_info["subject_number"]
                train_row.loc[0, "Age"] = self.subject_info["age"]
                train_row.loc[0, "Sex"] = self.subject_info["sex"]
                train_row.loc[0, "RESPONSE_LETTER"] = RESPONSE_LETTER
                train_row.loc[0, "RESPONSE_NUM"] = RESPONSE_NUM
                train_row.loc[0, "TYPE"] = "pretest loop"
                self.file_dict["Training"]["dataframe"] = pd.concat([self.file_dict["Training"]["dataframe"], train_row])
                
            ANSWER_LETTER_TOTAL = ANSWER_LETTER_TYPE1*0.65 + ANSWER_LETTER_TYPE2*0.35
            PERFORMANCE = ANSWER_LETTER_TOTAL*0.65 + np.mean(ANSWER_NUMBER)*0.35
            
            PERFORMANCE_TOTAL.append(PERFORMANCE)
            
            if PERFORMANCE < 0.85:
                error += 1
                accumu_error += 1
                STD = STD #STD does not increase --> repeat block
                if error == 3: 
                    # they couldn't perform at this STD, so revert to previous
                    # and set as HCL. This finishes the test.
                    self.screen.fill((0, 0, 0))  
                    self.render_centered_text("Congrats! The pretest is complete.")
                    time.sleep(3)
                    self.screen.fill((0, 0, 0))  
                    self.render_centered_text("")
                    PRETEST_HCL = STD + 0.10
                    PRETEST_LCL = PRETEST_HCL + 0.5*PRETEST_HCL
                    break
                
                if accumu_error == 3: # Although this value is fixed to 3 in Borragan & Slama,2017, increasing it at 5 might increase the pretest calibration
                    # the subject has had their performance across all tests
                    # dip below 85% 3 times. This ends the test. STD is kept 
                    # at the current value.
                    self.screen.fill((0, 0, 0))  
                    self.render_centered_text("Congrats! The pretest is complete.")
                    time.sleep(3)
                    self.screen.fill((0, 0, 0))  
                    self.render_centered_text("")  
                    PRETEST_HCL = STD
                    PRETEST_LCL = PRETEST_HCL + 0.5*PRETEST_HCL
                    break
                
                self.screen.fill((0, 0, 0))  
                self.render_centered_text("Let's take a break.")
                time.sleep(2)
                self.screen.fill((0, 0, 0))  
                self.render_centered_text("Press 'Y' to begin again when you're ready.")
                break_time = True
                while break_time:
                    if keyboard.is_pressed("y"):  # space key pressed
                        break_time = False
                        time.sleep(1)
                        self.screen.fill((0, 0, 0))  
                        self.render_centered_text('')
                        break  # finishing the loop
                    else:
                        continue
                    time.sleep(0.001)
                
            else:
                STD = STD - 0.10
                error = 0
                self.render_centered_text("Let's take a break.")
                time.sleep(2)
                self.screen.fill((0, 0, 0))  
                self.render_centered_text("Press 'Y' to begin again when you're ready.")
                break_time = True
                while break_time:
                    if keyboard.is_pressed("y"):  # space key pressed
                        break_time = False
                        time.sleep(1)
                        self.screen.fill((0, 0, 0))  
                        self.render_centered_text('')
                        break  # finishing the loop
                    else:
                        continue
                    time.sleep(0.001)
                            
        
        pre_row = pd.DataFrame(columns=list(self.file_dict["Pretest"]["dataframe"].columns))
        pre_row.loc[0, "Subject"] = self.subject_info["subject"]
        pre_row.loc[0, "Subject_number"] = self.subject_info["subject_number"]
        pre_row.loc[0, "Age"] = self.subject_info["age"]
        pre_row.loc[0, "Sex"] = self.subject_info["sex"]
        pre_row.loc[0, "PRETEST_HCL"] = PRETEST_HCL
        pre_row.loc[0, "PRETEST_LCL"] = PRETEST_LCL
        self.file_dict["Pretest"]["dataframe"] = pd.concat([self.file_dict["Pretest"]["dataframe"], pre_row])
       
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
        
        self.display_one_instruction(r"images\pretest\General_Instructions_REMADE.bmp")
        self.display_one_instruction(r"images\pretest\Digits_Instructions_REMADE.bmp")
        
        text = 'Digits Training is Beginning...'
        self.render_centered_text(text)
        time.sleep(2)
        self.screen.fill((0, 0, 0))
        self.digit_training()
        
        
        self.display_one_instruction(r"images\pretest\Letters_Instructions_REMADE.bmp")
        
        text = 'Letters Training is Beginning...'
        self.render_centered_text(text)
        time.sleep(2)
        self.screen.fill((0, 0, 0))
        self.letter_training()
        
        time.sleep(2)
        self.screen.fill((0, 0, 0))
        self.display_one_instruction(r"images\pretest\Letters_Digits_Instructions_REMADE.bmp")
        text = 'Letters and Digits Training is Beginning...'
        self.render_centered_text(text)
        time.sleep(2)
        self.screen.fill((0, 0, 0))
        self.learning_loop()
        self.pretest_loop()
        
        for key in self.file_dict.keys():
            df = self.file_dict[key]["dataframe"]
            df.to_csv(self.file_dict[key]["file_path"], index=False)

        
        pygame.quit()
        sys.exit(0)
        
        
        
if __name__ == "__main__":
    pre = TloadPretest()
    pre.run_game()
