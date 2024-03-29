# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:22:49 2014

@author: christian
"""
import platform
import serial
#from serial import serial
import time
import glob
import smokesignal
import globalsh
from serial import *
            
class serialh():
    def __init__(self):
        self.connected = False
        #serial.Serial.__init__(self)
        self.list_serial_ports_p()
        time.sleep(0.5)
        self.port = ("COM" + str(globalsh.comport))
        if globalsh.autocnct == 2:
            self.connect_p()
    def __del__(self):
        print 'releasing serial port'
        self.ser.close()
        
    def list_serial_ports_p(self):                                                                  #check wich serial ports are available
        self.system_name = platform.system()
        if self.system_name == "Windows":
            self.available_p = []
            for i in range(24):
                try:
                    self.s = serial.Serial(i)
                    self.available_p.append(i+1)
                    self.s.close()
                except SerialException:
                    pass
            globalsh.availble_p = self.available_p
        elif self.system_name == "Darwin":
                                                                                                    # Mac
            return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
        else:
                                                                                                    # Assume Linux or something else
            return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')
        
    def connect_p(self):                                                                            #nomen est omen
        try:
            self.ser = serial.Serial(str(self.port),baudrate=globalsh.baudrate)
            print("port " + self.port + "  opened successfully")
            self.connected = True
            smokesignal.emit('btn_unlock')
            smokesignal.emit('status', 'here we go!')
        except SerialException:
            print ('the requested serial port ' + str(self.port) + ' could not be opened')
            globalsh.dlg_title = 'warning!'
            globalsh.dlg_txt = 'serial port ' + str(self.port) + ' could not be opened, the program will likely not work before you connect to a proper device'
            globalsh.dlg_issue = 'ser'
            #mygui.get_dialog()
            smokesignal.emit('dialog')
         
    def step(self, way, n):                                                                         #do n steps in $way way
        if way == 'cw':
            for i in range(n):
                self.ser.write("F")
                time.sleep(0.03)
        elif way == 'cc':
            for i in range(n):
                self.ser.write("B")
                time.sleep(0.03)
            
            
    def onestep(self):                                                                              #do a single step
        for i in range(1):
            self.ser.write("F")
            time.sleep(0.03)
            
    def turn(self):                                                                                 #send the comand for 2 full spins
        self.ser.write("T")
        time.sleep(0.05)
        
    def laser(self, n, v):                                                                          #toggle the lasers
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
    def setlLaser(self):
        self.ser.write("L")
        
    def light(self, state):
        if state == 1:
            self.ser.write("W")
        else:
            self.ser.write("w")
                

meiserial = serialh()
