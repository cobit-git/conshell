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
            status,pixels = self.sensor.read_temp(pix_to_read) # read pixels with status
            if status: # if error in pixel, re-enter loop and try again
                continue
            T_thermistor = self.sensor.read_thermistor() # read thermistor temp
            #print("Thermistor Temperature: {0:2.2f}".format(T_thermistor)) # print thermistor temp
            #print(pixels)

    def get_heat_pixels(self):
        return self.pixels

if __name__ == '__main__':

    amg8833 = ConshellAmg8833()
    amg8833.run()
