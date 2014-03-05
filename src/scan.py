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
import numpy as np
import capture
from globalsh import *
import globalsh
import os

def doscan(mode):   #init the scan
    if globalsh.scan_active == False:
        meiserial.laser(1,0)
        meiserial.laser(2,0)
        globalsh.scan_active = True
        if mode == 'r':
            scn = scanthread_r()
        if mode == 'l':
            scn = scanthread_l()
        if mode == 'd':
            scn = scanthread_d()
        smokesignal.emit('btn_lock')
        scn.start()
    else:
        globalsh.scan_active = False
        smokesignal.emit('progress', 0)
        
        
class scanthread_r(threading.Thread):     #scan class right laser
    def __init__(self):
        threading.Thread.__init__(self)
        self.pi = math.pi
        self.h_pxmm = 1.5
        self.v_pxmm = 1.5
        self.steps_rev = 400
        self.scan_active = False
        self.cam_angle = 12*self.pi/180
        self.cam_dist = 300
        self.l_Laserangle = 28*self.pi/180
        self.r_Laserangle = 28*self.pi/180
        self.steptotake = globalsh.steptotake
        self.stepangle = 2*self.pi/self.steptotake
        self.minpixbright = globalsh.minpixbright
        self.stepnr = 0
        self.stepdelay = globalsh.stepdelay #ms
        self.steptotake = globalsh.steptotake
        self.barvalue = 0
        #self.picfile = "temp\image.png"
        #self.anafile = "temp\image2.png" 
        self.lborder = globalsh.lborder
        self.rborder = globalsh.rborder
        self.uborder = globalsh.uborder
        self.dborder = globalsh.dborder
        smokesignal.emit('status', 'scanning:')
    def run(self):          #go go go!
        self.x = 0
        self.y = 0
        self.z = 0
        self.camwidth = globalsh.camwidth
        self.camheight = globalsh.camheight
        rowstotake = np.arange(self.uborder,int(self.camheight) - self.dborder)
        colstotake = np.arange(self.lborder,int(self.camwidth) - self.rborder)
        self.stepangle = 2*self.pi/self.steptotake
        now_itis = time.strftime("%Y_%m_%d_%H_%M")
        self.file_ana = open("scans\scn" + now_itis + "_r.asc", "w")
        meiserial.laser(1,2)
        ret, self.anaimg = capture.cap.read()
        ret, self.feed = capture.cap.read()
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        for self.stepnr in np.arange(0, self.steptotake):   #iterate over all steps to take for 360degrees
            ret, self.feed = capture.cap.read()
            self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
            self.cur_angle = self.stepangle*self.stepnr
            for self.row in rowstotake:     #iterate over all the rows of the picture
                self.intensity = 0
                self.lastmaxpix = 0
                self.maxbrightpos = 0
                for self.col in colstotake:     #iterate over all the columns of the picture
                    self.intensity = self.gray_image.item(self.row, self.col)
                    #self.gray_anaimage[self.row,self.col] = 0
                    if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                        if self.intensity >= self.lastmaxpix:
                            self.lastmaxpix = self.intensity
                            self.maxbrightpos = self.col
                #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                if self.maxbrightpos > 0:                    
                    self.b = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
                    if self.b > 0: #positive
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * -1
                        self.y=self.ro * math.sin(self.cur_angle) * 1
                        self.roz=self.ro * math.sin(self.cam_angle) * 1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 0 255 0\n")
                        self.file_ana.write(self.txt)
                    if self.b < 0: #negative
                        self.b = self.b * -1
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * 1
                        self.y=self.ro * math.sin(self.cur_angle) * -1
                        self.roz=self.ro * math.sin(self.cam_angle) * -1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 255 0 0\n")
                        self.file_ana.write(self.txt)
            meiserial.step(int(self.steps_rev/self.steptotake))    
            #cv2.imwrite(anafile, gray_anaimage)
            progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
            smokesignal.emit('progress', progBarV)
            smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
            if globalsh.scan_active == False:
                break
        meiserial.step(int(self.steps_rev/globalsh.steptotake))
        meiserial.laser(1,0)
        self.file_ana.close()
        self.file_asc = open("scans\scn" + now_itis + "_r.asc", "r")
        num_vertex = sum(1 for line in self.file_asc if line.rstrip())
        print 'analyzing..'
        #mygui.setstatus('scan done')
        smokesignal.emit('status', 'processing .ply')
        self.file_ply_stamp = "scans\scn" + now_itis + "_r.ply"
        with open("scans\scn" + now_itis + "_r.ply", 'w') as self.file_ply:
            with open("scans\scn" + now_itis + "_r.asc", 'r') as self.file_asc:
                self.header = open('plyheader.txt', 'r')
                self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex) + '\n')
                for line in self.header:
                    self.file_ply.write(line)
                self.header.close()
                for line in self.file_asc:
                    self.file_ply.write(line)
        globalsh.scan_active = False
        smokesignal.emit('btn_unlock')
        smokesignal.emit('scanbtnstate', False)
        smokesignal.emit('status', 'scan finished.')
        os.system("start scans\scn" + now_itis + "_r.ply")
        #Charlie down!      #end of rightmode_scan

