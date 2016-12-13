# Inertial Guidance System
Team: Mohamed Elamin, Ace Cordero, Ivan Arguello, Hardy Pham

This system utilizes the IMU of the LSM6DS3 sensor, providing users with accurate 3-axis accelerometer and gyroscope readings
This system is meant to be used with a Raspberry Pi on a Linux operating system

## Hardware Components
- Raspberry Pi 3
- LSM6DS3 sensor board

## Files
- LSM6DS3.py
-- This file contains the LSM6DS3 class which contains a bundle of functions that initialize the settings for the gyroscope and accelerometer and output the results
- LSM6DS3_Registers.py
-- Contains a list of global variables used within LSM6DS3.py and sensorGUI.py
- LSM6DS3settings.ini
-- Contains the default configurations that are edited and saved through the GUI
- sensorGUI.py (located inside the GUI file)
-- This contains a graphical user interface which allows the user to edit the default settings, and read/write to any of the sensors registers

## Module Requirements
- configparser
-- pip install configparser
--- Used to read/write to the config file (LSM6DS3settings.ini)

- PyQt4
-- Installation setup: http://movingthelamppost.com/blog/html/2013/07/12/installing_pyqt____because_it_s_too_good_for_pip_or_easy_install_.html
--- Used to display the GUI

- smbus
-- Installation setup: http://skpang.co.uk/blog/archives/575
--- Allows SMBus access through the I2C /dev interface on Linux hosts
---- Useful links:
----- https://pypi.python.org/pypi/smbus-cffi/0.5.1
----- http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
    
## Full Walkthrough
- Work in Progress