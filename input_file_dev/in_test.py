self.address = 0x6b
self.gyroEnabled = 1            # can be 0 or 1
self.gyroRange = 2000           # Max deg/s. Can be: 125, 245, 500, 1000, 2000
self.gyroSampleRate = 416       # Hz. Can be: 13, 26, 52, 104, 208, 416, 833, 1666
self.gyroBandwidth = 400        # Hz. Can be: 50, 100, 200, 400
self.gyroFifoEnabled = 1        # Set to include gyro in FIFO
self.gyroFifoDecimation = 1     # Set 1 for on
self.accelEnabled = 1           # can be 0 or 1
self.accelODROff = 1
self.accelRange = 16            # Max G force readable. Can be: 2, 4, 8, 16
self.accelSampleRate = 416      # Hz. Can be: 13, 26, 52, 104, 208, 416, 833, 1666, 3332, 6664, 13330
self.accelBandwidth = 100       # Hz. Can be: 50, 100, 200, 400
self.accelFifoEnabled = 1       # Set to include accelerometer in the FIFO
self.accelFifoDecimation = 1    # Set 1 for on
self.tempEnabled = 1

# interface mode
self.commMode = 1                # Can be modes 1, 2, or 3

# FIFO control data
self.fifoThreshold = 3000        # Can be 0 to 4096(16 bit bytes)
self.fifoSampleRate = 10         # default 1-Hz
self.fifoModeWord = 0            # default off