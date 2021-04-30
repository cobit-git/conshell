import struct 
import conshell_parameters

class ProtocolSystemIDSet():

    def __init__(self):
        # header 
        self.STX = 0x0203
        self.CMD = 0x13
        self.dummy = 0xff
        self.mode = 0x00
        self.result = 0x00
        self.CRC = 0xffff
        self.len = 0x00
        '''
        # body
        self.ProjectID = 0
        self.ProjectTitle = "conshaell"
        self.CageID = 0
        self.autoInterval = 0
        self.distCalcRate  = 0
        self.start_year = 2021        # 2 byte 
        self.start_month = 4          # 1 byte
        self.start_date = 28           # 1 byte
        self.start_hour = 12          # 1 byte
        self.start_minute = 0         # 1 byte 
        self.start_second = 0         # 1 byte 
        self.stop_year = 2021        # 2 byte 
        self.stop_month = 4          # 1 byte
        self.stop_date = 28           # 1 byte
        self.stop_hour = 12          # 1 byte
        self.stop_minute = 0         # 1 byte 
        self.stop_second = 0         # 1 byte 
        '''
    '''
    def make_system_set_pack(self):
        data1 = self.make_system_set_header()
        data2 = self.make_system_set_body()
        return data1+data2
    '''
    def make_system_set_header(self):
        value =  (self.STX, self.CMD, self.dummy, self.mode, self.result, self.CRC, self.len)
        fmt = '>H B B B B H B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value) 

    def parsing_system_set(self, data):
        print(data)
        fmt = '>H B B B B H B H 40p H B f H B B B B B H B B B B B '.format()
        unpack_data = struct.unpack(fmt, data)
        conshell_parameters.ProjectID = int(unpack_data[7])
        conshell_parameters.ProjectName = unpack_data[8].decode()
        conshell_parameters.CageID = int(unpack_data[9])
        conshell_parameters.autoInterval = int(unpack_data[10])
        conshell_parameters.distCalcRate = round(float(unpack_data[11]), 2)
        conshell_parameters.start_year = int(unpack_data[12])
        conshell_parameters.start_month = int(unpack_data[13])
        conshell_parameters.start_date = int(unpack_data[14])
        conshell_parameters.start_hour = int(unpack_data[15])
        conshell_parameters.start_minute = int(unpack_data[16])
        conshell_parameters.start_second = int(unpack_data[17])
        conshell_parameters.stop_year = int(unpack_data[12])
        conshell_parameters.stop_month = int(unpack_data[13])
        conshell_parameters.stop_date = int(unpack_data[14])
        conshell_parameters.stop_hour = int(unpack_data[15])
        conshell_parameters.stop_minute = int(unpack_data[16])
        conshell_parameters.stop_second = int(unpack_data[17])
        
        print(conshell_parameters.ProjectID)
        print(conshell_parameters.ProjectName)
        print(conshell_parameters.CageID)
        print(conshell_parameters.autoInterval)
        print(conshell_parameters.distCalcRate)
        print(conshell_parameters.start_year)
        print(conshell_parameters.start_month)
        print(conshell_parameters.start_date)
        print(conshell_parameters.start_hour)
        print(conshell_parameters.start_minute)
        print(conshell_parameters.start_second)
        print(conshell_parameters.stop_year)
        print(conshell_parameters.stop_month)
        print(conshell_parameters.stop_date)
        print(conshell_parameters.stop_hour)
        print(conshell_parameters.stop_minute)
        print(conshell_parameters.stop_second)
        
    '''
    def make_system_set_body(self):
        value =  (self.ProjectID, self.ProjectTitle, self.CageID, self.autoInterval, self.distCalcRate, \
                    self.start_year, self.start_month, self.start_date, self.start_hour, self.start_minute, self.start_second,
                    self.stop_year, self.stop_month, self.stop_date, self.stop_hour, self.stop_minute, self.stop_second)
        fmt = '>H 40p H B I H B B B B B H B B B B B '.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)
    '''

if __name__ =='__main__':
    system_set = ProtocolSystemIDSet()
    print(system_set.make_system_set_header())
