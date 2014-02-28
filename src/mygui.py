# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 04:14:31 2014

@author: christian
"""
from PyQt4 import QtCore,QtGui,uic
import sys
from numpy import interp
from capture import cap
from globalsh import *
import globalsh
import cv2
import reghandle
form_class, base_class = uic.loadUiType("main.ui")
opt_class, base_class = uic.loadUiType("opt.ui")
dlg_class, base_class = uic.loadUiType("dlg.ui")

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
    def set_deg_lcd(self, value):
        self.deg_lcd.display(value)
    def refresh(self):
        cap.open(0)
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
    
    def setautocnct(self):
        globalsh.autocnct = int(self.connectBox.checkState())
    def setbaudrate(self):
        globalsh.baudrate = self.baudBox.currentText()
    def setcomport(self):
        globalsh.comport = self.comBox.currentText()
    def setspinboxl(self):
        globalsh.lspinBox = self.lspinBox.value()
    def setspinboxr(self):
        globalsh.rspinBox = self.rspinBox.value()
    def setspinboxu(self):
        globalsh.uspinBox = self.uspinBox.value()
    def setspinboxd(self):
        globalsh.dspinBox = self.dspinBox.value()
        
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
            
            
class dlgWidget (QtGui.QDialog, dlg_class):
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QDialog.__init__(self,parent,*args)
        #self.dialog = QtGui.QDialog(parent)
        self.setupUi(self)
    def getdlg(self,):
        #self.setWindowTitle('meidialog')
        self.show()
        
    def closedlg(self):
        self.close()

app = QtGui.QApplication(sys.argv)
form = MyWidget(None)
opt = optWidget(None)
dlg = dlgWidget(None)

def setbar(value):
    form.progress(value)
def setlcd(value):
    form.set_deg_lcd(value)
    
def get_dialog():
    dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('accepted()'), dlg_accept)
    dlg.setWindowTitle(globalsh.dlg_title)
    dlg.label_dlg.setText(globalsh.dlg_txt)
    dlg.getdlg()
    
def dlg_accept():
    if globalsh.dlg_issue == 'serial':
        pass
    if globalsh.dlg_issue == 'reg':
        reghandle.write_reg_default
    
import scan
