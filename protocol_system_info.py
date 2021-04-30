import struct
import conshell_parameters
import netifaces as ni 

class ProtocolSystemInfo():

    def __init__(self):
        # header 
        self.STX = 0x0203
        self.CMD = 0x32
        self.dummy = 0xff
        self.mode = 0x00
        self.result = 0x00
        self.CRC = 0xffff
        self.len = 0x00
        # body 
        '''
        self.ProjectID = 0x00
        self.ProjectName = b''
        self.CageID = 0x00
        self.mcuIP = b''
        self.mcuSubnet = b'' 
        self.mcuGateway = b''
        self.wifiOnOff = 0x00
        self.wifiSSID = b''
        self.wifiPass = b''
        self.wifiIP = b''
        self.wifiSubnet = b''
        self.wifiGateway = b''
        self.selfDummy2 = b''
        self.mcuTime = b''
        self.autoInterval = 0x00
        self.distCalcRate = 0x00
        self.startLab = b''
        self.stopLab = b''
        self.firmVer = b''
        self.modelName = b'' 
        '''

    def make_system_pack(self):
        data1 = self.make_system_header()
        data2 = self.make_system_body()
        return data1+data2
    
    def make_system_header(self):
        value =  (self.STX, self.CMD, self.dummy, self.mode, self.result, self.CRC, self.len)
        fmt = '>H B B B B H B'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value) 

    def make_system_body(self):
        conshell_parameters.mcuIP = str(ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'])
        conshell_parameters.mcuGateway = str(ni.gateways()[ni.AF_INET][0][0])
        print(conshell_parameters.mcuIP)
        print(conshell_parameters.mcuGateway )
        value = (conshell_parameters.ProjectID,  conshell_parameters.ProjectName.encode(), conshell_parameters.CageID, conshell_parameters.mcuIP.encode(), conshell_parameters.mcuSubnet.encode(), \
                conshell_parameters.mcuGateway.encode(), conshell_parameters.wifiOnOff, conshell_parameters.wifiSSID.encode(), conshell_parameters.wifiPass.encode(), conshell_parameters.wifiIP.encode(), \
                conshell_parameters.wifiSubnet.encode(), conshell_parameters.wifiGateway.encode(), conshell_parameters.dummy.encode(), \
                conshell_parameters.mcuTime_y, conshell_parameters.mcuTime_mo, conshell_parameters.mcuTime_d, conshell_parameters.mcuTime_h, conshell_parameters.mcuTime_mi, conshell_parameters.mcuTime_s,  \
                conshell_parameters.autoInterval, conshell_parameters.distCalcRate, conshell_parameters.start_year, conshell_parameters.start_month, conshell_parameters.start_date, \
                conshell_parameters.start_hour, conshell_parameters.start_minute, conshell_parameters.start_second, conshell_parameters.stop_year, conshell_parameters.stop_month, conshell_parameters.stop_date, \
                conshell_parameters.stop_hour, conshell_parameters.stop_minute, conshell_parameters.stop_second, conshell_parameters.firmVer.encode(), conshell_parameters.modelName.encode())
        fmt = '>H 40p H 4p 4p 4p B 10p 10p 4p 4p 4p 15p H B B B B B B f H B B B B B H B B B B B 10p 10p'.format()
        packer = struct.Struct(fmt)
        return packer.pack(*value)
    
if __name__ == '__main__':

    system = SystemInfoProtocol()
    print(system.make_system_pack())
