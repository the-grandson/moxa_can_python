from MXCAN import *
from ctypes import *
from ctypes.wintypes import HANDLE

class Moxa_CAN_IO:

    def __init__(self, PORT=CAN_PORT0, OPMODE=CNIO_OPMODE_SINGLE_ACC, BAUD=B_250K):
        # Structure to be filled with board info
        dev_node_4 = CNIO_DEV_INFO * 4
        dev_node_array = dev_node_4()
        # Load the Moxa .dll
        canlib = cdll.LoadLibrary("mxcanfunc.dll")
        canlib.restype = HANDLE
        self.canlib = canlib
        # Define current status
        self.status = CNIO_SUCCESS.value

        res = canlib.cnio_enum_devices(dev_node_array, CNIO_MAX_BOARDS)
        if res != CNIO_SUCCESS.value:
            self.status = CNIO_STATUS_ERR.value
            print("There is no Moxa CAN board present...")

        # fd0  = cnio_open(dev_node[0].CNIOID, CAN_PORT0);
        fd0 = canlib.cnio_open(dev_node_array[0].CNIOID, CAN_PORT0)
        if fd0 < 0:
            self.status = CNIO_STATUS_ERR.value
            print("Invalid Moxa CAN handler...")

        # ret = cnio_init(fd1, baud_struct.mod, baud_struct.baud);
        ret = canlib.cnio_init(fd0,OPMODE,BAUD)
        if ret != CNIO_SUCCESS.value:
            self.status = CNIO_STATUS_ERR.value
            print("Error on init Moxa CAN board...")
        # Keep the driver handler   
        self.fd0 = fd0

        # ret = cnio_reset(hPort);
        ret = canlib.cnio_reset(fd0)
        if ret != CNIO_SUCCESS.value:
            self.status = CNIO_STATUS_ERR.value
            print("Error on reset Moxa CAN board...")

        status = DWORD(0x0)
        ret = canlib.cnio_status(fd0, byref(status))
        if ret != CNIO_SUCCESS.value:
            self.status = CNIO_STATUS_ERR.value
            print("Error on status Moxa CAN board...")
        print("Moxa CAN init completed, current board status: 0x%x" % status.value)
    
    def set_filters(self, DEFAULT_ACC_ID, DEFAULT_ACM_ID, DEFAULT_OPT):
        # ret = cnio_set_filters(fd1, acc_struct.acc, acc_struct.acm, acc_struct.opt);
        # 0x1fffffff, 0x1fffffff, CNIO_OPT_EXTENDED|CNIO_OPT_ACCEPT_RTR
        ret = self.canlib.cnio_set_filters_ex(self.fd0, DEFAULT_ACC_ID, DEFAULT_ACM_ID, DEFAULT_OPT)
        if ret != CNIO_SUCCESS.value:
            self.status = CNIO_STATUS_ERR.value
            print("Error on setting filters for Moxa CAN board...")

        status = DWORD(0x0)
        ret = self.canlib.cnio_status(self.fd0, byref(status))
        print("Moxa CAN filters set correctly, current CAN board status: 0x%x" % status.value)
        return CNIO_SUCCESS
    
    def start_board(self):
        # ret = cnio_start(fd1);
        if(self.status == CNIO_SUCCESS.value):
            ret = self.canlib.cnio_start(self.fd0)
            if ret != CNIO_SUCCESS.value:
                self.status = CNIO_STATUS_ERR.value
                print("Error on starting the Moxa CAN board...")
        else:
            print("Can not start Moxa CAN board, current status is error...")
        
    def read_msg(self, timeout=0):
        if(self.status == CNIO_SUCCESS.value):
            # ret = cnio_receive_message(fd1, &rx_frame, INFINITE);
            timeout = DWORD(timeout)
            rx_frame = CNIO_MSG()

            ret = self.canlib.cnio_receive_message(self.fd0, byref(rx_frame), timeout)
            if ret != CNIO_SUCCESS.value:
                if ret == E_RX_TIMEOUT.value:
                    print("Moxa CAN board reading function timeout: %d"
                      % (ret))
                else:
                    print("Moxa CAN board reading function, Error Code: %d"
                        % (ret))
            
            if rx_frame.FrameType == CNIO_ERROR_FRAME.value:
                print("Bus error occured, Bus Error Code: 0x%x", rx_frame.Data[0])

            print(" ******** Rx Message ******** ")
            print("Data Frame Id      = 0x%x" % (rx_frame.ID))
            print("Data Frame Type    = 0x%x" % (rx_frame.FrameType))
            print("Data Frame Len     = %u" % (rx_frame.Length))
            for i in range(8):
                print("Data Frame Data [%d] = (0x%x)" % (i, rx_frame.Data[i]))
            print(" **************************** ")
            return rx_frame
    
    def stop_board(self):
        # ret = cnio_stop(hPort)
        ret = self.canlib.cnio_stop(self.fd0)
        if ret != CNIO_SUCCESS.value:
            print("Error on stop the Moxa CAN board...")
        
    def close_board(self):
        # cnio_close(fd1);
        self.canlib.cnio_close(self.fd0)
