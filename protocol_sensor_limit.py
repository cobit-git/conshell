import struct

class ProtocolSensorLimit():

    def __init__(self):
        self.STX = 0x0203
        self.CMD_ASK = 0x32
        self.dummy = 0xff
        self.mode = 0x00
        self.result = 0x00
        self.CRC = 0xffff
        self.len = 0x00
        self.repeatCnt = 0x00
        self.sensorNum = 0x00
        self.lowerLimit = 0x1234
        self.upperLimit = 0x2345
        self.isUsing = 0x000
        self.currentValue = 0x03456

    def make_ask_limit_pack(self):
        data1 = self.make_ask_limit_header()
        data2 = self.make_ask_limit_sensor()
        return data1+data2
    
    def make_ask_limit_header(self):
        value =  (self.STX, self.CMD_ASK, self.dummy, self.mode, self.result, self.CRC, self.len)
        fmt = '>H B B B B H B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value) 

    def make_ask_limit_sensor(self):
        value =  (self.repeatCnt, self.sensorNum, self.lowerLimit, self.upperLimit, self.isUsing, self.currentValue)
        fmt = '>B B H H B H'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)
    
if __name__ == '__main__':

    sensor = SensorLimitProtocol()
    print(sensor.make_ask_limit_pack())

