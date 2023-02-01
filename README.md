# TloadDback

The time-load dual-back (TloadDback) is a cognitive test in which different levels of cognitive load can be induced and individually adjusted by modifying the 
time available to process and manipulate the ongoing task demands.

The test is comprised on two parts: 1.) The pretest to individually calibrate high cognitive load (HCL) and low cognitive load (LCL) by setting a suitable stimulus time duration (STD) and 2.) The test itself to measure performance under either HCL or LCL.


## Installation
1. `git clone https://github.com/alyssa-rose/TloadDback.git`
2. `cd TloadDback`
3. `pip install -r requirements.txt` (this can and should be done within a virtual environment!)
4. in `configs/test_settings.yaml` modify: 
    * **subject**: Subjects identifier. If you do not wish to set it or do not have a separate identifier, set it equal to the subject_number in a string 
                   format. **It cannot empty!**
    * **subject_number**: Subject's number, must be unique to that subject. **It cannot be empty!**
    * **age**: Subject's age. May be obfuscated to protect identity. Age does not impact the results or test conditions. This value must be a positive integer.
    * **sex**: Either 'male' or 'female'
    * **condition**: Either 'HCL' or 'LCL'. It must be one of these two, or the test will not run.
    * **test_reps** [OPTIONAL]: How many times the test should be repeated. In Borragan et al. (2017), the test runs for 16 minutes. However, you may specify a 
                                short or longer time, although it is not recommended. If utilized, this value must be a positive integer. If it remains  
                                commented out, the test will run for 16 minutes [round(16/stimulus_time_duration)]
5. run `python pygame_TloadDback_Training_Pretest.py` **Note that you should NOT use the mouse, or click on the game window as this might cause the game to crash**. To quit early, you may press **ESC** at any time. If you quit early, no results will be saved.
6. run `python pygame_TloadDback.py` **Note that you should NOT use the mouse, or click on the game window as this might cause the game to crash**. To quit early, you may press **ESC** at any time. If you quit early, no results will be saved. If you attempt to run the test before the pretest, it will not work. `configs/test_settings.yaml` should NOT be modified in between running the pretest and the test.
