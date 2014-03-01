# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:14:37 2014

@author: christian
"""
import threading
import time
import smokesignal
#import serial_h
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
        meiserial.laser(1,0)
        meiserial.laser(2,0)
        globalsh.scan_active = True
        scn = scanthread()
        #mygui.disable_btn()
        smokesignal.emit('btn_lock')
        scn.start()
    else:
        globalsh.scan_active = False
        #mygui.setbar(0)
        smokesignal.emit('progress', 0)
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
        self.minpixbright = globalsh.minpixbright
        self.stepnr = 0
        self.stepdelay = globalsh.stepdelay #ms
        self.barvalue = 0
        self.picfile = "temp\image.png"
        self.anafile = "temp\image2.png" 
    def run(self):        
        x = 0
        y = 0
        z = 0
        self.camwidth = cap.get(3)
        self.camheight = cap.get(4)
        self.stepangle = 2*self.pi/self.steptotake
        self.file_ana = open("file.asc", 'w')
        meiserial.laser(1,2)
        ret, self.anaimg = self.cap.read()
        ret, self.feed = self.cap.read()
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        for self.stepnr in range(0, globalsh.steptotake):
            ret, self.feed = self.cap.read()
            self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
            self.cur_angle = self.stepangle*self.stepnr
            #self.file_ana.write('scanning ' + str(math.degrees(self.cur_angle)) + ' degrees\n')
            for self.row in range(globalsh.uspinBox,int(self.camheight) - globalsh.dspinBox):
                #print self.row
                self.intensity = 0
                self.lastmaxpix = 0
                self.maxbrightpos = 0
                for self.col in range(globalsh.lspinBox,int(self.camwidth) - globalsh.rspinBox):
                    #print self.col
                    self.intensity = self.gray_image[self.row, self.col]
                    #self.gray_anaimage[self.row,self.col] = 0
                    if self.intensity >= self.lastmaxpix and self.intensity >= self.minpixbright:
                        self.lastmaxpix = self.intensity
                        self.maxbrightpos = self.col
                #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                self.b = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
                if self.b > 0 and self.maxbrightpos > 0: #positive
                    self.ro=self.b/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle) * -1
                    self.y=self.ro * math.sin(self.cur_angle) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.row/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " \n")
                    self.file_ana.write(self.txt)
                if self.b < 0 and self.maxbrightpos > 0: #negative
                    self.b = self.b * -1
                    self.ro=self.b/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle) * 1
                    self.y=self.ro * math.sin(self.cur_angle) * -1
                    self.roz=self.ro * math.sin(self.cam_angle) * -1
                    self.z=self.row/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " \n")
                    self.file_ana.write(self.txt)
            meiserial.step(int(self.steps_rev/globalsh.steptotake))    
            time.sleep(self.stepdelay / 1000)
            #cv2.imwrite(anafile, gray_anaimage)
            #print self.stepnr
            #print self.cur_angle
            progBarV = interp(self.stepnr,[0,globalsh.steptotake -1],[0,100])
            #mygui.setbar(progBarV)
            smokesignal.emit('progress', progBarV)
            #mygui.setlcd(math.degrees(self.cur_angle + self.stepangle))
            smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
            #mygui.setstatus('scanning:')
            smokesignal.emit('status', 'scanning:')
            if globalsh.scan_active == False:
                break
        print 'scan done'
        #mygui.setstatus('scan done')
        smokesignal.emit('status', 'scan finished.')
        meiserial.step(int(self.steps_rev/globalsh.steptotake))
        self.file_ana.close()
        meiserial.laser(1,0)
        globalsh.scan_active = False
        #mygui.enable_btn()
        smokesignal.emit('btn_unlock')
        #.setscanstate(False)
        smokesignal.emit('scanbtnstate', False)
