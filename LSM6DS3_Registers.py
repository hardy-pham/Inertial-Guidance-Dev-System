# Device Registers
LSM6DS3_ACC_GYRO_TEST_PAGE = 0X00
LSM6DS3_ACC_GYRO_RAM_ACCESS = 0X01
LSM6DS3_ACC_GYRO_SENSOR_SYNC_TIME = 0X04
LSM6DS3_ACC_GYRO_SENSOR_SYNC_EN = 0X05
LSM6DS3_ACC_GYRO_FIFO_CTRL1 = 0X06
LSM6DS3_ACC_GYRO_FIFO_CTRL2 = 0X07
LSM6DS3_ACC_GYRO_FIFO_CTRL3 = 0X08
LSM6DS3_ACC_GYRO_FIFO_CTRL4 = 0X09
LSM6DS3_ACC_GYRO_FIFO_CTRL5 = 0X0A
LSM6DS3_ACC_GYRO_ORIENT_CFG_G = 0X0B
LSM6DS3_ACC_GYRO_REFERENCE_G = 0X0C
LSM6DS3_ACC_GYRO_INT1_CTRL = 0X0D
LSM6DS3_ACC_GYRO_INT2_CTRL = 0X0E
LSM6DS3_ACC_GYRO_WHO_AM_I_REG = 0X0F
LSM6DS3_ACC_GYRO_CTRL1_XL = 0X10
LSM6DS3_ACC_GYRO_CTRL2_G = 0X11
LSM6DS3_ACC_GYRO_CTRL3_C = 0X12
LSM6DS3_ACC_GYRO_CTRL4_C = 0X13
LSM6DS3_ACC_GYRO_CTRL5_C = 0X14
LSM6DS3_ACC_GYRO_CTRL6_G = 0X15
LSM6DS3_ACC_GYRO_CTRL7_G = 0X16
LSM6DS3_ACC_GYRO_CTRL8_XL = 0X17
LSM6DS3_ACC_GYRO_CTRL9_XL = 0X18
LSM6DS3_ACC_GYRO_CTRL10_C = 0X19
LSM6DS3_ACC_GYRO_MASTER_CONFIG = 0X1A
LSM6DS3_ACC_GYRO_WAKE_UP_SRC = 0X1B
LSM6DS3_ACC_GYRO_TAP_SRC = 0X1C
LSM6DS3_ACC_GYRO_D6D_SRC = 0X1D
LSM6DS3_ACC_GYRO_STATUS_REG = 0X1E
LSM6DS3_ACC_GYRO_OUT_TEMP_L = 0X20
LSM6DS3_ACC_GYRO_OUT_TEMP_H = 0X21
LSM6DS3_ACC_GYRO_OUTX_L_G = 0X22
LSM6DS3_ACC_GYRO_OUTX_H_G = 0X23
LSM6DS3_ACC_GYRO_OUTY_L_G = 0X24
LSM6DS3_ACC_GYRO_OUTY_H_G = 0X25
LSM6DS3_ACC_GYRO_OUTZ_L_G = 0X26
LSM6DS3_ACC_GYRO_OUTZ_H_G = 0X27
LSM6DS3_ACC_GYRO_OUTX_L_XL = 0X28
LSM6DS3_ACC_GYRO_OUTX_H_XL = 0X29
LSM6DS3_ACC_GYRO_OUTY_L_XL = 0X2A
LSM6DS3_ACC_GYRO_OUTY_H_XL = 0X2B
LSM6DS3_ACC_GYRO_OUTZ_L_XL = 0X2C
LSM6DS3_ACC_GYRO_OUTZ_H_XL = 0X2D
LSM6DS3_ACC_GYRO_SENSORHUB1_REG = 0X2E
LSM6DS3_ACC_GYRO_SENSORHUB2_REG = 0X2F
LSM6DS3_ACC_GYRO_SENSORHUB3_REG = 0X30
LSM6DS3_ACC_GYRO_SENSORHUB4_REG = 0X31
LSM6DS3_ACC_GYRO_SENSORHUB5_REG = 0X32
LSM6DS3_ACC_GYRO_SENSORHUB6_REG = 0X33
LSM6DS3_ACC_GYRO_SENSORHUB7_REG = 0X34
LSM6DS3_ACC_GYRO_SENSORHUB8_REG = 0X35
LSM6DS3_ACC_GYRO_SENSORHUB9_REG = 0X36
LSM6DS3_ACC_GYRO_SENSORHUB10_REG = 0X37
LSM6DS3_ACC_GYRO_SENSORHUB11_REG = 0X38
LSM6DS3_ACC_GYRO_SENSORHUB12_REG = 0X39
LSM6DS3_ACC_GYRO_FIFO_STATUS1 = 0X3A
LSM6DS3_ACC_GYRO_FIFO_STATUS2 = 0X3B
LSM6DS3_ACC_GYRO_FIFO_STATUS3 = 0X3C
LSM6DS3_ACC_GYRO_FIFO_STATUS4 = 0X3D
LSM6DS3_ACC_GYRO_FIFO_DATA_OUT_L = 0X3E
LSM6DS3_ACC_GYRO_FIFO_DATA_OUT_H = 0X3F
LSM6DS3_ACC_GYRO_TIMESTAMP0_REG = 0X40
LSM6DS3_ACC_GYRO_TIMESTAMP1_REG = 0X41
LSM6DS3_ACC_GYRO_TIMESTAMP2_REG = 0X42
LSM6DS3_ACC_GYRO_STEP_COUNTER_L = 0X4B
LSM6DS3_ACC_GYRO_STEP_COUNTER_H = 0X4C
LSM6DS3_ACC_GYRO_FUNC_SRC = 0X53
LSM6DS3_ACC_GYRO_TAP_CFG1 = 0X58
LSM6DS3_ACC_GYRO_TAP_THS_6D = 0X59
LSM6DS3_ACC_GYRO_INT_DUR2 = 0X5A
LSM6DS3_ACC_GYRO_WAKE_UP_THS = 0X5B
LSM6DS3_ACC_GYRO_WAKE_UP_DUR = 0X5C
LSM6DS3_ACC_GYRO_FREE_FALL = 0X5D
LSM6DS3_ACC_GYRO_MD1_CFG = 0X5E
LSM6DS3_ACC_GYRO_MD2_CFG = 0X5F

