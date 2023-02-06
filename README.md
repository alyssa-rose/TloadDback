# TloadDback

## _**This has only been tested on a Windows 10 machine. Use on Linux may require sudo privileges for use of the `keyboard` library. Additionally, file path locations will need to be made Linux compatible ('\' vs '/'). There is no information on the functionality of this code in a Mac environment, but installation instructions for Pygame may be found here: https://www.pygame.org/wiki/GettingStarted#Mac%20installation**_


The time-load dual-back (TloadDback) is a cognitive test in which different levels of cognitive load can be induced and individually adjusted by modifying the 
time available to process and manipulate the ongoing task demands.

The test is comprised on two parts: 1.) The pretest to individually calibrate high cognitive load (HCL) and low cognitive load (LCL) by setting a suitable stimulus time duration (STD) and 2.) The test itself to measure performance under either HCL or LCL.


## Installation
1. `git clone https://gitlab-ee.aurora.aero/praca103/tloaddback.git`
2. `cd tloaddback`
3. `pip install -r requirements.txt` (this can and should be done within a virtual environment!)
4. Refer to the PRETEST.md and TEST.md scripts under `scripts`, which provide context for the pretest and test, including how to run. The test director scripts without contextual information can be found under the files `scripts/<test type>_SCRIPT_ONLY.md`

During the pretest and test, the only file that requires modification and manual input is `configs/test_settings.yaml`, in which subject identifier, age, sex, and test condition must be specified for that user. It is required that a mapping of subject name to subject identifier exists beforehand. The subject identifier ("subject_number" in the config file) MUST be unique to that individual, and should only contain letters and/or numbers.
