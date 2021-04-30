#-*- coding:utf-8 -*-
import serial 
from threading import Thread
import time
import conshell_parameters

class ConshellSerialManager(Thread):
   
    def __init__(self, serial_port):

        Thread.__init__(self)
        self.seq = serial.Serial(
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.seq.port = serial_port
        self.is_serial_running = False
        self.daemon = True
        self.command = None

    def set_D1_lamp(self, value):
        if value == False:
            self.seq.write(str.encode("a0r\n"))
        else:
            self.seq.write(str.encode("a1\r\n"))
       
    def run(self):
        
        while True: 
            if self.seq.isOpen() == True:  
                try:
                    if self.seq.inWaiting():
                        try:
                            
                            self.command = self.seq.readline()
                            cmd_temp = self.command.decode()
                            cmd_sub = cmd_temp[:(len(cmd_temp)-2)]
                            print(cmd_sub)
                            if cmd_sub[0] == 'a':
                                a = cmd_sub.index('a')
                                b = cmd_sub.index('b')
                                c = cmd_sub.index('c')
                                d = cmd_sub.index('d')
                                e = cmd_sub.index('e')
                                conshell_parameters.A2_weight = float(cmd_sub[a+1:b])
                                conshell_parameters.A0_temp = float(cmd_sub[b+1:c])
                                conshell_parameters.A1_humid = float(cmd_sub[c+1:d])
                                conshell_parameters.D2_door = int(cmd_sub[d+1:e])
                         
                        except AttributeError:
                            print("attr error")

                        
                except IOError:
                    print("IO error")

    def open_port(self):
        if self.seq.isOpen() == False:
            self.seq.open()

    def close_port(self):
        if self.seq.isOpen() == True:
            self.seq.close()

    def is_seq_open(self):
        if self.seq.isOpen() == True:
            return True
        else:
            return False

    def get_serial_port(self):
        return self.seq.port

    def get_serial_data(self):
        return self.command

if __name__ =='__main__':
    ser_manager = SerialManager("/dev/ttyUSB0")
    ser_manager.open_port()
    ser_manager.run()
