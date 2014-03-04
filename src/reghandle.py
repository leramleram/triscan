# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:43:04 2014

@author: christian
"""


#import os
import globalsh
from _winreg import *
import smokesignal

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

def read_reg():     #load all registry entrys
    try:
        root_key=OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\CHAOSCOMPANY\cfg', 0, KEY_READ)
        [r_stepdelay,regtype]=(QueryValueEx(root_key,"stepdelay"))
        [r_steptotake,regtype]=(QueryValueEx(root_key,"steptotake"))
        [r_lspinbox,regtype]=(QueryValueEx(root_key,"lspinbox"))
        [r_rspinbox,regtype]=(QueryValueEx(root_key,"rspinbox"))
        [r_uspinbox,regtype]=(QueryValueEx(root_key,"uspinbox"))
        [r_dspinbox,regtype]=(QueryValueEx(root_key,"dspinbox"))
        [r_comport,regtype]=(QueryValueEx(root_key,"comport"))
        [r_baudrate,regtype]=(QueryValueEx(root_key,"baudrate"))
        [r_autocnct,regtype]=(QueryValueEx(root_key,"autocnct"))
        [r_minpixbright,regtype]=(QueryValueEx(root_key,"minpixbright"))
        #[r_dspinbox,regtype]=(QueryValueEx(root_key,"dummy"))
        globalsh.stepdelay = int(r_stepdelay)
        globalsh.steptotake = int(r_steptotake)
        globalsh.lspinBox = int(r_lspinbox)
        globalsh.rspinBox = int(r_rspinbox)
        globalsh.uspinBox = int(r_uspinbox)
        globalsh.dspinBox = int(r_dspinbox)
        globalsh.comport = int(r_comport)
        globalsh.baudrate = int(r_baudrate)
        globalsh.autocnct = int(r_autocnct)
        globalsh.minpixbright = int(r_minpixbright)
        CloseKey(root_key)
    except WindowsError:
        globalsh.dlg_issue = 'reg'
        globalsh.dlg_txt = 'oops, could not read Windows registry, perhaps first start? should i write the defaults? If not you have to enter all the values again each time aou restart the program...'
        smokesignal.emit('dialog')
        #write_reg_default()
        
def save_all():
    
    write_reg()
    
def write_reg():        #write config to registry
    keyVal = r'SOFTWARE\CHAOSCOMPANY\cfg'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "stepdelay", 0, REG_DWORD, int(globalsh.stepdelay))
    SetValueEx(key, "steptotake", 0, REG_DWORD, int(globalsh.steptotake))
    SetValueEx(key, "lspinbox", 0, REG_DWORD, int(globalsh.lspinBox))
    SetValueEx(key, "rspinbox", 0, REG_DWORD, int(globalsh.rspinBox))
    SetValueEx(key, "uspinbox", 0, REG_DWORD, int(globalsh.uspinBox))
    SetValueEx(key, "dspinbox", 0, REG_DWORD, int(globalsh.dspinBox))
    SetValueEx(key, "comport", 0, REG_DWORD, int(globalsh.comport))
    SetValueEx(key, "baudrate", 0, REG_DWORD, int(globalsh.baudrate))
    SetValueEx(key, "autocnct", 0, REG_DWORD, int(globalsh.autocnct))
    SetValueEx(key, "minpixbright", 0, REG_DWORD, int(globalsh.minpixbright))
    CloseKey(key)
    print 'keys written'

@smokesignal.on('write_def_reg')
def write_reg_default():        #write the default registry values 
    keyVal = r'SOFTWARE\CHAOSCOMPANY\cfg'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "stepdelay", 0, REG_DWORD, int(globalsh.stepdelay))
    SetValueEx(key, "steptotake", 0, REG_DWORD, int(globalsh.steptotake))
    SetValueEx(key, "lspinbox", 0, REG_DWORD, int(globalsh.lspinBox))
    SetValueEx(key, "rspinbox", 0, REG_DWORD, int(globalsh.rspinBox))
    SetValueEx(key, "uspinbox", 0, REG_DWORD, int(globalsh.uspinBox))
    SetValueEx(key, "dspinbox", 0, REG_DWORD, int(globalsh.dspinBox))
    SetValueEx(key, "comport", 0, REG_DWORD, int(globalsh.comport))
    SetValueEx(key, "baudrate", 0, REG_DWORD, int(globalsh.baudrate))
    SetValueEx(key, "autocnct", 0, REG_DWORD, int(globalsh.autocnct))
    SetValueEx(key, "minpixbright", 0, REG_DWORD, int(globalsh.minpixbright))
    CloseKey(key)
    print 'defaults written..'