# Access Device RAM
LSM6DS3_ACC_GYRO_ADDR0_TO_RW_RAM = 0x62
LSM6DS3_ACC_GYRO_ADDR1_TO_RW_RAM = 0x63
LSM6DS3_ACC_GYRO_DATA_TO_WR_RAM = 0x64
LSM6DS3_ACC_GYRO_DATA_RD_FROM_RAM = 0x65

LSM6DS3_ACC_GYRO_RAM_SIZE = 4096

# Embedded functions register mapping
LSM6DS3_ACC_GYRO_SLV0_ADD = 0x02
LSM6DS3_ACC_GYRO_SLV0_SUBADD = 0x03
LSM6DS3_ACC_GYRO_SLAVE0_CONFIG = 0x04
LSM6DS3_ACC_GYRO_SLV1_ADD = 0x05
LSM6DS3_ACC_GYRO_SLV1_SUBADD = 0x06
LSM6DS3_ACC_GYRO_SLAVE1_CONFIG = 0x07
LSM6DS3_ACC_GYRO_SLV2_ADD = 0x08
LSM6DS3_ACC_GYRO_SLV2_SUBADD = 0x09
LSM6DS3_ACC_GYRO_SLAVE2_CONFIG = 0x0A
LSM6DS3_ACC_GYRO_SLV3_ADD = 0x0B
LSM6DS3_ACC_GYRO_SLV3_SUBADD = 0x0C
LSM6DS3_ACC_GYRO_SLAVE3_CONFIG = 0x0D
LSM6DS3_ACC_GYRO_DATAWRITE_SRC_MODE_SUB_SLV0 = 0x0E
LSM6DS3_ACC_GYRO_CONFIG_PEDO_THS_MIN = 0x0F
LSM6DS3_ACC_GYRO_CONFIG_TILT_IIR = 0x10
LSM6DS3_ACC_GYRO_CONFIG_TILT_ACOS = 0x11
LSM6DS3_ACC_GYRO_CONFIG_TILT_WTIME = 0x12
LSM6DS3_ACC_GYRO_SM_STEP_THS = 0x13
LSM6DS3_ACC_GYRO_MAG_SI_XX = 0x24
LSM6DS3_ACC_GYRO_MAG_SI_XY = 0x25
LSM6DS3_ACC_GYRO_MAG_SI_XZ = 0x26
LSM6DS3_ACC_GYRO_MAG_SI_YX = 0x27
LSM6DS3_ACC_GYRO_MAG_SI_YY = 0x28
LSM6DS3_ACC_GYRO_MAG_SI_YZ = 0x29
LSM6DS3_ACC_GYRO_MAG_SI_ZX = 0x2A
LSM6DS3_ACC_GYRO_MAG_SI_ZY = 0x2B
LSM6DS3_ACC_GYRO_MAG_SI_ZZ = 0x2C
LSM6DS3_ACC_GYRO_MAG_OFFX_L = 0x2D
LSM6DS3_ACC_GYRO_MAG_OFFX_H = 0x2E
LSM6DS3_ACC_GYRO_MAG_OFFY_L = 0x2F
LSM6DS3_ACC_GYRO_MAG_OFFY_H = 0x30
LSM6DS3_ACC_GYRO_MAG_OFFZ_L = 0x31
LSM6DS3_ACC_GYRO_MAG_OFFZ_H = 0x32

"""
* Register      : TEST_PAGE
* Address       : 0X00
* Bit Group Name: FLASH_PAGE
* Permission    : RW
"""

FLASH_PAGE = 0x40

"""
* Register      : RAM_ACCESS
* Address       : 0X01
* Bit Group Name: PROG_RAM1
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PROG_RAM1_DISABLED = 0x00
LSM6DS3_ACC_GYRO_PROG_RAM1_ENABLED = 0x01

"""
* Register      : RAM_ACCESS
* Address       : 0X01
* Bit Group Name: CUSTOMROM1
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_CUSTOMROM1_DISABLED = 0x00
LSM6DS3_ACC_GYRO_CUSTOMROM1_ENABLED = 0x04

"""
* Register      : RAM_ACCESS
* Address       : 0X01
* Bit Group Name: RAM_PAGE
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_RAM_PAGE_DISABLED = 0x00
LSM6DS3_ACC_GYRO_RAM_PAGE_ENABLED = 0x80

"""
* Register      : SENSOR_SYNC_TIME
* Address       : 0X04
* Bit Group Name: TPH
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_TPH_MASK = 0xFF
LSM6DS3_ACC_GYRO_TPH_POSITION = 0

