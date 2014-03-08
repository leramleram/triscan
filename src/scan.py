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
from ardu import meiserial
import cv2
import math
from numpy import interp
import numpy as np
import capture
from globalsh import *
import globalsh
import os


scan_dir = "scans\\"
ana_dir = "tmp\\"
smokesignal.on('openfile')
def openfile():
    os.system(globalsh.filestamp)
    
def doscan(mode):   #init the scan
    if globalsh.scan_active == False:
        meiserial.laser(1,0)
        meiserial.laser(2,0)
        globalsh.scan_active = True
        scandir = os.path.dirname(scan_dir)
        try:
            os.stat(scandir)
        except:
            os.mkdir(scandir)
        anadir = os.path.dirname(ana_dir)
        try:
            os.stat(anadir)
        except:
            os.mkdir(anadir)
        scn = scanthread_x(mode)
        smokesignal.emit('btn_lock')
        scn.start()
    else:
        globalsh.scan_active = False
        smokesignal.emit('progress', 0)
    
class scanthread_x(threading.Thread):     #scan class right laser
    def __init__(self, mode):
        print 'starting scanthread'
        threading.Thread.__init__(self)
        self.mode = mode
        self.scanmode =  mode
        if self.mode == 'l':
            meiserial.laser(0,1)
        if self.mode == 'r':
            meiserial.laser(1,1)
        self.pi = math.pi
        self.h_pxmm = 1
        self.v_pxmm = 1
        self.steps_rev = 400
        self.scan_active = False
        self.cam_angle = globalsh.cam_angle*self.pi/180.0
        self.cam_dist = 300
        self.l_Laserangle = globalsh.l_angle*self.pi/180.0
        self.r_Laserangle = globalsh.r_angle*self.pi/180.0
        self.steptotake = globalsh.steptotake
        self.stepangle = 2*self.pi/self.steptotake
        self.minpixbright = globalsh.minpixbright
        self.stepnr = 0
        self.stepdelay = float(globalsh.stepdelay/1000.0) #ms
        self.steptotake = globalsh.steptotake
        self.camwidth = globalsh.camwidth
        self.camheight = globalsh.camheight
        self.stepangle = 2*self.pi/self.steptotake
        #self.picfile = "temp\image.png"
        #self.anafile = "temp\image2.png" 
        self.lborder = globalsh.lborder
        self.rborder = globalsh.rborder
        self.uborder = globalsh.uborder
        self.dborder = globalsh.dborder
        self.rowstotake = np.arange(self.uborder,int(self.camheight) - self.dborder)
        self.colstotake = np.arange(self.lborder,int(self.camwidth) - self.rborder)
        self.now_itis = time.strftime("%Y_%m_%d_%H_%M")
        meiserial.step('cc', 16)
        time.sleep(0.5)
        meiserial.step('cw', 16)
        #self.file_ana = open(ana_dir + self.filestamp + ".ana", "w")
        smokesignal.emit('status', 'scanning:')
    def __del__(self):
        print 'closing scanthread'        
    def run(self):          #go go go!
        self.x = 0
        self.y = 0
        self.z = 0
        #meiserial.laser(1,1)
        ret, self.anaimg = capture.cap.read()
        ret, self.feed = capture.cap.read()
        self.gray_anaimage = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite(picfile, gray_image)
        self.filestamp = "scn" + self.now_itis + "_" + self.mode
        if self.mode == 'd':
            with open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".ana", 'w') as self.file_anal:
                with open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".ana", 'w') as self.file_anar:
                    for self.stepnr in np.arange(0, self.steptotake):   #iterate over all steps needed for a 360degrees turn
                        meiserial.laser(0,1)                                                        #firste the left side
                        time.sleep(self.stepdelay)
                        ret, self.feed = capture.cap.read()
                        self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
                        self.cur_angle_l = self.stepangle*self.stepnr - self.l_Laserangle
                        if self.cur_angle_l < 0:
                            self.cur_angle_l += 2*self.pi
                        elif self.cur_angle_l > 2*self.pi:
                            self.cur_angle_l -= 2*self.pi
                        self.cur_angle_r = self.stepangle*self.stepnr + self.r_Laserangle
                        if self.cur_angle_r < 0:
                            self.cur_angle_r += 2*self.pi
                        elif self.cur_angle_r > 2*self.pi:
                            self.cur_angle_r -= 2*self.pi
                        for self.rows in self.rowstotake:     #iterate over all the rows of the picture
                            self.intensity = 0
                            self.lastmaxpix = 0
                            self.maxbrightpos = 0
                            for self.cols in self.colstotake:     #iterate over all the columns of the picture
                                self.intensity = self.gray_image.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                                    if self.intensity >= self.lastmaxpix:
                                        self.lastmaxpix = self.intensity
                                        self.maxbrightpos = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.mode = 'l'
                            self.process_offset()  
                        meiserial.laser(0,0)
                        meiserial.laser(1,1)                                                            #then the second side
                        time.sleep(self.stepdelay)
                        ret, self.feed = capture.cap.read()
                        self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
                        self.cur_angle = self.stepangle*self.stepnr
                        for self.rows in self.rowstotake:     #iterate over all the rows of the picture
                            self.intensity = 0
                            self.lastmaxpix = 0
                            self.maxbrightpos = 0
                            for self.cols in self.colstotake:     #iterate over all the columns of the picture
                                self.intensity = self.gray_image.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                                    if self.intensity >= self.lastmaxpix:
                                        self.lastmaxpix = self.intensity
                                        self.maxbrightpos = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.mode = 'r'
                            self.process_offset()                                                       #compute offset
                        meiserial.laser(1,0)                            
                        meiserial.step('cw', int(self.steps_rev/self.steptotake))    
                        #cv2.imwrite(anafile, gray_anaimage)
                        progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
                        smokesignal.emit('progress', progBarV)
                        smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
                        if globalsh.scan_active == False:
                            break
        else:
            with open(ana_dir + self.filestamp + ".ana", 'w') as self.file_ana:
                for self.stepnr in np.arange(0, self.steptotake):   #iterate over all steps needed for a 360degrees turn
                    ret, self.feed = capture.cap.read()
                    self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
                    self.cur_angle_l = self.stepangle*self.stepnr - self.l_Laserangle
                    if self.cur_angle_l < 0:
                        self.cur_angle_l += 2*self.pi
                    elif self.cur_angle_l > 2*self.pi:
                        self.cur_angle_l -= 2*self.pi
                    self.cur_angle_r = self.stepangle*self.stepnr + self.r_Laserangle
                    if self.cur_angle_r < 0:
                        self.cur_angle_r += 2*self.pi
                    elif self.cur_angle_r > 2*self.pi:
                        self.cur_angle_r -= 2*self.pi
                    for self.rows in self.rowstotake:     #iterate over all the rows of the picture
                        self.intensity = 0
                        self.lastmaxpix = 0
                        self.maxbrightpos = 0
                        for self.cols in self.colstotake:     #iterate over all the columns of the picture
                            self.intensity = self.gray_image.item(self.rows, self.cols)
                            #self.gray_anaimage[self.row,self.col] = 0
                            if self.intensity >= self.minpixbright:     #look wich pixel was the brightest in this line
                                if self.intensity >= self.lastmaxpix:
                                    self.lastmaxpix = self.intensity
                                    self.maxbrightpos = self.cols
                        #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                        self.process_offset()                                                       #compute offset
                    meiserial.step('cw', int(self.steps_rev/self.steptotake))    
                    #cv2.imwrite(anafile, gray_anaimage)
                    progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
                    smokesignal.emit('progress', progBarV)
                    smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
                    if globalsh.scan_active == False:
                        break
            
        meiserial.step('cw', int(self.steps_rev/globalsh.steptotake))
        meiserial.laser(1,0)
        #self.file_ana.close()

        print 'analyzing..'
        #mygui.setstatus('scan done')
        smokesignal.emit('status', 'processing .ply')
        #self.file_ply_stamp = scan_dir + self.filestamp + ".ply"
        globalsh.filestamp = str(scan_dir + self.filestamp + ".ply")
        self.write_scans()
        globalsh.scan_active = False
        smokesignal.emit('btn_unlock')
        smokesignal.emit('scanbtnstate', False)
        smokesignal.emit('status', 'scan finished.')
        self.__del__()
               
    def process_offset(self):       #compute coordinates and save them to the analysation file
        if self.maxbrightpos > 0:                    
            self.offset = ((self.maxbrightpos + 1)-self.camwidth/2)/self.h_pxmm
            if self.mode == 'l':                                                                          #left Laser mode
                if self.offset > 0: #negative
                    self.ro=self.offset/math.sin(self.l_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_l) * -1
                    self.y=self.ro * math.sin(self.cur_angle_l) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 0 255 0\n")
                elif self.offset < 0: #positive
                    self.offset = self.offset * -1
                    self.ro=self.offset/math.sin(self.l_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_l) * -1
                    self.y=self.ro * math.sin(self.cur_angle_l) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 255 0 255\n")
                self.file_anal.write(self.txt)
            elif self.mode == 'r':                                                                          #Right Laser mode
                if self.offset > 0: #positive
                    self.ro=self.offset/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_r) * -1
                    self.y=self.ro * math.sin(self.cur_angle_r) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 255 255 0\n")
                elif self.offset < 0: #negative
                    self.offset = self.offset * -1
                    self.ro=self.offset/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_r) * 1
                    self.y=self.ro * math.sin(self.cur_angle_r) * -1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " 0 0 255\n")
                self.file_anar.write(self.txt)

    def write_scans(self):   
        if self.scanmode == 'd':                                                                   #export the scan to ply/asc
            self.file_anal = open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".ana", "r")
            num_vertex_l = sum(1 for line in self.file_anal if line.rstrip())
            self.file_anar = open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".ana", "r")
            num_vertex_r = sum(1 for line in self.file_anar if line.rstrip())
            self.file_ply_stamp = scan_dir + self.filestamp + ".ply"
            with open(self.file_ply_stamp, 'w') as self.file_ply:
                with open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".ana", "r") as self.file_anal:
                    with open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".ana", "r") as self.file_anar:
                        self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex_l + num_vertex_r) + '\n')
                        self.file_ply.write("property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n")
                        for line in self.file_anal:
                            self.file_ply.write(line)
                        for line in self.file_anar:
                            self.file_ply.write(line)
        else:
            self.file_ana = open(ana_dir + self.filestamp + ".ana", "r")
            num_vertex = sum(1 for line in self.file_ana if line.rstrip())
            self.file_ply_stamp = scan_dir + self.filestamp + ".ply"
            with open(self.file_ply_stamp, 'w') as self.file_ply:
                with open(ana_dir + self.filestamp + ".ana", 'r') as self.file_ana:
                    self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex) + '\n')
                    self.file_ply.write("property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n")
                    for line in self.file_ana:
                        self.file_ply.write(line)                      
    
        
        #Charlie down!      #end of scan