class scanthread_l(threading.Thread):     #scan class       #left laser
    def __init__(self):
        threading.Thread.__init__(self)
        self.pi = math.pi
        self.h_pxmm = 1.5
        self.v_pxmm = 1.5
        self.steps_rev = 400
        self.scan_active = False
        self.cam_angle = 12*self.pi/180
        self.cam_dist = 300
        self.l_Laserangle = 28*self.pi/180
        self.r_Laserangle = 28*self.pi/180
        self.steptotake = globalsh.steptotake
        self.stepangle = 2*self.pi/self.steptotake
        self.minpixbright = globalsh.minpixbright
        self.stepnr = 0
        self.stepdelay = globalsh.stepdelay #ms
        self.steptotake = globalsh.steptotake
        self.barvalue = 0
        #self.picfile = "temp\image.png"
        #self.anafile = "temp\image2.png" 
        self.lborder = globalsh.lborder
        self.rborder = globalsh.rborder
        self.uborder = globalsh.uborder
        self.dborder = globalsh.dborder
        smokesignal.emit('status', 'scanning:')
    def run(self):          #go go go!
        print 'left!!'
        self.x = 0
        self.y = 0
        self.z = 0
        self.camwidth = globalsh.camwidth
        self.camheight = globalsh.camheight
        rowstotake = np.arange(self.uborder,int(self.camheight) - self.dborder)
        colstotake = np.arange(self.lborder,int(self.camwidth) - self.rborder)
        self.stepangle = 2*self.pi/self.steptotake
        now_itis = time.strftime("%Y_%m_%d_%H_%M")
        self.file_ana = open("scans\scn" + now_itis + "_l.asc", "w")
        meiserial.laser(0,2)
        ret, self.anaimg = capture.cap.read()
        ret, self.feed = capture.cap.read()
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        for self.stepnr in np.arange(0, self.steptotake):   #iterate over all steps to take for 360degrees
            ret, self.feed = capture.cap.read()
            self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
            self.cur_angle = self.stepangle*self.stepnr
            for self.row in rowstotake:     #iterate over all the rows of the picture
                self.intensity = 0
                self.lastmaxpix = 0
                self.maxbrightpos = 0
                for self.col in colstotake:     #iterate over all the columns of the picture
                    self.intensity = self.gray_image.item(self.row, self.col)
                    #self.gray_anaimage[self.row,self.col] = 0
                    if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                        if self.intensity >= self.lastmaxpix:
                            self.lastmaxpix = self.intensity
                            self.maxbrightpos = self.col
                #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                if self.maxbrightpos > 0:                    
                    self.b = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
                    if self.b > 0: #positive
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * -1
                        self.y=self.ro * math.sin(self.cur_angle) * 1
                        self.roz=self.ro * math.sin(self.cam_angle) * 1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 0 255 0\n")
                        self.file_ana.write(self.txt)
                    if self.b < 0: #negative
                        self.b = self.b * -1
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * 1
                        self.y=self.ro * math.sin(self.cur_angle) * -1
                        self.roz=self.ro * math.sin(self.cam_angle) * -1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 255 0 0\n")
                        self.file_ana.write(self.txt)
            meiserial.step(int(self.steps_rev/self.steptotake))    
            #cv2.imwrite(anafile, gray_anaimage)
            progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
            smokesignal.emit('progress', progBarV)
            smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
            if globalsh.scan_active == False:
                break
        meiserial.step(int(self.steps_rev/globalsh.steptotake))
        meiserial.laser(1,0)
        self.file_ana.close()
        self.file_asc = open("scans\scn" + now_itis + "_l.asc", "r")
        num_vertex = sum(1 for line in self.file_asc if line.rstrip())
        print 'analyzing..'
        #mygui.setstatus('scan done')
        smokesignal.emit('status', 'processing .ply')
        self.file_ply_stamp = "scans\scn" + now_itis + "_l.ply"
        with open("scans\scn" + now_itis + "_l.ply", 'w') as self.file_ply:
            with open("scans\scn" + now_itis + "_l.asc", 'r') as self.file_asc:
                self.header = open('plyheader.txt', 'r')
                self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex) + '\n')
                for line in self.header:
                    self.file_ply.write(line)
                self.header.close()
                for line in self.file_asc:
                    self.file_ply.write(line)
        globalsh.scan_active = False
        smokesignal.emit('btn_unlock')
        smokesignal.emit('scanbtnstate', False)
        smokesignal.emit('status', 'scan finished.')
        os.system("start scans\scn" + now_itis + "_l.ply")
        #Charlie down!    #end of leftmode_scan