"""
* Register      : SENSOR_SYNC_EN
* Address       : 0X05
* Bit Group Name: SYNC_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SYNC_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_SYNC_EN_ENABLED = 0x01

"""
* Register      : SENSOR_SYNC_EN
* Address       : 0X05
* Bit Group Name: HP_RST
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_HP_RST_RST_OFF = 0x00
LSM6DS3_ACC_GYRO_HP_RST_RST_ON = 0x02

"""
* Register      : FIFO_CTRL1
* Address       : 0X06
* Bit Group Name: WTM_FIFO
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_WTM_FIFO_CTRL1_MASK = 0xFF
LSM6DS3_ACC_GYRO_WTM_FIFO_CTRL1_POSITION = 0
LSM6DS3_ACC_GYRO_WTM_FIFO_CTRL2_MASK = 0x0F
LSM6DS3_ACC_GYRO_WTM_FIFO_CTRL2_POSITION = 0

"""
* Register      : FIFO_CTRL2
* Address       : 0X07
* Bit Group Name: TIM_PEDO_FIFO_DRDY
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TIM_PEDO_FIFO_DRDY_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TIM_PEDO_FIFO_DRDY_ENABLED = 0x40

"""
* Register      : FIFO_CTRL2
* Address       : 0X07
* Bit Group Name: TIM_PEDO_FIFO_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TIM_PEDO_FIFO_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TIM_PEDO_FIFO_EN_ENABLED = 0x80

"""
* Register      : FIFO_CTRL3
* Address       : 0X08
* Bit Group Name: DEC_FIFO_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DATA_NOT_IN_FIFO = 0x00
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_NO_DECIMATION = 0x01
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_2 = 0x02
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_3 = 0x03
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_4 = 0x04
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_8 = 0x05
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_16 = 0x06
LSM6DS3_ACC_GYRO_DEC_FIFO_XL_DECIMATION_BY_32 = 0x07

"""
* Register      : FIFO_CTRL3
* Address       : 0X08
* Bit Group Name: DEC_FIFO_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEC_FIFO_G_DATA_NOT_IN_FIFO = 0x00
LSM6DS3_ACC_GYRO_DEC_FIFO_G_NO_DECIMATION = 0x08
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_2 = 0x10
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_3 = 0x18
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_4 = 0x20
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_8 = 0x28
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_16 = 0x30
LSM6DS3_ACC_GYRO_DEC_FIFO_G_DECIMATION_BY_32 = 0x38

"""
* Register      : FIFO_CTRL4
* Address       : 0X09
* Bit Group Name: DEC_FIFO_SLV0
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DATA_NOT_IN_FIFO = 0x00
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_NO_DECIMATION = 0x01
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_2 = 0x02
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_3 = 0x03
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_4 = 0x04
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_8 = 0x05
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_16 = 0x06
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV0_DECIMATION_BY_32 = 0x07

"""
* Register      : FIFO_CTRL4
* Address       : 0X09
* Bit Group Name: DEC_FIFO_SLV1
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DATA_NOT_IN_FIFO = 0x00
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_NO_DECIMATION = 0x08
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_2 = 0x10
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_3 = 0x18
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_4 = 0x20
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_8 = 0x28
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_16 = 0x30
LSM6DS3_ACC_GYRO_DEC_FIFO_SLV1_DECIMATION_BY_32 = 0x38

"""
* Register      : FIFO_CTRL4
* Address       : 0X09
* Bit Group Name: HI_DATA_ONLY
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_HI_DATA_ONLY_DISABLED = 0x00
LSM6DS3_ACC_GYRO_HI_DATA_ONLY_ENABLED = 0x40

"""
* Register      : FIFO_CTRL5
* Address       : 0X0A
* Bit Group Name: FIFO_MODE
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FIFO_MODE_BYPASS = 0x00
LSM6DS3_ACC_GYRO_FIFO_MODE_FIFO = 0x01
LSM6DS3_ACC_GYRO_FIFO_MODE_STREAM = 0x02
LSM6DS3_ACC_GYRO_FIFO_MODE_STF = 0x03
LSM6DS3_ACC_GYRO_FIFO_MODE_BTS = 0x04
LSM6DS3_ACC_GYRO_FIFO_MODE_DYN_STREAM = 0x05
LSM6DS3_ACC_GYRO_FIFO_MODE_DYN_STREAM_2 = 0x06
LSM6DS3_ACC_GYRO_FIFO_MODE_BTF = 0x07

"""
* Register      : FIFO_CTRL5
* Address       : 0X0A
* Bit Group Name: ODR_FIFO
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ODR_FIFO_10Hz = 0x08
LSM6DS3_ACC_GYRO_ODR_FIFO_25Hz = 0x10
LSM6DS3_ACC_GYRO_ODR_FIFO_50Hz = 0x18
LSM6DS3_ACC_GYRO_ODR_FIFO_100Hz = 0x20
LSM6DS3_ACC_GYRO_ODR_FIFO_200Hz = 0x28
LSM6DS3_ACC_GYRO_ODR_FIFO_400Hz = 0x30
LSM6DS3_ACC_GYRO_ODR_FIFO_800Hz = 0x38
LSM6DS3_ACC_GYRO_ODR_FIFO_1600Hz = 0x40
LSM6DS3_ACC_GYRO_ODR_FIFO_3300Hz = 0x48
LSM6DS3_ACC_GYRO_ODR_FIFO_6600Hz = 0x50
LSM6DS3_ACC_GYRO_ODR_FIFO_13300Hz = 0x58

