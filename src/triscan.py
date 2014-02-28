# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:07:46 2014

@author: christian
"""

def runprogram():
    from PyQt4 import QtCore,QtGui,uic
    import sys
    import reghandle
    reghandle.read_reg()
    import scan
    from serial_h import meiserial
    from mygui import MyWidget, optWidget, form, opt, app
    
    form.connect(form.toolButton, QtCore.SIGNAL('clicked()'), opt.show)
    form.connect(form.stepButton, QtCore.SIGNAL('clicked()'), meiserial.onestep)
    form.connect(form.turnButton, QtCore.SIGNAL('clicked()'), meiserial.turn)
    form.connect(form.scanButton, QtCore.SIGNAL('clicked()'), scan.doscan)
    form.connect(form.camBox, QtCore.SIGNAL('clicked()'), form.refresh)
    opt.connect(opt.saveButton, QtCore.SIGNAL('clicked()'), reghandle.save_all)
    form.show()
    form.move(20,20)
    form.progress(0)
    app.exec_()

if __name__ == '__main__':
    runprogram() 
    
if True:
    pass
    
