# Inertial-Guidance-Dev-System

Design for an inertial guidance development system

Used to evaluate and develop accurate satellite dish pointing systems and simulations
This system utilizes the IMU of the LSM6DS3 and interfaces with the Raspberry Pi 3

## Communicating with Raspberry Pi
Utilized Python's SMBus module
- https://pypi.python.org/pypi/smbus-cffi/0.5.1
- Capabilities
    - Read/Write to registers
    - Read/Write block data
    - Example
        - http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2

## Team: Mohamed Elamin, Ace Cordero, Ivan Arguello, Hardy Pham

Mac OS El Capitan Compatability Issue Notes:
- Getting PySide GUI to work on PyCharm
    - http://stackoverflow.com/questions/31343299/mysql-improperly-configured-reason-unsafe-use-of-relative-path
