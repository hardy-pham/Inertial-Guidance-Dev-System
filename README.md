# Inertial Guidance System
Team: Mohamed Elamin, Ace Cordero, Ivan Arguello, Hardy Pham

- This system utilizes the IMU of the LSM6DS3 sensor, providing users with accurate 3-axis accelerometer and gyroscope readings
- This system is meant to be used with a Raspberry Pi on a Linux operating system

##### Hardware Components
- Raspberry Pi 3
- LSM6DS3 sensor board

## Files
- LSM6DS3.py
    - This file contains the LSM6DS3 class which contains a bundle of functions that initialize the settings for the gyroscope and accelerometer and output the results
- LSM6DS3_Registers.py
    - Contains a list of global variables used within LSM6DS3.py and sensorGUI.py
- LSM6DS3settings.ini
    - Contains the default configurations that are edited and saved through the GUI
- sensorGUI.py (located inside the GUI file)
    - This contains a graphical user interface which allows the user to edit the default settings, and read/write to any of the sensors registers

## Module Requirements
- configparser
    - pip install configparser
    - Used to read/write to the config file (LSM6DS3settings.ini)

- PyQt4
    - Installation setup: [PyQt setup](http://movingthelamppost.com/blog/html/2013/07/12/installing_pyqt____because_it_s_too_good_for_pip_or_easy_install_.html)
    - Used to display the GUI

- smbus
    - Installation setup: [SMBus setup](http://skpang.co.uk/blog/archives/575)
    - Allows SMBus access through the I2C /dev interface on Linux hosts
    - Useful links:
        - [Basic info on SMBus](https://pypi.python.org/pypi/smbus-cffi/0.5.1)
        - [Example usage of SMBus module](http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2)
    
## Usage
1. Establish all necessary wire connections
    1. Connect Raspberry Pi with a monitor through the HDMI port
    2. Connect the LSM6DS3 sensor with the Raspberry Pi
        - ![alt tag](http://i.imgur.com/7PjFGzD.png)
    3. Connect power to Raspberry Pi
        - Note: Be sure to connect the Raspberry Pi to the monitor first before powering it on to avoid resolution errors

2. Download the repository onto the Raspberry Pi

3. Install necessary modules listed above.
    - Note: Other modules such as time, csv, sys, etc., do not need to be downloaded as it comes loaded with Python already

4. Run the GUI
    1. Open the terminal
    2. Navigate to the directory containing all the files
    3. Run the GUI
        - python sensorGUI.py