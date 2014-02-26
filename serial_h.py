# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:22:49 2014

@author: christian
"""
import serial
from serial import Serial
import time
import glob
import triscan

            
class serialh(serial.Serial):
    def __init__(self):
        serial.Serial.__init__(self)
        time.sleep(0.5)
        self.port = "COM15"
        self.connect_p()
        
    def list_serial_ports_p(self):
        self.system_name = "Windows"
        if self.system_name == "Windows":
            # Scan for available ports.
            self.available_p = []
            for i in range(32):
                try:
                    self.s
                    
                    #self.s = serial.Serial(i)
                    self.available_p.append(i+1)
                    #setcombox(+1)
                    #triscan.opt.comBox.addItem(str(i+1))
                    self.s.close()
                except serial.SerialException:
                    pass
            return self.available_p
        elif self.system_name == "Darwin":
            # Mac
            return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
        else:
            # Assume Linux or something else
            return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')
        
    def connect_p(self):
        try:
            self.ser = serial.Serial(str(self.port),baudrate=9600)
            print("port " + self.port + "  opened successfully")
        except serial.SerialException:
            print ('the requested serial port ' + str(self.port) + ' could not be opened')
         
    def step(self, n):
        for i in range(n):
            self.ser.write("F")
            time.sleep(0.05)
            
    def onestep(self):
        for i in range(1):
            self.ser.write("F")
            time.sleep(0.05)
            
    def turn(self):
        self.ser.write("T")
        time.sleep(0.05)
        
    def laser(self, n, v):
        if n == 0:
            if v == 1:
                self.ser.write("L")
            else:
                self.ser.write("l")
        if n == 1:
            if v == 1:
                self.ser.write("R")
            else:
                self.ser.write("r")
                

meiserial = serialh()