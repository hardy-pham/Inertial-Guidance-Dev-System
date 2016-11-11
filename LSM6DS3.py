import smbus
import csv
import time
from LSM6DS3_Registers import *

# initialize i2c connection using smbus module
# TODO: fix to be OOP
bus = smbus.SMBus(1)
address = 0x6b

class LSM6DS3(object):
    """
    class creating a LSM6DS3 sensor object
    """

    def __init__(self):
        """
        Initialize setting variables that will be inputted into the control registers to set up accelerometer and gyroscope
        """

        self.address = 0x6b  # can be 0x6a or 0x6b --> 0x6a seems to be more stable as of now
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

    def begin(self):
        """
        configures basic settings for accelerometer and gyroscope

        @param none
        @return none
        """

        # setup accelerometer settings
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

        # setup gyroscope settings
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

    def readAccelX(self):
        """
        retrieves raw acceleration and returns the calculated acceleration

        @param none
        @return calcAccelX /calculated x-axis acceleration
        """

        rawAccelX = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTX_L_XL)
        calcAccelX = self.calcAccel(rawAccelX)

        return calcAccelX

    def readAccelY(self):
        """
        retrieves raw acceleration and returns the calculated acceleration

        @param none
        @return calcAccelY /calculated y-axis acceleration
        """

        rawAccelY = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTY_L_XL)
        calcAccelY = self.calcAccel(rawAccelY)

        return calcAccelY

    def readAccelZ(self):
        """
        retrieves raw acceleration and returns the calculated acceleration

        @param none
        @return calcAccelZ /calculated z-axis acceleration
        """

        rawAccelZ = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTZ_L_XL)
        calcAccelZ = self.calcAccel(rawAccelZ)

        return calcAccelZ

    def calcAccel(self, rawAccel):
        """
        converts the raw acceleration value from m/(s^2) to mg

        @param rawAccel /the raw acceleration value obtained from the output register
        @return calculatedAccel /the converted acceleration value
        """

        calculatedAccel = float(rawAccel) * 0.0509 * (
            self.accelRange >> 1) / 1000  # accel range is =/- 2 4 8 16g
        return calculatedAccel

    def printAccelXYZ(self):
        """
        prints the acceleration force in all three axes (x, y, and z)

        @param none
        @return none
        """

        # initial accelerometer calibration
        xCalibration = self.readAccelX()
        yCalibration = self.readAccelY()
        zCalibration = self.readAccelZ()

        while (True):
            X = self.readAccelX() - xCalibration
            Y = self.readAccelY() - yCalibration
            Z = self.readAccelZ() - zCalibration
            print("X:  " + str(X) + "  Y:  " + str(Y) + "  Z:  " + str(Z))

    def readGyroX(self):
        """
        returns the angular rate of the x-axis

        @param none
        @return calculatedRate /x-axis angular rate
        """

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTX_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    def readGyroY(self):
        """
        returns the angular rate of the y-axis

        @param none
        @return calculatedRate /y-axis angular rate
        """

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTY_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    def readGyroZ(self):
        """
        returns the angular rate of the z-axis

        @param none
        @return calculatedRate /z-axis angular rate
        """

        readValue = self.readRegisterInt16(LSM6DS3_ACC_GYRO_OUTZ_L_G)
        calculatedRate = self.calcGyro(readValue)
        return calculatedRate

    def calcGyro(self, rawGyro):
        """
        Calculates the angular rate

        @param rawGyro /raw value obtained from the register
        @return calcAngRate /calculated angular rate from the raw value in the register
        """

        gyroRangeDivisor = self.gyroRange / 125
        if (self.gyroRange == 245):
            gyroRangeDivisor = 2

        calcAngRate = rawGyro * 4.375 * gyroRangeDivisor / 1000
        return calcAngRate

    def printGyroXYZ(self):
        """
        prints the angular rate of all axes to the terminal

        @param none
        @return none
        """

        # TODO: fix calibration
        # initial gyroscope calibration
        xCalibration = self.readGyroX()
        yCalibration = self.readGyroY()
        zCalibration = self.readGyroZ()

        while (True):
            X = round(self.readGyroX() - xCalibration, 0)
            Y = round(self.readGyroY() - yCalibration, 0)
            Z = round(self.readGyroZ() - zCalibration, 0)

            print("X: " + str(X) + " Y: " + str(Y) + " Z: " + str(Z))

    def logAccelXYZ(self):
        """
        logs the output to a unique log file that is named based on the current time and date

        @param none
        @return none
        """

        # TODO: test functionality

        counter = 0
        # YearMonthDate_HourMinutesSeconds
        curDateTime = time.strftime("%Y%m%d_%H%M%S")
        xCalibration = 0
        yCalibration = 0
        zCalibration = 0

        # initial calibration using 100 values
        while(counter < 100):

            counter += 1
            xCalibration += self.readAccelX()
            yCalibration += self.readAccelY()
            zCalibration += self.readAccelZ()

        xCalibration /= 100
        yCalibration /= 100
        zCalibration /= 100

        with open('../logs/' + str(curDateTime) + '_log.csv', 'a') as file:
            w = csv.writer(file)

            while (True):
                X = round(self.readGyroX() - xCalibration, 0)
                Y = round(self.readGyroY() - yCalibration, 0)
                Z = round(self.readGyroZ() - zCalibration, 0)

                # append
                # TODO: add time stamp
                w.writerow([X, Y, Z])

    def readRegisterInt16(self, register):
        """
        Reads blocks of bytes in order to process 16 bit returns from registers of 8 bits

        @param register /the register to read blocks of 8 bits from
        @return output /converted binary value of the 2s complement word
        """

        # connection between 0x6a and 0x6b is unstable. If 0x6b disconnects, use 0x6a
        try:
            bytes = bus.read_i2c_block_data(self.address, register, 2)
        except IOError:
            bytes = bus.read_i2c_block_data(0x6a, register, 2)

        # turn read 8 bit register blocks into 16 bit 2s complement word
        output = bytes[0] | (bytes[1] << 8)

        # convert 16 bit 2s complement into a decimal int
        if (output & (1 << 16 - 1)):
            output = output - (1 << 16)

        return output

# test calls
test = LSM6DS3()
test.begin()
test.printAccelXYZ()
# test.printGyroXYZ()