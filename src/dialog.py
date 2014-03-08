# -*- coding: utf-8 -*-
"""
Created on Sat Mar 01 19:17:29 2014

@author: christian
"""
from PyQt4 import QtCore,QtGui,uic
import smokesignal
import globalsh
import dlg_ui
from dlg_ui import Ui_dlg
#dlg_class, base_class = uic.loadUiType("dlg.ui")
            
class dlgWidget (QtGui.QDialog, Ui_dlg):     #warnings dialog
    def __init__(self,parent=None,selected=[],flag=0,*args):
        QtGui.QDialog.__init__(self,parent,*args)
        self.setupUi(self)
    def getdlg(self,):
        self.show()
    def closedlg(self):
        self.close()
        
dlg = dlgWidget(None)

@smokesignal.on('dialog')
def get_dialog():   #call the warnings dialog
    dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('accepted()'), dlg_accept)
    dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('rejected()'), dlg_reject)
    dlg.setWindowTitle(globalsh.dlg_title)
    dlg.label_dlg.setText(globalsh.dlg_txt)
    dlg.getdlg()
    
def dlg_accept():
    if globalsh.dlg_issue == 'ser':
        print 'juouhou'
    if globalsh.dlg_issue == 'reg':
        smokesignal.emit('write_json')
        #reghandle.write_reg_default
        
def dlg_reject():
    if globalsh.dlg_issue == 'ser':
        print 'exiting'
        smokesignal.emit('killme')
    if globalsh.dlg_issue == 'reg':
        #smokesignal.emit('write_def_reg')
        print 'exiting'
        smokesignal.emit('killme')
    
    