"""
* Register      : ORIENT_CFG_G
* Address       : 0X0B
* Bit Group Name: ORIENT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ORIENT_XYZ = 0x00
LSM6DS3_ACC_GYRO_ORIENT_XZY = 0x01
LSM6DS3_ACC_GYRO_ORIENT_YXZ = 0x02
LSM6DS3_ACC_GYRO_ORIENT_YZX = 0x03
LSM6DS3_ACC_GYRO_ORIENT_ZXY = 0x04
LSM6DS3_ACC_GYRO_ORIENT_ZYX = 0x05

"""
* Register      : ORIENT_CFG_G
* Address       : 0X0B
* Bit Group Name: SIGN_Z_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIGN_Z_G_POSITIVE = 0x00
LSM6DS3_ACC_GYRO_SIGN_Z_G_NEGATIVE = 0x08

"""
* Register      : ORIENT_CFG_G
* Address       : 0X0B
* Bit Group Name: SIGN_Y_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIGN_Y_G_POSITIVE = 0x00
LSM6DS3_ACC_GYRO_SIGN_Y_G_NEGATIVE = 0x10

"""
* Register      : ORIENT_CFG_G
* Address       : 0X0B
* Bit Group Name: SIGN_X_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIGN_X_G_POSITIVE = 0x00
LSM6DS3_ACC_GYRO_SIGN_X_G_NEGATIVE = 0x20

"""
* Register      : REFERENCE_G
* Address       : 0X0C
* Bit Group Name: REF_G
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_REF_G_MASK = 0xFF
LSM6DS3_ACC_GYRO_REF_G_POSITION = 0

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_DRDY_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_DRDY_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_DRDY_XL_ENABLED = 0x01

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_DRDY_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_DRDY_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_DRDY_G_ENABLED = 0x02

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_BOOT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_BOOT_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_BOOT_ENABLED = 0x04

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_FTH
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_FTH_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_FTH_ENABLED = 0x08

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_OVR
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_OVR_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_OVR_ENABLED = 0x10

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_FSS5
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_FSS5_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_FSS5_ENABLED = 0x20

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_SIGN_MOT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_SIGN_MOT_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_SIGN_MOT_ENABLED = 0x40

"""
* Register      : INT1_CTRL
* Address       : 0X0D
* Bit Group Name: INT1_PEDO
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_PEDO_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_PEDO_ENABLED = 0x80

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_DRDY_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_DRDY_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_DRDY_XL_ENABLED = 0x01

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_DRDY_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_DRDY_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_DRDY_G_ENABLED = 0x02

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_FTH
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_FTH_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_FTH_ENABLED = 0x08

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_OVR
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_OVR_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_OVR_ENABLED = 0x10

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_FSS5
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_FSS5_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_FSS5_ENABLED = 0x20

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_SIGN_MOT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_SIGN_MOT_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_SIGN_MOT_ENABLED = 0x40

"""
* Register      : INT2_CTRL
* Address       : 0X0E
* Bit Group Name: INT2_PEDO
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_PEDO_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_PEDO_ENABLED = 0x80

"""
* Register      : WHO_AM_I
* Address       : 0X0F
* Bit Group Name: WHO_AM_I_BIT
* Permission    : RO
"""
LSM6DS3_ACC_GYRO_WHO_AM_I_BIT_MASK = 0xFF
LSM6DS3_ACC_GYRO_WHO_AM_I_BIT_POSITION = 0

"""
* Register      : CTRL1_XL
* Address       : 0X10
* Bit Group Name: BW_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_BW_XL_400Hz = 0x00
LSM6DS3_ACC_GYRO_BW_XL_200Hz = 0x01
LSM6DS3_ACC_GYRO_BW_XL_100Hz = 0x02
LSM6DS3_ACC_GYRO_BW_XL_50Hz = 0x03

"""
* Register      : CTRL1_XL
* Address       : 0X10
* Bit Group Name: FS_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FS_XL_2g = 0x00
LSM6DS3_ACC_GYRO_FS_XL_16g = 0x04
LSM6DS3_ACC_GYRO_FS_XL_4g = 0x08
LSM6DS3_ACC_GYRO_FS_XL_8g = 0x0C

"""
* Register      : CTRL1_XL
* Address       : 0X10
* Bit Group Name: ODR_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ODR_XL_POWER_DOWN = 0x00
LSM6DS3_ACC_GYRO_ODR_XL_13Hz = 0x10
LSM6DS3_ACC_GYRO_ODR_XL_26Hz = 0x20
LSM6DS3_ACC_GYRO_ODR_XL_52Hz = 0x30
LSM6DS3_ACC_GYRO_ODR_XL_104Hz = 0x40
LSM6DS3_ACC_GYRO_ODR_XL_208Hz = 0x50
LSM6DS3_ACC_GYRO_ODR_XL_416Hz = 0x60
LSM6DS3_ACC_GYRO_ODR_XL_833Hz = 0x70
LSM6DS3_ACC_GYRO_ODR_XL_1660Hz = 0x80
LSM6DS3_ACC_GYRO_ODR_XL_3330Hz = 0x90
LSM6DS3_ACC_GYRO_ODR_XL_6660Hz = 0xA0
LSM6DS3_ACC_GYRO_ODR_XL_13330Hz = 0xB0

"""
* Register      : CTRL2_G
* Address       : 0X11
* Bit Group Name: FS_125
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FS_125_DISABLED = 0x00
LSM6DS3_ACC_GYRO_FS_125_ENABLED = 0x02

"""
* Register      : CTRL2_G
* Address       : 0X11
* Bit Group Name: FS_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FS_G_245dps = 0x00
LSM6DS3_ACC_GYRO_FS_G_500dps = 0x04
LSM6DS3_ACC_GYRO_FS_G_1000dps = 0x08
LSM6DS3_ACC_GYRO_FS_G_2000dps = 0x0C

