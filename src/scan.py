# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:14:37 2014

@author: christian
"""
import threading
import time
import serial_h
import mygui

from serial_h import meiserial
import cv2

import math
from numpy import interp
from capture import cap
from globalsh import *
import globalsh


def doscan():
    if globalsh.scan_active == False:
        globalsh.scan_active = True
        scn = scanthread()
        scn.start()
    else:
        globalsh.scan_active = False
        mygui.setbar(0)
class scanthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pi = math.pi
        self.h_pxmm = 6
        self.v_pxmm = 6
        self.steps_rev = 400
        self.scan_active = False
        self.cam_angle = 12*self.pi/180
        self.cam_dist = 300
        self.l_Laserangle = 28*self.pi/180
        self.r_Laserangle = 28*self.pi/180
        self.steptotake = globalsh.steptotake
        self.stepangle = 2*self.pi/self.steptotake
        self.cap = cv2.VideoCapture(0)
        self.stepnr = 0
        self.stepdelay = globalsh.stepdelay #ms
        self.barvalue = 0
        self.picfile = "temp\image.png"
        self.anafile = "temp\image2.png" 
    def run(self):        
        x = 0
        y = 0
        z = 0
        self.camwidth = self.cap.get(3)
        self.camheight = cap.get(4)
        self.stepangle = 2*self.pi/self.steptotake
        self.file_ana = open("file.asc", 'w')
        meiserial.laser(1,1)
        ret, self.anaimg = self.cap.read()
        ret, self.feed = self.cap.read()
        
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        for self.stepnr in range(0, globalsh.steptotake):
            ret, self.feed = self.cap.read()
            self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
            self.cur_angle = self.stepangle*self.stepnr
            for self.row in range(uspinBox,int(self.camheight) - dspinBox):
                self.intensity = 0
                self.lastmaxpix = 0
                self.maxbrightpos = 0
                for self.col in range(lspinBox,int(self.camwidth) - rspinBox):
                    self.intensity = self.gray_image[self.row, self.col]
                    self.gray_anaimage[self.row,self.col] = 0
                    if self.intensity >= self.lastmaxpix:
                        self.lastmaxpix = self.intensity
                        self.maxbrightpos = self.col
                self.gray_anaimage[self.row, self.maxbrightpos] = 255
                self.b = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
                if self.b > 0: #positive
                    self.ro=self.b/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle) * -1
                    self.y=self.ro * math.sin(self.cur_angle) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.row/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " \n")
                    self.file_ana.write(self.txt)
                if self.b < 0: #negative
                    self.b = self.b * -1
                    self.ro=self.b/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle) * 1
                    self.y=self.ro * math.sin(self.cur_angle) * -1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.row/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " \n")
                    self.file_ana.write(self.txt)
                    #mygui.form.show()
                    #txt = (str(row) + ", " + str(lastmaxpix) + ", " + str(maxbrightpos) + ", " + str(intensity) + " \n")
            meiserial.step(int(self.steps_rev/globalsh.steptotake))    
            time.sleep(self.stepdelay / 1000)
            #cv2.imwrite(anafile, gray_anaimage)
            print self.stepnr
            print self.cur_angle
            progBarV = interp(self.stepnr,[0,globalsh.steptotake -1],[0,100])
            mygui.setbar(progBarV)
            mygui.setlcd(math.degrees(self.cur_angle))
            if globalsh.scan_active == False:
                break
        print 'scan done'
        self.file_ana.close()
        meiserial.laser(1,0)
        globalsh.scan_active = False
