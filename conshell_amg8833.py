import time,sys
sys.path.append('../')
import amg8833_i2c
import numpy as np
from threading import Thread
pix_to_read = 64 # read all 64 pixels
class ConshellAmg8833(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        t0 = time.time()
        self.sensor = []
        self.pixels = []
        self.max = 0 
        self.high_index = 0 
        self.high_x = 0
        self.high_y = 0
        while (time.time()-t0)<1: # wait 1sec for sensor to start
            try:
                # AD0 = GND, addr = 0x68 | AD0 = 5V, addr = 0x69
                self.sensor = amg8833_i2c.AMG8833(addr=0x69) # start AMG8833
            except:
                self.sensor = amg8833_i2c.AMG8833(addr=0x68)
            finally:
                pass
        time.sleep(0.1) # wait for sensor to settle
        # If no device is found, exit the script
        if self.sensor==[]:
            print("No AMG8833 Found - Check Your Wiring")

    def run(self):
        while True:
            status,self.pixels = self.sensor.read_temp(pix_to_read) # read pixels with status
            if status: # if error in pixel, re-enter loop and try again
                continue
            T_thermistor = self.sensor.read_thermistor() # read thermistor temp
            #print("Thermistor Temperature: {0:2.2f}".format(T_thermistor)) # print thermistor temp
            self.max = max(self.pixels)
            self.high_index = self.pixels.index(self.max)
            self.high_x = self.high_index % 8 
            self.high_y = int(self.high_index / 8)
            #print(str(self.max)+" "+str(self.high_index)+" "+str(self.high_x)+" "+str(self.high_y))

    def get_heat_pixels(self):
        return self.pixels

    def get_max_temp(self):
        return self.max

    def get_max_temp_point(self):
        return self.high_x, self.high_y

    

if __name__ == '__main__':

    amg8833 = ConshellAmg8833()
    amg8833.run()
