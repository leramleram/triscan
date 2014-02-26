# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:43:04 2014

@author: christian
"""


import os
import globalsh
from _winreg import *

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

def read_reg():
    root_key=OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\CHAOSCOMPANY\cfg', 0, KEY_READ)
    [globalsh.stepdelay,regtype]=(QueryValueEx(root_key,"stepdelay"))
    [globalsh.steptotake,regtype]=(QueryValueEx(root_key,"steptotake"))
    [globalsh.lspinbox,regtype]=(QueryValueEx(root_key,"lspinbox"))
    globalsh.steptotake = int(globalsh.steptotake)
    print globalsh.steptotake
    CloseKey(root_key)
    
def write_reg():
    keyVal = r'SOFTWARE\CHAOSCOMPANY\cfg'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "stepdelay", 0, REG_SZ, str(globalsh.stepdelay))
    SetValueEx(key, "steptotake", 0, REG_SZ, str(globalsh.steptotake))
    SetValueEx(key, "lspinbox", 0, REG_SZ, str(globalsh.lspinBox))
    CloseKey(key)