"""
* Register      : CTRL2_G
* Address       : 0X11
* Bit Group Name: ODR_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ODR_G_POWER_DOWN = 0x00
LSM6DS3_ACC_GYRO_ODR_G_13Hz = 0x10
LSM6DS3_ACC_GYRO_ODR_G_26Hz = 0x20
LSM6DS3_ACC_GYRO_ODR_G_52Hz = 0x30
LSM6DS3_ACC_GYRO_ODR_G_104Hz = 0x40
LSM6DS3_ACC_GYRO_ODR_G_208Hz = 0x50
LSM6DS3_ACC_GYRO_ODR_G_416Hz = 0x60
LSM6DS3_ACC_GYRO_ODR_G_833Hz = 0x70
LSM6DS3_ACC_GYRO_ODR_G_1660Hz = 0x80

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: SW_RESET
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SW_RESET_NORMAL_MODE = 0x00
LSM6DS3_ACC_GYRO_SW_RESET_RESET_DEVICE = 0x01

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: BLE
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_BLE_LSB = 0x00
LSM6DS3_ACC_GYRO_BLE_MSB = 0x02

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: IF_INC
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_IF_INC_DISABLED = 0x00
LSM6DS3_ACC_GYRO_IF_INC_ENABLED = 0x04

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: SIM
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIM_4_WIRE = 0x00
LSM6DS3_ACC_GYRO_SIM_3_WIRE = 0x08

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: PP_OD
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PP_OD_PUSH_PULL = 0x00
LSM6DS3_ACC_GYRO_PP_OD_OPEN_DRAIN = 0x10

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: INT_ACT_LEVEL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT_ACT_LEVEL_ACTIVE_HI = 0x00
LSM6DS3_ACC_GYRO_INT_ACT_LEVEL_ACTIVE_LO = 0x20

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: BDU
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_BDU_CONTINUOS = 0x00
LSM6DS3_ACC_GYRO_BDU_BLOCK_UPDATE = 0x40

"""
* Register      : CTRL3_C
* Address       : 0X12
* Bit Group Name: BOOT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_BOOT_NORMAL_MODE = 0x00
LSM6DS3_ACC_GYRO_BOOT_REBOOT_MODE = 0x80

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: STOP_ON_FTH
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_STOP_ON_FTH_DISABLED = 0x00
LSM6DS3_ACC_GYRO_STOP_ON_FTH_ENABLED = 0x01

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: MODE3_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_MODE3_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_MODE3_EN_ENABLED = 0x02

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: I2C_DISABLE
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_I2C_DISABLE_I2C_AND_SPI = 0x00
LSM6DS3_ACC_GYRO_I2C_DISABLE_SPI_ONLY = 0x04

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: DRDY_MSK
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DRDY_MSK_DISABLED = 0x00
LSM6DS3_ACC_GYRO_DRDY_MSK_ENABLED = 0x08

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: FIFO_TEMP_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FIFO_TEMP_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_FIFO_TEMP_EN_ENABLED = 0x10

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: INT2_ON_INT1
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_ON_INT1_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_ON_INT1_ENABLED = 0x20

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: SLEEP_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SLEEP_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_SLEEP_G_ENABLED = 0x40

"""
* Register      : CTRL4_C
* Address       : 0X13
* Bit Group Name: BW_SCAL_ODR
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_BW_SCAL_ODR_DISABLED = 0x00
LSM6DS3_ACC_GYRO_BW_SCAL_ODR_ENABLED = 0x80

"""
* Register      : CTRL5_C
* Address       : 0X14
* Bit Group Name: ST_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ST_XL_NORMAL_MODE = 0x00
LSM6DS3_ACC_GYRO_ST_XL_POS_SIGN_TEST = 0x01
LSM6DS3_ACC_GYRO_ST_XL_NEG_SIGN_TEST = 0x02
LSM6DS3_ACC_GYRO_ST_XL_NA = 0x03

"""
* Register      : CTRL5_C
* Address       : 0X14
* Bit Group Name: ST_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ST_G_NORMAL_MODE = 0x00
LSM6DS3_ACC_GYRO_ST_G_POS_SIGN_TEST = 0x04
LSM6DS3_ACC_GYRO_ST_G_NA = 0x08
LSM6DS3_ACC_GYRO_ST_G_NEG_SIGN_TEST = 0x0C

"""
* Register      : CTRL6_G
* Address       : 0X15
* Bit Group Name: LP_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_LP_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_LP_XL_ENABLED = 0x10

"""
* Register      : CTRL6_G
* Address       : 0X15
* Bit Group Name: DEN_LVL2_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEN_LVL2_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_DEN_LVL2_EN_ENABLED = 0x20

"""
* Register      : CTRL6_G
* Address       : 0X15
* Bit Group Name: DEN_LVL_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEN_LVL_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_DEN_LVL_EN_ENABLED = 0x40

"""
* Register      : CTRL6_G
* Address       : 0X15
* Bit Group Name: DEN_EDGE_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DEN_EDGE_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_DEN_EDGE_EN_ENABLED = 0x80

"""
* Register      : CTRL7_G
* Address       : 0X16
* Bit Group Name: HPM_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_HPM_G_NORMAL_MODE = 0x00
LSM6DS3_ACC_GYRO_HPM_G_REF_SIGNAL = 0x10
LSM6DS3_ACC_GYRO_HPM_G_NORMAL_MODE_2 = 0x20
LSM6DS3_ACC_GYRO_HPM_G_AUTO_RESET_ON_INT = 0x30

