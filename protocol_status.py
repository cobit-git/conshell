import struct
import conshell_parameters

class ProtocolStatus():

    def __init__(self):

        # header packet
        self.STX = 0x0203
        self.CMD = 0x51
        self.dummy = 0xff 
        self.mode = 0x00
        self.result = 0x00
        self.CRC = 0xffff
        self.len = 0x00
        '''
        # status packet 
        self.ProjectID = 0x00
        self.CageID = 0x00
        self.Mode = 0x03
        self.tempDistance = 0x234
        self.highTemp = 0x123
        self.tempPointX = 0x04
        self.tempPointY = 0x02
        self.camDistance = 0x00
        self.camPointX = 0x00
        self.camPointY = 0x00
        self.tickTotCnt = 0x345
        self.statusDI = 0x30
        self.statusAI = 0x03
        self.AI_0 = 0x00
        self.AI_1 = 0x00
        self.AI_2 = 0x00
        self.AI_3 = 0x00
        self.AI_4 = 0x00
        self.AI_5 = 0x00
        self.AI_6 = 0x00
        self.AI_7 = 0x00
        self.AI_8 = 0x00
        self.AI_9 = 0x00
        self.AI_10 = 0x00
        self.AI_11 = 0x00
        self.AI_12 = 0x00
        self.AI_13 = 0x00
        self.AI_14 = 0x00
        self.AI_15 = 0x00
        self.AI_16 = 0x00
        self.DI_0 = 0x00
        self.DI_1 = 0x00
        self.DI_2 = 0x00
        self.DI_3 = 0x00
        self.DI_4 = 0x00
        self.DI_5 = 0x00
        self.DI_6 = 0x00
        self.DI_7 = 0x00
        self.DI_8 = 0x00
        self.DI_9 = 0x00
        self.DI_10 = 0x00
        self.DI_11 = 0x00
        self.DI_12 = 0x00
        self.DI_13 = 0x00
        self.DI_14 = 0x00
        self.DI_15 = 0x00
        self.DI_16 = 0x00
        '''


    # make header packet
    def make_status_header(self):
        value =  (self.STX, self.CMD, self.dummy, self.mode, self.result, self.CRC, self.len)
        fmt = '>H B B B B H B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value) 

    #make status packet 
    def make_status_body(self):
        value =  (conshell_parameters.ProjectID, conshell_parameters.CageID , conshell_parameters.Mode, conshell_parameters.tempDistance, conshell_parameters.highTemp, \
            conshell_parameters.tempPointX, conshell_parameters.tempPointY, conshell_parameters.camDistance, conshell_parameters.camPointX, conshell_parameters.camPointY, conshell_parameters.tickTotCnt, conshell_parameters.statusDI, conshell_parameters.statusAI)
        fmt = '>H H B I f H H I H H I H H'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)

    #make AI sensor data 
    def make_AI_sensor(self):
        value =  (conshell_parameters.A0_temp, conshell_parameters.A1_humid, conshell_parameters.A2_weight, conshell_parameters.A3, conshell_parameters.A4, conshell_parameters.A5, conshell_parameters.A6,conshell_parameters.A7, conshell_parameters.A8, conshell_parameters.A9, conshell_parameters.A10, conshell_parameters.A11, conshell_parameters.A12, conshell_parameters.A13, conshell_parameters.A14, conshell_parameters.A15, conshell_parameters.A16)
        fmt = '>f f f I I I I I I I I I I I I I I'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)

    #make DI sensor data 
    def make_DI_sensor(self):
        value = (conshell_parameters.D0, conshell_parameters.D1_lamp, conshell_parameters.D2_door, conshell_parameters.D3, conshell_parameters.D4, conshell_parameters.D5, conshell_parameters.D6, conshell_parameters.D7, conshell_parameters.D8, conshell_parameters.D9, conshell_parameters.D10,conshell_parameters.D11,conshell_parameters.D12, conshell_parameters.D13, conshell_parameters.D14,conshell_parameters.D15,conshell_parameters.D16)
        fmt = 'B B B B B B B B B B B B B B B B B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)

    def make_status_pack(self):
        data1 = self.make_status_header()
        data2 = self.make_status_body()
        data3 = self.make_AI_sensor()
        data4 = self.make_DI_sensor()
        return data1+data2+data3+data4

if __name__ == '__main__':
    status = ProtocolStatus()
    print(status.make_status_pack())