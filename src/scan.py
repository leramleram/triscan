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
red = '255 0 0'
green = '0 255 0'
blue = '0 0 255'
yellow = '255 255 0'
magenta = '255 0 255'
turquoise = '0 255 255'

smokesignal.on('openfile')
def openfile():
    os.system(globalsh.filestamp)
    
def doscan(mode):   #init the scan
    if globalsh.scan_active == False:
        meiserial.laser(1,0)
        meiserial.laser(2,0)
        smokesignal.emit('setcamexpo', globalsh.camexpo)
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
    
class scanthread_x(threading.Thread):                                                               #scan class right laser
    def __init__(self, mode):
        print 'starting scanthread'
        threading.Thread.__init__(self)
        self.mode = mode
        self.scanmode =  self.mode
        meiserial.laser(0,0)
        meiserial.laser(1,0)
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
        meiserial.step('cc', 8)
        time.sleep(0.2)
        meiserial.step('cw', 8)
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
        if self.scanmode == 'd':
            with open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".anal", 'w') as self.file_anal:
                with open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".anar", 'w') as self.file_anar:
                    for self.stepnr in np.arange(0, self.steptotake):                               #iterate over all steps needed for a 360degrees turn
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
                        self.mode = 'l'
                        meiserial.laser(0,1)                                                        #firste the left side
                        time.sleep(self.stepdelay)
                        ret, self.feedl = capture.cap.read()
                        ret, self.feedl = capture.cap.read()
                        self.gray_imagel = cv2.cvtColor(self.feedl, cv2.COLOR_BGR2GRAY)
                        for self.rows in self.rowstotake:                                           #iterate over all the rows of the picture
                            self.intensityl = 0
                            self.lastmaxpixl = 0
                            self.maxbrightposl = 0
                            for self.cols in self.colstotake:                                       #iterate over all the columns of the picture
                                self.intensityl = self.gray_imagel.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensityl >= self.minpixbright:                            #look wich pixel was the brightest in this line
                                    if self.intensityl >= self.lastmaxpixl:
                                        self.lastmaxpixl = self.intensityl
                                        self.maxbrightposl = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.process_offset()  
                        self.mode = 'r'
                        meiserial.laser(0,0)
                        meiserial.laser(1,1)                                                       #then the right side
                        time.sleep(self.stepdelay)
                        ret, self.feedr = capture.cap.read()
                        ret, self.feedr = capture.cap.read()
                        self.gray_imager = cv2.cvtColor(self.feedr, cv2.COLOR_BGR2GRAY)
                        
                        for self.rows in self.rowstotake:                                           #iterate over all the rows of the picture
                            self.intensityr = 0
                            self.lastmaxpixr = 0
                            self.maxbrightposr = 0
                            for self.cols in self.colstotake:                                       #iterate over all the columns of the picture
                                self.intensityr = self.gray_imager.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensityr >= self.minpixbright:                            #look wich pixel was the brightest in this line
                                    if self.intensityr >= self.lastmaxpixr:
                                        self.lastmaxpixr = self.intensityr
                                        self.maxbrightposr = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.process_offset()                                                   #compute offset
                        meiserial.laser(1,0)                            
                        meiserial.step('cw', int(self.steps_rev/self.steptotake))    
                        #cv2.imwrite(anafile, gray_anaimage)
                        progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
                        smokesignal.emit('progress', progBarV)
                        self.cur_angle = self.stepangle*self.stepnr
                        smokesignal.emit('lcd', math.degrees(self.cur_angle + self.stepangle))
                        if globalsh.scan_active == False:
                            break
        else:
            if self.scanmode == 'l':
                with open(ana_dir + self.filestamp + ".anal", 'w') as self.file_anal:
                    for self.stepnr in np.arange(0, self.steptotake):                               #iterate over all steps needed for a 360degrees turn
                        ret, self.feed = capture.cap.read()
                        self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
                        self.cur_angle_l = self.stepangle*self.stepnr - self.l_Laserangle
                        if self.cur_angle_l < 0:
                            self.cur_angle_l += 2*self.pi
                        elif self.cur_angle_l > 2*self.pi:
                            self.cur_angle_l -= 2*self.pi
                        for self.rows in self.rowstotake:                                           #iterate over all the rows of the picture
                            self.intensityl = 0
                            self.lastmaxpixl = 0
                            self.maxbrightposl = 0
                            for self.cols in self.colstotake:                                       #iterate over all the columns of the picture
                                self.intensityl = self.gray_image.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensityl >= self.minpixbright:                            #look wich pixel was the brightest in this line
                                    if self.intensityl >= self.lastmaxpixl:
                                        self.lastmaxpixl = self.intensityl
                                        self.maxbrightposl = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.process_offset()                                                   #compute offset
                        meiserial.step('cw', int(self.steps_rev/self.steptotake))  
                        time.sleep(self.stepdelay)
                        #cv2.imwrite(anafile, gray_anaimage)
                        progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
                        smokesignal.emit('progress', progBarV)
                        smokesignal.emit('lcd', math.degrees(self.cur_angle_l + self.stepangle))
                        if globalsh.scan_active == False:
                            break
            elif self.scanmode == 'r':
                with open(ana_dir + self.filestamp + ".anar", 'w') as self.file_anar:
                    for self.stepnr in np.arange(0, self.steptotake):                               #iterate over all steps needed for a 360degrees turn
                        ret, self.feed = capture.cap.read()
                        self.gray_image = cv2.cvtColor(self.feed, cv2.COLOR_BGR2GRAY)
                        self.cur_angle_r = self.stepangle*self.stepnr + self.r_Laserangle
                        if self.cur_angle_r < 0:
                            self.cur_angle_r += 2*self.pi
                        elif self.cur_angle_r > 2*self.pi:
                            self.cur_angle_r -= 2*self.pi
                        for self.rows in self.rowstotake:                                           #iterate over all the rows of the picture
                            self.intensityr = 0
                            self.lastmaxpixr = 0
                            self.maxbrightposr = 0
                            for self.cols in self.colstotake:                                       #iterate over all the columns of the picture
                                self.intensityr = self.gray_image.item(self.rows, self.cols)
                                #self.gray_anaimage[self.row,self.col] = 0
                                if self.intensityr >= self.minpixbright:                            #look wich pixel was the brightest in this line
                                    if self.intensityr >= self.lastmaxpixr:
                                        self.lastmaxpixr = self.intensityr
                                        self.maxbrightposr = self.cols
                            #self.gray_anaimage[self.row, self.maxbrightpos] = 255
                            self.process_offset()                                                   #compute offset
                        meiserial.step('cw', int(self.steps_rev/self.steptotake))   
                        time.sleep(self.stepdelay)
                        #cv2.imwrite(anafile, gray_anaimage)
                        progBarV = interp(self.stepnr,[0,self.steptotake -1],[0,100])
                        smokesignal.emit('progress', progBarV)
                        smokesignal.emit('lcd', math.degrees(self.cur_angle_r + self.stepangle))
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
               
    def process_offset(self):                                                                       #compute coordinates and save them to the analysation file
        if self.mode == 'l':
            if self.maxbrightposl > 0:                                                              #left Laser mode
                self.offset = ((self.maxbrightposl - 1)-self.camwidth/2)/self.h_pxmm
                if self.offset > 0:                                                                 #negative
                    self.ro=self.offset/math.sin(self.l_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_l) * 1
                    self.y=self.ro * math.sin(self.cur_angle_l) * -1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + turquoise + "\n")
                elif self.offset < 0:                                                               #positive
                    self.inv_offset = self.offset * -1
                    self.ro=self.inv_offset/math.sin(self.l_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_l) * -1
                    self.y=self.ro * math.sin(self.cur_angle_l) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm - self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + green + "\n")
                self.file_anal.write(self.txt)
        elif self.mode == 'r':                                                                      #Right Laser mode
            if self.maxbrightposr > 0:
                self.offset = ((self.maxbrightposr + 1)-self.camwidth/2)/self.h_pxmm
                if self.offset > 0:                                                                 #positive
                    self.ro=self.offset/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_r) * -1
                    self.y=self.ro * math.sin(self.cur_angle_r) * 1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm - self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + red + "\n")
                elif self.offset < 0:                                                               #negative
                    self.inv_offset = self.offset * -1
                    self.ro=self.inv_offset/math.sin(self.r_Laserangle)
                    self.x=self.ro * math.cos(self.cur_angle_r) * 1
                    self.y=self.ro * math.sin(self.cur_angle_r) * -1
                    self.roz=self.ro * math.sin(self.cam_angle) * 1
                    self.z=self.rows/self.v_pxmm + self.roz
                    self.txt = (str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + magenta + "\n")
                self.file_anar.write(self.txt)

    def write_scans(self):   
        if self.scanmode == 'd':                                                                    #export the scan to ply/asc
            self.file_anal = open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".anal", "r")
            num_vertex_l = sum(1 for line in self.file_anal if line.rstrip())
            self.file_anar = open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".anar", "r")
            num_vertex_r = sum(1 for line in self.file_anar if line.rstrip())
            self.file_ply_stamp = scan_dir + self.filestamp + ".ply"
            with open(self.file_ply_stamp, 'w') as self.file_ply:
                with open(ana_dir + "scn" + self.now_itis + "_" + 'l' + ".anal", "r") as self.file_anal:
                    with open(ana_dir + "scn" + self.now_itis + "_" + 'r' + ".anar", "r") as self.file_anar:
                        self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex_l + num_vertex_r) + '\n')
                        self.file_ply.write("property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n")
                        for line in self.file_anal:
                            self.file_ply.write(line)
                        for line in self.file_anar:
                            self.file_ply.write(line)
        else:
            self.file_ana = open(ana_dir + self.filestamp + ".ana" + self.scanmode, "r")
            num_vertex = sum(1 for line in self.file_ana if line.rstrip())
            self.file_ply_stamp = scan_dir + self.filestamp + ".ply"
            with open(self.file_ply_stamp, 'w') as self.file_ply:
                with open(ana_dir + self.filestamp + ".ana" + self.scanmode, 'r') as self.file_ana:
                    self.file_ply.write('ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex ' + str(num_vertex) + '\n')
                    self.file_ply.write("property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n")
                    for line in self.file_ana:
                        self.file_ply.write(line)                      
    
        
        #Charlie down!      #end of scan
