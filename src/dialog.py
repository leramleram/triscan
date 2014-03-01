# -*- coding: utf-8 -*-
"""
Created on Sat Mar 01 19:17:29 2014

@author: christian
"""
from PyQt4 import QtCore,QtGui,uic
import smokesignal
import globalsh

dlg_class, base_class = uic.loadUiType("dlg.ui")
            
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

dlg = dlgWidget(None)

@smokesignal.on('dialog')
def get_dialog():
    dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('accepted()'), dlg_accept)
    dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('rejected()'), dlg_reject)
    dlg.setWindowTitle(globalsh.dlg_title)
    dlg.label_dlg.setText(globalsh.dlg_txt)
    dlg.getdlg()
    
def dlg_accept():
    if globalsh.dlg_issue == 'ser':
        print 'juouhou'
    if globalsh.dlg_issue == 'reg':
        smokesignal.emit('write_def_reg')
        #reghandle.write_reg_default
        
def dlg_reject():
    if globalsh.dlg_issue == 'ser':
        print 'exiting'
        exit()
    if globalsh.dlg_issue == 'reg':
        #smokesignal.emit('write_def_reg')
        pass
    
    