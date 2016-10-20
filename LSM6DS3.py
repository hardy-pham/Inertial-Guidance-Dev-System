import smbus
from LSM6DS3_Registers import *

# initialize i2c connection through smbus
# TODO: fix to be OOP
bus = smbus.SMBus(1)
address = 0x6a


# TODO: Format properly
class LSM6DS3(object):
    """
    Initialization

    Initialize basic settings that will be inputted into the control registers to set up accelerometer and gyroscope
    """

    def __init__(self):
        self.address = 0x6a  # can be 0x6a or 0x6b --> 0x6a seems to be more stable as of now
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
        Setup accelerometer settings
        """
        dataToWrite = 0

        if (self.accelEnabled == 1):
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

            dataToWrite += accelBandWidthDict[self.accelBandwidth] + accelRangeDict[self.accelRange] + \
                           accelSampleRateDict[
                               self.accelSampleRate]

        # setup control register 1
        bus.write_byte_data(self.address, LSM6DS3_ACC_GYRO_CTRL1_XL, dataToWrite)

        # let bandwidth be determined by setting BW_XL[1:0] in CTRL1_XL (0x10)
        dataToWrite = LSM6DS3_ACC_GYRO_BW_SCAL_ODR_ENABLED
        bus.write_byte_data(self.address, LSM6DS3_ACC_GYRO_CTRL4_C, dataToWrite)

        """
        Setup gyroscope settings
        """
        dataToWrite = 0

        if (self.gyroEnabled == 1):
            gyroRangeDict = {
                125: LSM6DS3_ACC_GYRO_FS_125_ENABLED,
                245: LSM6DS3_ACC_GYRO_FS_G_245dps,
                500: LSM6DS3_ACC_GYRO_FS_G_500dps,
                1000: LSM6DS3_ACC_GYRO_FS_G_1000dps,
                2000: LSM6DS3_ACC_GYRO_FS_G_2000dps
            }

            gyroSampleRateDict = {
                13: LSM6DS3_ACC_GYRO_ODR_G_13Hz,
                26: LSM6DS3_ACC_GYRO_ODR_G_26Hz,
                52: LSM6DS3_ACC_GYRO_ODR_G_52Hz,
                104: LSM6DS3_ACC_GYRO_ODR_G_104Hz,
                208: LSM6DS3_ACC_GYRO_ODR_G_208Hz,
                416: LSM6DS3_ACC_GYRO_ODR_G_416Hz,
                833: LSM6DS3_ACC_GYRO_ODR_G_833Hz,
                1660: LSM6DS3_ACC_GYRO_ODR_G_1660Hz,
            }

            dataToWrite += gyroRangeDict[self.gyroRange] + gyroSampleRateDict[self.gyroSampleRate]

        bus.write_byte_data(self.address, LSM6DS3_ACC_GYRO_CTRL2_G, dataToWrite)

    """
    readAccelX / readAccelY / readAccelZ / readAccelXYZ

    returns the acceleration value for the given axis
    """

    def readAccelX(self):

        # connection between 0x6a and 0x6b is unstable. If 0x6a disconnects, use 0x6b
        # LSM6DS3_ACC_GYRO_OUTX_L_XL prints the X-axis output
        # output value is expressed as 16bit word in two's complement

        try:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTX_L_XL)))
        except IOError:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTX_L_XL)))

    def readAccelY(self):

        try:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTY_L_XL)))
        except IOError:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTY_L_XL)))

    def readAccelZ(self):
        try:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTZ_L_XL)))
        except IOError:
            return (self.calcAccel(self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTZ_L_XL)))

    def readAccelXYZ(self):
        while (True):
            X = self.readAccelX()
            Y = self.readAccelY()
            Z = self.readAccelZ()
            print("X: " + str(X) + "Y: " + str(Y) + "Z: " + str(Z))

    """
    calcAccel

    takes in a 16 bit word in two's complement and returns the X-axis linear acceleration value
    """

    def calcAccel(self, input):
        output = input * 0.0061 * (self.accelRange >> 1) / 1000
        return output

    """
    readGyroX

    returns the angular rate of the x-axis
    """

    def readGyroX(self):

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTX_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    """
    readGyroY

    returns the angular rate of the y-axis
    """

    def readGyroY(self):

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTY_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    """
    readGyroZ

    returns the angular rate of the z-axis
    """

    def readGyroZ(self):

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTZ_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    """
    readGyroXYZ

    prints the angular rate of all axes
    """

    def printGyroXYZ(self):
        initialCounter = 0
        while (True):
            if (initialCounter == 0):
                X = self.readGyroX()
                Y = self.readGyroY()
                Z = self.readGyroZ()

                xDifference = 0 - X
                yDifference = 0 - Y
                zDifference = 0 - Z

                initialCounter = 1

            X = round(self.readGyroX() + xDifference, 0)
            Y = round(self.readGyroY() + yDifference, 0)
            Z = round(self.readGyroZ() + zDifference, 0)

            print("X: " + str(X) + " Y: " + str(Y) + " Z: " + str(Z))

    """
    calcGyro

    Calculates the angular rate
    """

    def calcGyro(self, input):
        gyroRangeDivisor = self.gyroRange / 125
        if (self.gyroRange == 245):
            gyroRangeDivisor = 2

        output = input * 4.375 * gyroRangeDivisor / 1000
        return output

    """
    readRegisterInt16

    Reads blocks of bytes in order to process 16 bit returns from registers of 8 bits

    Input: register / the register to read blocks of 8 bits from
    Output: converted binary value of the 2s complement word
    """

    def readRegisterInt16(self, register):
        try:
            bytes = bus.read_i2c_block_data(self.address, register, 2)
        except IOError:
            bytes = bus.read_i2c_block_data(0x6b, register, 2)

        # turn read 8 bit register blocks into 16 bit 2s complement word
        output = bytes[0] | (bytes[1] << 8)

        # convert 16 bit 2s complement to int
        if (output & (1 << 16 - 1)):
            output = output - (1 << 16)

        return output


test = LSM6DS3()
test.begin()
test.readAccelXYZ()
