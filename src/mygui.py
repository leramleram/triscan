# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 04:14:31 2014

@author: christian
"""
from PyQt4 import QtCore,QtGui,uic
import sys
import scan
from capture import cap
import triscan
from globalsh import *
import globalsh
import cv2
form_class, base_class = uic.loadUiType("main.ui")
opt_class, base_class = uic.loadUiType("opt.ui")

class MyWidget (QtGui.QWidget, form_class):
    
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QWidget.__init__(self,parent,*args)
        self.setupUi(self)
    def update_bar(self):
        self.progressBar.setValue(progBarV)
    def initscan(self):
        if scan_active == False:
            doscan()
        else:
            stopscan()
    def __del__(self):
        print 'pfiati'
    def step(self):
        step(2)
    def turn(self):
        pass
    def progress(self, value):
        self.progressBar.setValue(value)
    def refresh(self):
        self.camstate = self.camBox.checkState()
        camwidth = cap.get(3)
        camheight = cap.get(4)
        if self.camstate == 0:
            cv2.destroyAllWindows()
            self.camBox.setCheckState(0)
        while self.camstate == 2:
            #print 'yoaha'
            ret, feed = cap.read()
            cv2.line(feed,(int(camwidth / 2),0),(int(camwidth/2),int(camheight)),(255,0,0),2)
            cv2.line(feed,(0,int(camheight/2)),(int(camwidth),int(camheight/2)),(255,0,0),2)

            cv2.line(feed,(opt.lspinBox.value(),0),(opt.lspinBox.value(),int(camheight)),(0,255,0),2)
            cv2.line(feed,(int(camwidth) - opt.rspinBox.value(),0),(int(camwidth) - opt.rspinBox.value(),int(camheight)),(0,255,0),2)
            cv2.line(feed,(0,opt.uspinBox.value()),(int(camwidth),opt.uspinBox.value()),(255,255,0),2)
            cv2.line(feed,(0,int(camheight) - opt.dspinBox.value()),(int(camwidth),int(camheight) - opt.dspinBox.value()),(255,255,0),2)
            cv2.imshow("webcam", feed)
            #time.sleep(0.02)
            key = cv2.waitKey(20)
            if key in [27, ord('Q'), ord('q')]: # exit on ESC
                cv2.destroyAllWindows()
                self.camBox.setCheckState(0)
                break
class optWidget (QtGui.QWidget, opt_class):
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QWidget.__init__(self,parent,*args)
        self.setupUi(self)
        self.resoBox.addItem('640x480')
        self.resoBox.addItem('800x600')
        self.resoBox.addItem('1280x960')
        self.connect(self.closeButton, QtCore.SIGNAL('clicked()'), self.closeopt)
        self.connect(self.scansrev_sdr, QtCore.SIGNAL('valueChanged(int)'), self.set_scansrev)
        self.connect(self.stepdelay_sdr, QtCore.SIGNAL('valueChanged(int)'), self.set_stepdelay)
        #self.connect(self.comBox, QtCore.SIGNAL('clicked()'), setcombox) #cross module link
        self.resoBox.activated.connect(self.set_resolution)
        self.resoBox.setCurrentIndex(1)
        self.scansrev_sdr.setValue(globalsh.steptotake)
        self.steps_lbl.setText(str(globalsh.steptotake))
        self.delay_lbl.setText(str(globalsh.stepdelay))
        self.scansrev_sdr.setTracking(True)
    def set_scansrev(self):
        globalsh.steptotake = self.scansrev_sdr.value()
        self.steps_lbl.setText(str(globalsh.steptotake))
        #print 'ohoho'
    def set_stepdelay(self):
        globalsh.stepdelay = self.stepdelay_sdr.value()
        self.delay_lbl.setText(str(globalsh.stepdelay))
    def set_resolution(self):
        reso = self.resoBox.currentIndex()
        if reso == 0:
            cap.set(3,640)
            cap.set(4,480)
            camwidth = 640
            camheight = 480
        if reso == 1:
            cap.set(3,800)
            cap.set(4,600)
            camwidth = 800
            camheight = 600
        if reso == 2:
            cap.set(3,1280)
            cap.set(4,960)
            camwidth = 1280
            camheight = 960
    def getopt():
        print 'yess'
        self.show()
        self.move(10, 20)
    def closeopt(self):
        self.close()  
    def setcombox(self, value):
        self.comBox.addItem(value) 
            

app = QtGui.QApplication(sys.argv)
form = MyWidget(None)
opt = optWidget(None)
def setbar(value):
    form.progress(value)
    
