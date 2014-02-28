# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:43:04 2014

@author: christian
"""


#import os
import globalsh
from _winreg import *

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

def read_reg():
    try:
        root_key=OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\CHAOSCOMPANY\cfg', 0, KEY_READ)
        [r_stepdelay,regtype]=(QueryValueEx(root_key,"stepdelay"))
        [r_steptotake,regtype]=(QueryValueEx(root_key,"steptotake"))
        [r_lspinbox,regtype]=(QueryValueEx(root_key,"lspinbox"))
        [r_rspinbox,regtype]=(QueryValueEx(root_key,"rspinbox"))
        [r_uspinbox,regtype]=(QueryValueEx(root_key,"uspinbox"))
        [r_dspinbox,regtype]=(QueryValueEx(root_key,"dspinbox"))   
        #[r_dspinbox,regtype]=(QueryValueEx(root_key,"dummy"))
        globalsh.stepdelay = int(r_stepdelay)
        globalsh.steptotake = int(r_steptotake)
        globalsh.lspinBox = int(r_lspinbox)
        globalsh.rspinBox = int(r_rspinbox)
        globalsh.uspinBox = int(r_uspinbox)
        globalsh.dspinBox = int(r_dspinbox)
        CloseKey(root_key)
    except WindowsError:
        globalsh.dlg_issue = 'reg'
        globalsh.dlg_txt = 'oops, could not read Windows registry, perhaps first start?\nI can (re)build it with default values, do you want me to do so?'
                
        
def save_all():
    
    write_reg()
    
def write_reg():
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
    CloseKey(key)
    print 'keys written'
def write_reg_default():
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
    CloseKey(key)
    print 'defaults written..'