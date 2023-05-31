from ctypes import c_int
from ctypes.wintypes import LONG, BYTE, CHAR, WORD, DWORD

#define CAN_PORT0  0
CAN_PORT0 = LONG(0)
#define CAN_PORT1  1
CAN_PORT1 = LONG(1)
#define CNIO_MAX_BOARDS			4
CNIO_MAX_BOARDS = LONG(4)
#define CNIO_MAX_PORTS_PER_BOARD	2
CNIO_MAX_PORTS_PER_BOARD = LONG(2)
#define CNIO_SUCCESS				1
CNIO_SUCCESS = c_int(1)

#define CNIO_OPMODE_LISTEN_ONLY	0x01
CNIO_OPMODE_LISTEN_ONLY = BYTE(0x01)
#define CNIO_OPMODE_SELF_TEST		0x02
CNIO_OPMODE_SELF_TEST = BYTE(0x02)
#define CNIO_OPMODE_SINGLE_ACC	0x00
CNIO_OPMODE_SINGLE_ACC = BYTE(0x00)
#define CNIO_OPMODE_DUAL_ACC		0x04
CNIO_OPMODE_DUAL_ACC = BYTE(0x04)
#define CNIO_OPMODE_ERROR_FRAME	0x08
CNIO_OPMODE_ERROR_FRAME = BYTE(0x08)

#define CNIO_OPT_STANDARD			0x00
CNIO_OPT_STANDARD = BYTE(0x00)
#define CNIO_OPT_EXTENDED			0x01
CNIO_OPT_EXTENDED = BYTE(0x01)
#define CNIO_OPT_ACCEPT_RTR		0x02
CNIO_OPT_ACCEPT_RTR = BYTE(0x02)
#define CNIO_OPT_ACCEPT_RTR_ONLY	0x04
CNIO_OPT_ACCEPT_RTR_ONLY = BYTE(0x04)

#define CNIO_STANDARD_FRAME		0x00
CNIO_STANDARD_FRAME = BYTE(0x00)
#define CNIO_EXTENDED_FRAME		0x80
CNIO_EXTENDED_FRAME = BYTE(0x80)
#define CNIO_ERROR_FRAME			0x20
CNIO_ERROR_FRAME = BYTE(0x20)
#define CNIO_RTR					0x40
CNIO_RTR = BYTE(0x40)
#define CNIO_SRR					0x10
CNIO_SRR = BYTE(0x10)

#define B_10K						0x311C
B_10K = WORD(0x311C)
#define B_20K						0x181C
B_20K = WORD(0x181C)
#define B_50K						0x091C
B_50K = WORD(0x091C)
#define B_100K						0x041C
B_100K = WORD(0x041C)
#define B_125K						0x031C
B_125K = WORD(0x031C)
#define B_250K						0x011C
B_250K = WORD(0x011C)
#define B_500K						0x001C
B_500K = WORD(0x001C)
#define B_800K						0x0016
B_800K = WORD(0x0016)
#define B_1000K						0x0014
B_1000K = WORD(0x0014)

#define DEFAULT_ACC_ID		0xffffffff
DEFAULT_ACC_ID = DWORD(0xffffffff)
#define DEFAULT_ACM_ID		0xffffffff
DEFAULT_ACM_ID = DWORD(0xffffffff)
#define DEFAULT_OPT			CNIO_EXTENDED_FRAME
DEFAULT_OPT = BYTE(CNIO_OPT_EXTENDED.value | CNIO_OPT_ACCEPT_RTR.value)

# typedef struct _CNIO_DEV_INFO_STRUCT
# {
# 	DWORD CNIOID;
# 	DWORD Reserved;
# 	CHAR ProductName[32];
# 	CHAR DriverName[32];
# 	CHAR DeviceLocation[32];
# 	BYTE PortCount;
# } CNIO_DEV_INFO, *PCNIO_DEV_INFO;

class CNIO_DEV_INFO(Structure):

    _fields_ = [("CNIOID", DWORD),
                ("Reserved", DWORD),
                ("ProductName", CHAR * 32),
                ("DriverName", CHAR * 32),
                ("DeviceLocation", CHAR * 32),
                ("PortCount", BYTE)]
    
# typedef struct _CNIO_MSG_STRUCT
# {
# 	DWORD ID;
# 	BYTE FrameType;
# 	BYTE Length;
# 	BYTE Data[8];
# } CNIO_MSG, *PCNIO_MSG;

class CNIO_MSG(Structure):

    _fields_ = [("ID", DWORD),
                ("FrameType", BYTE),
                ("Length", BYTE),
                ("Data", BYTE * 8)]


CNIO_STATUS_ERR = DWORD(0x00)
#define CNIO_STATUS_TX_PENDING	0x20
CNIO_STATUS_TX_PENDING = DWORD(0x20)
#define CNIO_STATUS_OVRRUN		0x02
CNIO_STATUS_OVRRUN = DWORD(0x02)
#define CNIO_STATUS_ERRLIM			0x40
CNIO_STATUS_ERRLIM = DWORD(0x40)
#define CNIO_STATUS_BUS_OFF		0x80
CNIO_STATUS_BUS_OFF = DWORD(0x80)
#define CNIO_STATUS_RESET_MODE	0x0100
CNIO_STATUS_BUS_OFF = DWORD(0x100)

#define E_ACCESS_DEVICE_FAILED							(-1)
E_ACCESS_DEVICE_FAILED = c_int(-1)
#define E_TX_FAILED										(-2)
E_TX_FAILED = c_int(-2)
#define E_RX_FAILED										(-3)
E_RX_FAILED = c_int(-3)
#define E_TX_TIMEOUT									(-4)
E_TX_TIMEOUT = c_int(-4)
#define E_RX_TIMEOUT									(-5)
E_RX_TIMEOUT = c_int(-5)
#define E_INVALID_ACC_ID_CODE_VALUE					(-6)
E_INVALID_ACC_ID_CODE_VALUE = c_int(-6)
#define E_INVALID_ACC_ID_MASK_VALUE					(-7)
E_INVALID_ACC_ID_MASK_VALUE = c_int(-7)
#define E_INVALID_SIZE_VALUE							(-8)
E_INVALID_SIZE_VALUE = c_int(-8)
#define E_INVALID_OPERATION							(-9)
E_INVALID_OPERATION = c_int(-9)
#define E_WIN32_FAILED									(-10)
E_WIN32_FAILED = c_int(-10)