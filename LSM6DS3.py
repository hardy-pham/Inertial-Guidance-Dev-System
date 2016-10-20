import smbus
from LSM6DS3_Registers import *

# initialize i2c connection through smbus
# TODO: fix to be OOP
bus = smbus.SMBus(1)
address = 0x6a


class LSM6DS3(object):
    """
    Initialization

    Initialize basic settings that will be inputted into the control registers to set up accelerometer and gyroscope
    """

    def __init__(self):
        self.gyroEnabled = 1  # can be 0 or 1
        self.gyroRange = 2000  # Max deg/s. Can be: 125, 245, 500, 1000, 2000
        self.gyroSampleRate = 416  # Hz. Can be: 13, 26, 52, 104, 208, 416, 833, 1666
        self.gyroBandwidth = 400  # Hz. Can be: 50, 100, 200, 400
        self.gyroFifoEnabled = 1  # Set to include gyro in FIFO
        self.gyroFifoDecimation = 1  # Set 1 for on

        self.accelEnabled = 1
        self.accelODROff = 1
        self.accelRange = 16  # Max G force readable. Can be: 2, 4, 8, 16
        self.accelSampleRate = 416  # Hz. Can be: 13, 26, 52, 104, 208, 416, 833, 1666, 3332, 6664, 13330
        self.accelBandwidth = 100  # Hz. Can be: 50, 100, 200, 400
        self.accelFifoEnabled = 1  # Set to include accelerometer in the FIFO
        self.accelFifoDecimation = 1  # Set 1 for on

        self.tempEnabled = 1

        # interface mode
        self.commMode = 1  # Can be modes 1, 2, or 3

        # FIFO control data
        self.fifoThreshold = 3000  # Can be 0 to 4096(16 bit bytes)
        self.fifoSampleRate = 10  # default 1-Hz
        self.fifoModeWord = 0  # default off

    """
    Configuration

    Uses the stored settings to start the IMU (Inertial Measurement Unit)
    """

    def begin(self):
        """
        Setup basic accelerometer settings
        """

        # filter bandwidth
        accelBandWidthDict = {
            50: LSM6DS3_ACC_GYRO_BW_XL_50Hz,
            100: LSM6DS3_ACC_GYRO_BW_XL_100Hz,
            200: LSM6DS3_ACC_GYRO_BW_XL_200Hz,
            400: LSM6DS3_ACC_GYRO_BW_XL_50Hz
        }

        # full scale
        accelRangeDict = {
            2: LSM6DS3_ACC_GYRO_FS_XL_2g,
            4: LSM6DS3_ACC_GYRO_FS_XL_4g,
            8: LSM6DS3_ACC_GYRO_FS_XL_8g,
            16: LSM6DS3_ACC_GYRO_FS_XL_16g
        }

        # accelerometer ODR
        accelSampleRateDict = {
            13: LSM6DS3_ACC_GYRO_ODR_XL_13Hz,
            26: LSM6DS3_ACC_GYRO_ODR_XL_26Hz,
            52: LSM6DS3_ACC_GYRO_ODR_XL_52Hz,
            104: LSM6DS3_ACC_GYRO_ODR_XL_104Hz,
            208: LSM6DS3_ACC_GYRO_ODR_XL_208Hz,
            416: LSM6DS3_ACC_GYRO_ODR_XL_416Hz,
            833: LSM6DS3_ACC_GYRO_ODR_XL_833Hz,
            1660: LSM6DS3_ACC_GYRO_ODR_XL_1660Hz,
            3330: LSM6DS3_ACC_GYRO_ODR_XL_3330Hz,
            6660: LSM6DS3_ACC_GYRO_ODR_XL_6660Hz,
            13330: LSM6DS3_ACC_GYRO_ODR_XL_13330Hz
        }

        dataToWrite = accelBandWidthDict[self.accelBandwidth] + accelRangeDict[self.accelRange] + accelSampleRateDict[
            self.accelSampleRate]

        # data sent to register
        print("{0:b}".format(dataToWrite))
        # setup control register 1
        bus.write_byte_data(self.address, LSM6DS3_ACC_GYRO_CTRL1_XL, dataToWrite)

        # let bandwidth be determined by setting BW_XL[1:0] in CTRL1_XL (0x10)
        dataToWrite = LSM6DS3_ACC_GYRO_BW_SCAL_ODR_ENABLED
        bus.write_byte_data(self.address, LSM6DS3_ACC_GYRO_CTRL4_C, dataToWrite)

        """
        Setup basic gyroscope settings
        """



test = LSM6DS3()
test.begin()
