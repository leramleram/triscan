# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 04:14:31 2014

@author: christian
"""
from PyQt4 import QtCore,QtGui,uic
import sys
import smokesignal
from numpy import interp
from capture import cap
from globalsh import *
import globalsh
import cv2
#import reghandle

form_class, base_class = uic.loadUiType("main.ui")
opt_class, base_class = uic.loadUiType("opt.ui")

class MyWidget (QtGui.QWidget, form_class):         #Main window class
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QWidget.__init__(self,parent,*args)
        self.setupUi(self)
        self.status_lbl.setText('ready for rumble!')
    def update_bar(self):
        self.progressBar.setValue(progBarV)
    def __del__(self):
        print 'pfiati'
    def step(self):
        step(2)
    def turn(self):
        pass
    def progress(self, value):
        self.progressBar.setValue(value)
    def set_deg_lcd(self, value):
        self.deg_lcd.display(value)
    def refresh(self):
        smokesignal.emit('refresh', self.camBox.isChecked())
            
class optWidget (QtGui.QWidget, opt_class):     #options window class
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QWidget.__init__(self,parent,*args)
        self.setupUi(self)
        self.resoBox.addItem('640x480')
        self.resoBox.addItem('800x600')
        self.resoBox.addItem('1280x960')
        self.connect(self.closeButton, QtCore.SIGNAL('clicked()'), self.closeopt)
        self.connect(self.scansrev_sdr, QtCore.SIGNAL('valueChanged(int)'), self.set_scansrev)
        self.connect(self.stepdelay_sdr, QtCore.SIGNAL('valueChanged(int)'), self.set_stepdelay)
        self.connect(self.pixbright_sdr, QtCore.SIGNAL('valueChanged(int)'), self.set_minpixbright)
        self.connect(self.lspinBox, QtCore.SIGNAL('valueChanged(int)'), self.setspinboxl)
        self.connect(self.rspinBox, QtCore.SIGNAL('valueChanged(int)'), self.setspinboxr)
        self.connect(self.uspinBox, QtCore.SIGNAL('valueChanged(int)'), self.setspinboxu)
        self.connect(self.dspinBox, QtCore.SIGNAL('valueChanged(int)'), self.setspinboxd)
        self.connect(self.comBox, QtCore.SIGNAL('currentIndexChanged(int)'), self.setcomport)
        self.connect(self.baudBox, QtCore.SIGNAL('currentIndexChanged(int)'), self.setbaudrate)
        #self.connect(self.comBox, QtCore.SIGNAL('clicked()'), setcombox) #cross module link
        self.resoBox.activated.connect(self.set_resolution)
        self.resoBox.setCurrentIndex(1)
        self.scansrev_sdr.setValue(globalsh.steptotake)
        self.pixbright_sdr.setValue(globalsh.minpixbright)
        self.pixbright_lbl.setText(str(globalsh.minpixbright))
        self.steps_lbl.setText(str(globalsh.steptotake))
        self.delay_lbl.setText(str(globalsh.stepdelay))
        self.lspinBox.setValue(int(globalsh.lspinBox))
        self.rspinBox.setValue(int(globalsh.rspinBox))
        self.uspinBox.setValue(int(globalsh.uspinBox))
        self.dspinBox.setValue(int(globalsh.dspinBox))
        self.scansrev_sdr.setValue(globalsh.steptotake)
        self.stepdelay_sdr.setValue(globalsh.stepdelay)
        self.comport = globalsh.comport
        self.baudrate = globalsh.baudrate
        for i in range(len(globalsh.availble_p)):    
            self.comBox.addItem(str(globalsh.availble_p[i]))
        self.com_index = self.comBox.findText(str(self.comport))
        self.comBox.setCurrentIndex(self.com_index);
        for i in range(len(globalsh.baudlist)):    
            self.baudBox.addItem(str(globalsh.baudlist[i]))
        self.baud_index = self.baudBox.findText(str(self.baudrate))
        self.baudBox.setCurrentIndex(self.baud_index);
        self.connectBox.setCheckState(globalsh.autocnct)
    def set_minpixbright(self):
        globalsh.minpixbright = self.pixbright_sdr.value()
        self.pixbright_lbl.setText(str(globalsh.minpixbright))
    def setautocnct(self):
        globalsh.autocnct = int(self.connectBox.checkState())
    def setbaudrate(self):
        globalsh.baudrate = self.baudBox.currentText()
    def setcomport(self):
        globalsh.comport = self.comBox.currentText()    
        
    def setspinboxl(self):
        #globalsh.lborder = int(interp(self.lspinBox.value(),[0,100],[0,camwidth/2])) 
        globalsh.lspinBox = self.lspinBox.value()
        smokesignal.emit('setborders')
    def setspinboxr(self):
        #globalsh.rborder = int(interp(self.rspinBox.value(),[0,100],[0,camwidth/2]))
        globalsh.rspinBox = self.rspinBox.value()
        smokesignal.emit('setborders')
    def setspinboxu(self):
        #globalsh.uborder = int(interp(self.uspinBox.value(),[0,100],[0,camheight/2]))
        globalsh.uspinBox = self.uspinBox.value()
        smokesignal.emit('setborders')
    def setspinboxd(self):
        #globalsh.dborder = int(interp(self.dspinBox.value(),[0,100],[0,camheight/2]))
        globalsh.dspinBox = self.dspinBox.value()
        smokesignal.emit('setborders')
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
#            cap.set(3,640)
#            cap.set(4,480)
            globalsh.camwidth = 640
            globalsh.camheight = 480
            #smokesignal.emit('capset_reso')
            #smokesignal.emit('capset', 4, globalsh.camheigth)
        if reso == 1:
#            cap.set(3,800)
#            cap.set(4,600)
            globalsh.camwidth = 800
            globalsh.camheight = 600
            #smokesignal.emit('capset_reso')
            #smokesignal.emit('capset', 4, globalsh.camheigth)
        if reso == 2:
#            cap.set(3,1280)
#            cap.set(4,960)
            globalsh.camwidth = 1280
            globalsh.camheight = 960
            #smokesignal.emit('capset_reso')
            #smokesignal.emit('capset', 4, globalsh.camheigth)
        smokesignal.emit('capset_reso')
        smokesignal.emit('setborders')
    def getopt(self):
        #print 'yess'
        self.show()
        self.move(360, 20)
    def closeopt(self):
        self.close()  
    def setcombox(self, value):
        self.comBox.addItem(value) 