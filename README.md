# Inertial-Guidance-Dev-System
Team: Mohamed Elamin, Ace Cordero, Ivan Arguello, Hardy Pham

This system utilizes the IMU of the LSM6DS3 sensor, providing users with accurate 3-axis accelerometer and gyroscope readings

## Hardware Components
- Raspberry Pi 3
- LSM6DS3 sensor board

## Communicating with Raspberry Pi
Utilized Python's SMBus module
- https://pypi.python.org/pypi/smbus-cffi/0.5.1
- Capabilities
    - Read/Write to registers
    - Read/Write block data
    - Example
        - http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
    
## Full Walkthrough
- Work in Progress

## Common Compatability Issues:
- Mac OSX El Capitan
    - Getting PySide module to work
        - Ran into trouble getting the PySide modules to work on MacOS El Capitan
        - http://stackoverflow.com/questions/31343299/mysql-improperly-configured-reason-unsafe-use-of-relative-path