class scanthread_d(threading.Thread):     #scan class     #dual laser mode it is
    def __init__(self):
        threading.Thread.__init__(self)
        self.pi = math.pi
        self.h_pxmm = 1.5
        self.v_pxmm = 1.5
        self.steps_rev = 400
        self.scan_active = False
        self.cam_angle = 12*self.pi/180
        self.cam_dist = 300
        self.l_Laserangle = 28*self.pi/180
        self.r_Laserangle = 28*self.pi/180
        self.steptotake = globalsh.steptotake
        self.stepangle = 2*self.pi/self.steptotake
        self.minpixbright = globalsh.minpixbright
        self.stepnr = 0
        self.stepdelay = globalsh.stepdelay #ms
        self.steptotake = globalsh.steptotake
        self.barvalue = 0
        #self.picfile = "temp\image.png"
        #self.anafile = "temp\image2.png" 
        self.lborder = globalsh.lborder
        self.rborder = globalsh.rborder
        self.uborder = globalsh.uborder
        self.dborder = globalsh.dborder
        smokesignal.emit('status', 'scanning:')
    def run(self):          #go go go!
        print 'dual!!'
        self.x = 0
        self.y = 0
        self.z = 0
        self.camwidth = globalsh.camwidth
        self.camheight = globalsh.camheight
        rowstotake = np.arange(self.uborder,int(self.camheight) - self.dborder)
        colstotake = np.arange(self.lborder,int(self.camwidth) - self.rborder)
        self.stepangle = 2*self.pi/self.steptotake
        now_itis = time.strftime("%Y_%m_%d_%H_%M")
        self.file_ana = open("scans\scn" + now_itis + "_d.asc", "w")
        meiserial.laser(1,2)
        ret, self.anaimg = capture.cap.read()
        ret, self.feed = capture.cap.read()
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        for self.stepnr in np.arange(0, self.steptotake):   #iterate over all steps to take for 360degrees
            ret, self.feed = capture.cap.read()
            self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
            self.cur_angle = self.stepangle*self.stepnr
            for self.row in rowstotake:     #iterate over all the rows of the picture
                self.intensity = 0
                self.lastmaxpix = 0
                self.maxbrightpos = 0
                for self.col in colstotake:     #iterate over all the columns of the picture
                    self.intensity = self.gray_image.item(self.row, self.col)
                    #self.gray_anaimage[self.row,self.col] = 0
                    if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                        if self.intensity >= self.lastmaxpix:
                            self.lastmaxpix = self.intensity
                            self.maxbrightpos = self.col
                #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                if self.maxbrightpos > 0:                    
                    self.b = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
                    if self.b > 0: #positive
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * -1
                        self.y=self.ro * math.sin(self.cur_angle) * 1
                        self.roz=self.ro * math.sin(self.cam_angle) * 1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 0 255 0\n")
                        self.file_ana.write(self.txt)
                    if self.b < 0: #negative
                        self.b = self.b * -1
                        self.ro=self.b/math.sin(self.r_Laserangle)
                        self.x=self.ro * math.cos(self.cur_angle) * 1
                        self.y=self.ro * math.sin(self.cur_angle) * -1
                        self.roz=self.ro * math.sin(self.cam_angle) * -1
                        self.z=self.row/self.v_pxmm + self.roz
                        self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 255 0 0\n")
                        self.file_ana.write(self.txt)
            meiserial.step(int(self.steps_rev/self.steptotake))    
            #cv2.imwrite(anafile, gray_anaimage)
            progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
            smokesignal.emit('progress', progBarV)
            smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
            if globalsh.scan_active == False:
                break
        meiserial.step(int(self.steps_rev/globalsh.steptotake))
        meiserial.laser(1,0)
        self.file_ana.close()
        self.file_asc = open("scans\scn" + now_itis + "_d.asc", "r")
        num_vertex = sum(1 for line in self.file_asc if line.rstrip())
        print 'analyzing..'
        #mygui.setstatus('scan done')
        smokesignal.emit('status', 'processing .ply')
        self.file_ply_stamp = "scans\scn" + now_itis + "_d.ply"
        with open("scans\scn" + now_itis + "_d.ply", 'w') as self.file_ply:
            with open("scans\scn" + now_itis + "_d.asc", 'r') as self.file_asc:
                self.header = open('plyheader.txt', 'r')
                self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex) + '\n')
                for line in self.header:
                    self.file_ply.write(line)
                self.header.close()
                for line in self.file_asc:
                    self.file_ply.write(line)
        globalsh.scan_active = False
        smokesignal.emit('btn_unlock')
        smokesignal.emit('scanbtnstate', False)
        smokesignal.emit('status', 'scan finished.')
        os.system("start scans\scn" + now_itis + "_d.ply")
        #Charlie down!      #end of dualmode_scan