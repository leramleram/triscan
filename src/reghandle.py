# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:43:04 2014

@author: christian
"""


import os
import globalsh
from _winreg import *
from mygui import dlg
from PyQt4 import QtCore

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

def read_reg():
    try:
        root_key=OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\CHAOSCOMPANY\cfg', 0, KEY_READ)
        [globalsh.stepdelay,regtype]=(QueryValueEx(root_key,"stepdelay"))
        [globalsh.steptotake,regtype]=(QueryValueEx(root_key,"steptotake"))
        [globalsh.lspinbox,regtype]=(QueryValueEx(root_key,"lspinbox"))
        [globalsh.rspinbox,regtype]=(QueryValueEx(root_key,"rspinbox"))
        [globalsh.uspinbox,regtype]=(QueryValueEx(root_key,"uspinbox"))
        [globalsh.dspinbox,regtype]=(QueryValueEx(root_key,"dspinbox"))    
        globalsh.stepdelay = int(globalsh.stepdelay)
        globalsh.steptotake = int(globalsh.steptotake)
        globalsh.lspinbox = int(globalsh.lspinbox)
        globalsh.rspinbox = int(globalsh.rspinbox)
        globalsh.uspinbox = int(globalsh.uspinbox)
        globalsh.dspinbox = int(globalsh.dspinbox)
        CloseKey(root_key)
    except WindowsError:
        print 'oops, could not read Windows registry, perhaps first start?'
        print 'I can (re)build it with default values, do you want me to do so?'
        dlg.connect(dlg.btnBox_dlg, QtCore.SIGNAL('accepted()'), write_reg_default)
        dlg.setWindowTitle('heheheh')
        dlg.label_dlg.setText('Oops...  could not read Windows registry, perhaps first start?\n I can (re)build it with default values, do you want me to do so?' )
        dlg.getdlg()
    
        
        
def write_reg():
    keyVal = r'SOFTWARE\CHAOSCOMPANY\cfg'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "stepdelay", 0, REG_SZ, str(globalsh.stepdelay))
    SetValueEx(key, "steptotake", 0, REG_SZ, str(globalsh.steptotake))
    SetValueEx(key, "lspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "rspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "uspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "dspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    CloseKey(key)
def write_reg_default():
    keyVal = r'SOFTWARE\CHAOSCOMPANY\cfg'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "stepdelay", 0, REG_SZ, str(globalsh.stepdelay))
    SetValueEx(key, "steptotake", 0, REG_SZ, str(globalsh.steptotake))
    SetValueEx(key, "lspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "rspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "uspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    SetValueEx(key, "dspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    CloseKey(key)
    print 'defaults written..'