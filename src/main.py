# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:07:46 2014

@author: christian
"""

def runprogram():
    from PyQt4 import QtCore,QtGui,uic
    import sys
    import smokesignal
    app = QtGui.QApplication(sys.argv)
    import reghandle
    reghandle.read_reg()
    from serial_h import meiserial
    import capture
    import scan
    from mygui import MyWidget, optWidget
    
    form = MyWidget(None)
    opt = optWidget(None)
    
    
    @smokesignal.on('killme')
    def killme():   #close the program
        opt.close()
        form.close()
    @smokesignal.on('progress')
    def setbar(value):  #update progress bar
        form.progress(value)
    @smokesignal.on('lcd')
    def setlcd(value):      #update the numberLCD
        form.set_deg_lcd(value)
    @smokesignal.on('status')
    def setstatus(string):  #update the statusmessage
        form.status_lbl.setText(string)
    @smokesignal.on('scanbtnstate')
    def setscanbtnstate(state): #update the scanbuttonstate
        form.scanButton.setChecked(state)
    @smokesignal.on('btn_lock')
    def disable_btn():  #lock all buttons while scanning
        opt.close()
        form.turnButton.setEnabled(False) 
        form.stepButton.setEnabled(False) 
        form.toolButton.setEnabled(False) 
        form.lLaserBox.setEnabled(False)
        form.rLaserBox.setEnabled(False)
        form.lft_rd_btn.setEnabled(False)
        form.rgt_rd_btn.setEnabled(False)
        form.dual_rd_btn.setEnabled(False)
    @smokesignal.on('btn_unlock')
    def enable_btn():   #unlock the buttons
        form.turnButton.setEnabled(True) 
        form.stepButton.setEnabled(True) 
        form.toolButton.setEnabled(True)
        form.lLaserBox.setEnabled(True)
        form.rLaserBox.setEnabled(True)
        form.lft_rd_btn.setEnabled(True)
        form.rgt_rd_btn.setEnabled(True)
        form.dual_rd_btn.setEnabled(True)
        
    form.connect(form.toolButton, QtCore.SIGNAL('clicked()'), opt.getopt)
    form.connect(form.stepButton, QtCore.SIGNAL('clicked()'), meiserial.onestep)
    form.connect(form.turnButton, QtCore.SIGNAL('clicked()'), meiserial.turn)
    form.connect(form.scanButton, QtCore.SIGNAL('clicked()'), scan.doscan)
    form.lLaserBox.clicked.connect(lambda:  meiserial.laser(0,int(form.lLaserBox.checkState())))
    form.rLaserBox.clicked.connect(lambda:  meiserial.laser(1,int(form.rLaserBox.checkState())))
    form.connect(form.camBox, QtCore.SIGNAL('clicked()'), form.refresh)
    opt.connect(opt.saveButton, QtCore.SIGNAL('clicked()'), reghandle.save_all)
    opt.connect(opt.connectBtn, QtCore.SIGNAL('clicked()'), meiserial.connect_p)
    opt.connect(opt.connectBox, QtCore.SIGNAL('clicked()'), opt.setautocnct)
    form.show()     #main window
    form.move(20,20)
    form.show()
    form.progress(0)
    app.exec_()

if __name__ == '__main__':
    runprogram() 
    
if True:
    pass
    
