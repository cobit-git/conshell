import struct 

class ProtocolSensorControl():
    def __init__(self):
        # header packet
        self.STX = 0x0203
        self.CMD = 0x51
        self.dummy = 0xff
        self.mode = 0x00
        self.result = 0x00
        self.CRC = 0xffff
        self.len = 0x00

        # body 
        #self.sensor_no = 0x00
        #self.sensor_value = 0x00


    # make header packet
    def make_control_header(self):
        value =  (self.STX, self.CMD, self.dummy, self.mode, self.result, self.CRC, self.len)
        fmt = '>H B B B B H B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value) 
 
if __name__ == '__main__':
    control = ProtoconSensorControl()
    #print(control.make_control_pack(self.sensor_no, self.sensor_value))