"""
* Register      : CTRL7_G
* Address       : 0X16
* Bit Group Name: HP_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_HP_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_HP_EN_ENABLED = 0x40

"""
* Register      : CTRL7_G
* Address       : 0X16
* Bit Group Name: LP_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_LP_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_LP_EN_ENABLED = 0x80

"""
* Register      : CTRL8_XL
* Address       : 0X17
* Bit Group Name: FDS
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FDS_FILTER_OFF = 0x00
LSM6DS3_ACC_GYRO_FDS_FILTER_ON = 0x04

"""
* Register      : CTRL9_XL
* Address       : 0X18
* Bit Group Name: XEN_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_XEN_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_XEN_XL_ENABLED = 0x08

"""
* Register      : CTRL9_XL
* Address       : 0X18
* Bit Group Name: YEN_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_YEN_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_YEN_XL_ENABLED = 0x10

"""
* Register      : CTRL9_XL
* Address       : 0X18
* Bit Group Name: ZEN_XL
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ZEN_XL_DISABLED = 0x00
LSM6DS3_ACC_GYRO_ZEN_XL_ENABLED = 0x20

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: SIGN_MOTION_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIGN_MOTION_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_SIGN_MOTION_EN_ENABLED = 0x01

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: PEDO_RST_STEP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PEDO_RST_STEP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_PEDO_RST_STEP_ENABLED = 0x02

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: XEN_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_XEN_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_XEN_G_ENABLED = 0x08

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: YEN_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_YEN_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_YEN_G_ENABLED = 0x10

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: ZEN_G
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_ZEN_G_DISABLED = 0x00
LSM6DS3_ACC_GYRO_ZEN_G_ENABLED = 0x20

"""
* Register      : CTRL10_C
* Address       : 0X19
* Bit Group Name: FUNC_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FUNC_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_FUNC_EN_ENABLED = 0x04

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: MASTER_ON
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_MASTER_ON_DISABLED = 0x00
LSM6DS3_ACC_GYRO_MASTER_ON_ENABLED = 0x01

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: IRON_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_IRON_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_IRON_EN_ENABLED = 0x02

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: PASS_THRU_MODE
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PASS_THRU_MODE_DISABLED = 0x00
LSM6DS3_ACC_GYRO_PASS_THRU_MODE_ENABLED = 0x04

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: PULL_UP_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PULL_UP_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_PULL_UP_EN_ENABLED = 0x08

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: START_CONFIG
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_START_CONFIG_XL_G_DRDY = 0x00
LSM6DS3_ACC_GYRO_START_CONFIG_EXT_INT2 = 0x10

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: DATA_VAL_SEL_FIFO
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DATA_VAL_SEL_FIFO_XL_G_DRDY = 0x00
LSM6DS3_ACC_GYRO_DATA_VAL_SEL_FIFO_SHUB_DRDY = 0x40

"""
* Register      : MASTER_CONFIG
* Address       : 0X1A
* Bit Group Name: DRDY_ON_INT1
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_DRDY_ON_INT1_DISABLED = 0x00
LSM6DS3_ACC_GYRO_DRDY_ON_INT1_ENABLED = 0x80

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: Z_WU
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_Z_WU_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_Z_WU_DETECTED = 0x01

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: Y_WU
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_Y_WU_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_Y_WU_DETECTED = 0x02

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: X_WU
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_X_WU_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_X_WU_DETECTED = 0x04

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: WU_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_WU_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_WU_EV_STATUS_DETECTED = 0x08

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: SLEEP_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_SLEEP_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_SLEEP_EV_STATUS_DETECTED = 0x10

"""
* Register      : WAKE_UP_SRC
* Address       : 0X1B
* Bit Group Name: FF_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_FF_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_FF_EV_STATUS_DETECTED = 0x20

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: Z_TAP
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_Z_TAP_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_Z_TAP_DETECTED = 0x01

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: Y_TAP
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_Y_TAP_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_Y_TAP_DETECTED = 0x02

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: X_TAP
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_X_TAP_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_X_TAP_DETECTED = 0x04

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: TAP_SIGN
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_TAP_SIGN_POS_SIGN = 0x00
LSM6DS3_ACC_GYRO_TAP_SIGN_NEG_SIGN = 0x08

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: DOUBLE_TAP_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DOUBLE_TAP_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DOUBLE_TAP_EV_STATUS_DETECTED = 0x10

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: SINGLE_TAP_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_SINGLE_TAP_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_SINGLE_TAP_EV_STATUS_DETECTED = 0x20

"""
* Register      : TAP_SRC
* Address       : 0X1C
* Bit Group Name: TAP_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_TAP_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_TAP_EV_STATUS_DETECTED = 0x40

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_XL
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_XL_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_XL_DETECTED = 0x01

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_XH
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_XH_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_XH_DETECTED = 0x02

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_YL
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_YL_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_YL_DETECTED = 0x04

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_YH
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_YH_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_YH_DETECTED = 0x08

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_ZL
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_ZL_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_ZL_DETECTED = 0x10

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: DSD_ZH
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_DSD_ZH_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_DSD_ZH_DETECTED = 0x20

