import socket 
import threading 
import struct
import netifaces as ni 
import time
import conshell_parameters 
from conshell_serial_manager import ConshellSerialManager
from conshell_amg8833 import ConshellAmg8833
from protocol_status import ProtocolStatus
from protocol_system_info import ProtocolSystemInfo
from protocol_sensor_limit import ProtocolSensorLimit
from protocol_sensor_control import ProtocolSensorControl
from protocol_system_ID_set import ProtocolSystemIDSet
from conshell_OLED import ConshellOLED
from conshell_video_server import ConshellVideoServer


class ConshellCommandServer(object):
    def __init__(self):
        self.ip_addr = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host_ip = self.ip_addr # server IP address
        self.port = 9998 # server port address 
        self.sock.bind((self.host_ip, self.port))
        self.proto_status = ProtocolStatus()
        self.proto_system_info = ProtocolSystemInfo()
        self.proto_limit = ProtocolSensorLimit()
        self.proto_control = ProtocolSensorControl()
        self.proto_system_set = ProtocolSystemIDSet()
        self.oled = ConshellOLED()

    def listen(self):
        print("Conshell cmd server listen...")
        self.sock.listen(5)
        while True:
            self.client, self.address = self.sock.accept()
            print('Command server: new clinet from: ', self.address)
            threading.Thread(target = self.listenToClient, args = (self.client, self.address)).start()

    def listenToClient(self, client, address):
        print("Conshell cmd server thread running...")
        if self.client:
            while True:
                try:
                    data = self.client.recv(1024)
                    print(data)
                    if data is not None:
                        
                        if data[2] == 0x51:
                            print('Request status: received from ' + address[0],':',address[1] , data)
                            conshell_parameters.tempPointX, conshell_parameters.tempPointY = heat_sensor.get_max_temp_point()
                            conshell_parameters.highTemp = heat_sensor.get_max_temp()
                            cmd = self.proto_status.make_status_pack()
                            self.client.send(cmd) 
                        elif data[2] == 0x14:
                            print('Request system info received from ' + address[0],':',address[1] , data)
                            cmd = self.proto_system_info.make_system_pack()
                            self.client.send(cmd) 

                        elif data[2] == 0x32:
                            print('Request limit info received from ' + address[0],':',address[1] , data)
                            cmd = self.proto_limit.make_ask_limit_pack()
                            self.client.send(cmd) 

                        elif data[2] == 0x21:
                            print(len(data))
                            '''
                                sensor do_control: if adding sensor, add if else statement for sensor. 
                            '''
                            if data[9] == 1:  # D1 lamp sensor 
                                if data[10] == 0x01:
                                    conshell_parameters.D1_lamp = 1
                                    ser_manager.set_D1_lamp(True)
                                else:
                                    conshell_parameters.D1_lamp = 0
                                    ser_manager.set_D1_lamp(False)
                            # send  response packet
                            cmd = self.proto_control.make_control_header()
                            self.client.send(cmd)

                        elif data[2] == 0x13:
                            self.proto_system_set.parsing_system_set(data)
                            cmd = self.proto_system_set.make_system_set_header()
                            self.client.send(cmd)

                        if not data: 
                            print('Disconnected by ' + address[0],':',address[1])
                            break
                   
                except ConnectionResetError as e:
                    print('Disconnected by ' + address[0],':',address[1])
                    break 
            self.client.close()

    def disp_IP_oled(self):
        self.oled.clear_display()
        self.oled.draw_small_text("IP ADDRESS", 0, 0)
        self.oled.draw_small_text(str(self.host_ip), 0, 15)
        self.oled.update_display()

def test():
    print(heat_sensor.get_heat_pixels())
    print(ser_manager.get_serial_data())

def get_projectID():
    return 0x0101

def get_cageID():
    return 0x0202

if __name__ == '__main__':
    cmd_server = ConshellCommandServer()
    cmd_server.disp_IP_oled()
    ser_manager = ConshellSerialManager("/dev/ttyUSB0")
    ser_manager.start()
    ser_manager.open_port()
    heat_sensor = ConshellAmg8833()
    heat_sensor.start()
    
    #video_server = ConshellVideoServer('172.31.99.111', 9999)
    #video_server.listen()
    cmd_server.listen()
    cmd_server.close(0)



