# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:07:46 2014

@author: christian
"""

def runprogram():
    from PyQt4 import QtCore,QtGui,uic
    import sys
    app = QtGui.QApplication(sys.argv)
    import reghandle
    reghandle.read_reg()
    
    from serial_h import meiserial
    import scan
    from mygui import form, opt
    
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
    form.show()
    form.move(20,20)
    form.show()
    form.progress(0)
    app.exec_()

if __name__ == '__main__':
    runprogram() 
    
if True:
    pass
    