"""
* Register      : D6D_SRC
* Address       : 0X1D
* Bit Group Name: D6D_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_D6D_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_D6D_EV_STATUS_DETECTED = 0x40

"""
* Register      : STATUS_REG
* Address       : 0X1E
* Bit Group Name: XLDA
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_XLDA_NO_DATA_AVAIL = 0x00
LSM6DS3_ACC_GYRO_XLDA_DATA_AVAIL = 0x01

"""
* Register      : STATUS_REG
* Address       : 0X1E
* Bit Group Name: GDA
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_GDA_NO_DATA_AVAIL = 0x00
LSM6DS3_ACC_GYRO_GDA_DATA_AVAIL = 0x02

"""
* Register      : STATUS_REG
* Address       : 0X1E
* Bit Group Name: EV_BOOT
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_EV_BOOT_NO_BOOT_RUNNING = 0x00
LSM6DS3_ACC_GYRO_EV_BOOT_BOOT_IS_RUNNING = 0x08

"""
* Register      : FIFO_STATUS1
* Address       : 0X3A
* Bit Group Name: DIFF_FIFO
* Permission    : RO
"""
LSM6DS3_ACC_GYRO_DIFF_FIFO_STATUS1_MASK = 0xFF
LSM6DS3_ACC_GYRO_DIFF_FIFO_STATUS1_POSITION = 0
LSM6DS3_ACC_GYRO_DIFF_FIFO_STATUS2_MASK = 0xF
LSM6DS3_ACC_GYRO_DIFF_FIFO_STATUS2_POSITION = 0

"""
* Register      : FIFO_STATUS2
* Address       : 0X3B
* Bit Group Name: FIFO_EMPTY
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_FIFO_EMPTY_FIFO_NOT_EMPTY = 0x00
LSM6DS3_ACC_GYRO_FIFO_EMPTY_FIFO_EMPTY = 0x10

"""
* Register      : FIFO_STATUS2
* Address       : 0X3B
* Bit Group Name: FIFO_FULL
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_FIFO_FULL_FIFO_NOT_FULL = 0x00
LSM6DS3_ACC_GYRO_FIFO_FULL_FIFO_FULL = 0x20

"""
* Register      : FIFO_STATUS2
* Address       : 0X3B
* Bit Group Name: OVERRUN
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_OVERRUN_NO_OVERRUN = 0x00
LSM6DS3_ACC_GYRO_OVERRUN_OVERRUN = 0x40

"""
* Register      : FIFO_STATUS2
* Address       : 0X3B
* Bit Group Name: WTM
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_WTM_BELOW_WTM = 0x00
LSM6DS3_ACC_GYRO_WTM_ABOVE_OR_EQUAL_WTM = 0x80

"""
* Register      : FIFO_STATUS3
* Address       : 0X3C
* Bit Group Name: FIFO_PATTERN
* Permission    : RO
"""
LSM6DS3_ACC_GYRO_FIFO_STATUS3_PATTERN_MASK = 0xFF
LSM6DS3_ACC_GYRO_FIFO_STATUS3_PATTERN_POSITION = 0
LSM6DS3_ACC_GYRO_FIFO_STATUS4_PATTERN_MASK = 0x03
LSM6DS3_ACC_GYRO_FIFO_STATUS4_PATTERN_POSITION = 0

"""
* Register      : FUNC_SRC
* Address       : 0X53
* Bit Group Name: SENS_HUB_END
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_SENS_HUB_END_STILL_ONGOING = 0x00
LSM6DS3_ACC_GYRO_SENS_HUB_END_OP_COMPLETED = 0x01

"""
* Register      : FUNC_SRC
* Address       : 0X53
* Bit Group Name: SOFT_IRON_END
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_SOFT_IRON_END_NOT_COMPLETED = 0x00
LSM6DS3_ACC_GYRO_SOFT_IRON_END_COMPLETED = 0x02

"""
* Register      : FUNC_SRC
* Address       : 0X53
* Bit Group Name: PEDO_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_PEDO_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_PEDO_EV_STATUS_DETECTED = 0x10

"""
* Register      : FUNC_SRC
* Address       : 0X53
* Bit Group Name: TILT_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_TILT_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_TILT_EV_STATUS_DETECTED = 0x20

"""
* Register      : FUNC_SRC
* Address       : 0X53
* Bit Group Name: SIGN_MOT_EV_STATUS
* Permission    : RO
"""

LSM6DS3_ACC_GYRO_SIGN_MOT_EV_STATUS_NOT_DETECTED = 0x00
LSM6DS3_ACC_GYRO_SIGN_MOT_EV_STATUS_DETECTED = 0x40

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: LIR
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_LIR_DISABLED = 0x00
LSM6DS3_ACC_GYRO_LIR_ENABLED = 0x01

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: TAP_Z_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TAP_Z_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TAP_Z_EN_ENABLED = 0x02

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: TAP_Y_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TAP_Y_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TAP_Y_EN_ENABLED = 0x04

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: TAP_X_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TAP_X_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TAP_X_EN_ENABLED = 0x08

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: TILT_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TILT_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TILT_EN_ENABLED = 0x20

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: PEDO_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_PEDO_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_PEDO_EN_ENABLED = 0x40

"""
* Register      : TAP_CFG1
* Address       : 0X58
* Bit Group Name: TIMER_EN
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TIMER_EN_DISABLED = 0x00
LSM6DS3_ACC_GYRO_TIMER_EN_ENABLED = 0x80

"""
* Register      : TAP_THS_6D
* Address       : 0X59
* Bit Group Name: TAP_THS
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_TAP_THS_MASK = 0x1F
LSM6DS3_ACC_GYRO_TAP_THS_POSITION = 0

