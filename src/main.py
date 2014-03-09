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
    import cfg_storage
    smokesignal.emit('read_json')
    from ardu import meiserial
    import capture
    import scan
    from mygui import MyWidget, optWidget, aboutWidget
    import numpy
    import serial
    import globalsh
    
    form = MyWidget(None)
    opt = optWidget(None)
    about = aboutWidget(None)
    form.execButton.setEnabled(False)
    
    @smokesignal.on('killme')
    def killme():                                                                                   #close the program
        opt.close()
        form.close()
    @smokesignal.on('progress')
    def setbar(value):                                                                              #update progress bar
        form.progress(value)
    @smokesignal.on('lcd')
    def setlcd(value):                                                                              #update the numberLCD
        form.set_deg_lcd(value)
    @smokesignal.on('status')
    def setstatus(string):                                                                          #update the statusmessage
        form.status_lbl.setText(string)
    @smokesignal.on('scanbtnstate')
    def setscanbtnstate(state):                                                                     #update the scanbuttonstate
        form.scanButton.setChecked(state)
    @smokesignal.on('btn_lock')
    def disable_btn():                                                                              #lock all buttons while scanning
        opt.close()
        form.turnButton.setEnabled(False) 
        form.stepButton.setEnabled(False) 
        #form.toolButton.setEnabled(False) 
        form.lLaserBox.setEnabled(False)
        form.rLaserBox.setEnabled(False)
        form.lft_rd_btn.setEnabled(False)
        form.rgt_rd_btn.setEnabled(False)
        form.dual_rd_btn.setEnabled(False)
        form.lightBox.setEnabled(False)
    @smokesignal.on('btn_unlock')
    def enable_btn():                                                                               #unlock the buttons
        form.turnButton.setEnabled(True) 
        form.stepButton.setEnabled(True) 
        #form.toolButton.setEnabled(True)
        form.lLaserBox.setEnabled(True)
        form.rLaserBox.setEnabled(True)
        form.lft_rd_btn.setEnabled(True)
        form.rgt_rd_btn.setEnabled(True)
        form.dual_rd_btn.setEnabled(True)
        form.scanButton.setEnabled(True)
        form.lightBox.setEnabled(True)
        form.execButton.setEnabled(True)
    def initscan():
        if form.rgt_rd_btn.isChecked() == True:
            scan.doscan('r')
        elif form.lft_rd_btn.isChecked() == True:
            scan.doscan('l')
        elif form.dual_rd_btn.isChecked() == True:
            scan.doscan('d')

    form.connect(form.toolButton, QtCore.SIGNAL('clicked()'), opt.getopt)
    form.connect(form.execButton, QtCore.SIGNAL('clicked()'), scan.openfile)
    form.connect(form.stepButton, QtCore.SIGNAL('clicked()'), meiserial.onestep)
    form.connect(form.turnButton, QtCore.SIGNAL('clicked()'), meiserial.turn)
    form.connect(form.scanButton, QtCore.SIGNAL('clicked()'), initscan)
    form.lLaserBox.clicked.connect(lambda:  meiserial.laser(0,int(form.lLaserBox.isChecked())))
    form.rLaserBox.clicked.connect(lambda:  meiserial.laser(1,int(form.rLaserBox.isChecked())))
    form.lightBox.clicked.connect(lambda:  meiserial.light(int(form.lightBox.isChecked())))
    form.connect(form.camBox, QtCore.SIGNAL('clicked()'), form.refresh)
    opt.connect(opt.saveButton, QtCore.SIGNAL('clicked()'), cfg_storage.write_file)
    opt.connect(opt.connectBtn, QtCore.SIGNAL('clicked()'), meiserial.connect_p)
    opt.connect(opt.connectBox, QtCore.SIGNAL('clicked()'), opt.setautocnct)
    opt.connect(opt.aboutButton, QtCore.SIGNAL('clicked()'), about.getabout)
       
    form.show()                                                                                     #show the main window
    form.move(20,20)
    form.show()
    form.progress(0)
    print globalsh.camexpo
    smokesignal.emit('setcamexpo', globalsh.camexpo)
    if meiserial.connected == False:
        disable_btn()
        form.scanButton.setEnabled(False)
        form.execButton.setEnabled(False)
        smokesignal.emit('status', 'no serial connection')
    app.exec_()
    if True:
        meiserial.__del__()
        form.__del__()
if __name__ == '__main__':
    runprogram() 
    
if True:
    pass
    