"""
* Register      : TAP_THS_6D
* Address       : 0X59
* Bit Group Name: SIXD_THS
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SIXD_THS_80_degree = 0x00
LSM6DS3_ACC_GYRO_SIXD_THS_70_degree = 0x20
LSM6DS3_ACC_GYRO_SIXD_THS_60_degree = 0x40
LSM6DS3_ACC_GYRO_SIXD_THS_50_degree = 0x60

"""
* Register      : INT_DUR2
* Address       : 0X5A
* Bit Group Name: SHOCK
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_SHOCK_MASK = 0x03
LSM6DS3_ACC_GYRO_SHOCK_POSITION = 0

"""
* Register      : INT_DUR2
* Address       : 0X5A
* Bit Group Name: QUIET
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_QUIET_MASK = 0x0C
LSM6DS3_ACC_GYRO_QUIET_POSITION = 2

"""
* Register      : INT_DUR2
* Address       : 0X5A
* Bit Group Name: DUR
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_DUR_MASK = 0xF0
LSM6DS3_ACC_GYRO_DUR_POSITION = 4

"""
* Register      : WAKE_UP_THS
* Address       : 0X5B
* Bit Group Name: WK_THS
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_WK_THS_MASK = 0x3F
LSM6DS3_ACC_GYRO_WK_THS_POSITION = 0

"""
* Register      : WAKE_UP_THS
* Address       : 0X5B
* Bit Group Name: INACTIVITY_ON
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INACTIVITY_ON_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INACTIVITY_ON_ENABLED = 0x40

"""
* Register      : WAKE_UP_THS
* Address       : 0X5B
* Bit Group Name: SINGLE_DOUBLE_TAP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_SINGLE_DOUBLE_TAP_DOUBLE_TAP = 0x00
LSM6DS3_ACC_GYRO_SINGLE_DOUBLE_TAP_SINGLE_TAP = 0x80

"""
* Register      : WAKE_UP_DUR
* Address       : 0X5C
* Bit Group Name: SLEEP_DUR
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_SLEEP_DUR_MASK = 0x0F
LSM6DS3_ACC_GYRO_SLEEP_DUR_POSITION = 0

"""
* Register      : WAKE_UP_DUR
* Address       : 0X5C
* Bit Group Name: TIMER_HR
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_TIMER_HR_6_4ms = 0x00
LSM6DS3_ACC_GYRO_TIMER_HR_25us = 0x10

"""
* Register      : WAKE_UP_DUR
* Address       : 0X5C
* Bit Group Name: WAKE_DUR
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_WAKE_DUR_MASK = 0x60
LSM6DS3_ACC_GYRO_WAKE_DUR_POSITION = 5

"""
* Register      : FREE_FALL
* Address       : 0X5D
* Bit Group Name: FF_DUR
* Permission    : RW
"""
LSM6DS3_ACC_GYRO_FF_FREE_FALL_DUR_MASK = 0xF8
LSM6DS3_ACC_GYRO_FF_FREE_FALL_DUR_POSITION = 3
LSM6DS3_ACC_GYRO_FF_WAKE_UP_DUR_MASK = 0x80
LSM6DS3_ACC_GYRO_FF_WAKE_UP_DUR_POSITION = 7

"""
* Register      : FREE_FALL
* Address       : 0X5D
* Bit Group Name: FF_THS
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_FF_THS_5 = 0x00
LSM6DS3_ACC_GYRO_FF_THS_7 = 0x01
LSM6DS3_ACC_GYRO_FF_THS_8 = 0x02
LSM6DS3_ACC_GYRO_FF_THS_10 = 0x03
LSM6DS3_ACC_GYRO_FF_THS_11 = 0x04
LSM6DS3_ACC_GYRO_FF_THS_13 = 0x05
LSM6DS3_ACC_GYRO_FF_THS_15 = 0x06
LSM6DS3_ACC_GYRO_FF_THS_16 = 0x07

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_TIMER
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_TIMER_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_TIMER_ENABLED = 0x01

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_TILT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_TILT_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_TILT_ENABLED = 0x02

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_6D
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_6D_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_6D_ENABLED = 0x04

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_TAP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_TAP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_TAP_ENABLED = 0x08

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_FF
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_FF_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_FF_ENABLED = 0x10

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_WU
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_WU_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_WU_ENABLED = 0x20

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_SINGLE_TAP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_SINGLE_TAP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_SINGLE_TAP_ENABLED = 0x40

"""
* Register      : MD1_CFG
* Address       : 0X5E
* Bit Group Name: INT1_SLEEP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT1_SLEEP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT1_SLEEP_ENABLED = 0x80

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_TIMER
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_TIMER_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_TIMER_ENABLED = 0x01

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_TILT
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_TILT_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_TILT_ENABLED = 0x02

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_6D
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_6D_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_6D_ENABLED = 0x04

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_TAP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_TAP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_TAP_ENABLED = 0x08

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_FF
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_FF_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_FF_ENABLED = 0x10

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_WU
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_WU_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_WU_ENABLED = 0x20

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_SINGLE_TAP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_SINGLE_TAP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_SINGLE_TAP_ENABLED = 0x40

"""
* Register      : MD2_CFG
* Address       : 0X5F
* Bit Group Name: INT2_SLEEP
* Permission    : RW
"""

LSM6DS3_ACC_GYRO_INT2_SLEEP_DISABLED = 0x00
LSM6DS3_ACC_GYRO_INT2_SLEEP_ENABLED = 0x80
