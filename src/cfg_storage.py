# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 18:48:26 2014

@author: christian
"""

import json
import globalsh
import smokesignal

@smokesignal.on('write_json')
def write_file():
    entry = {'stepdelay' : int(globalsh.stepdelay), 'steptotake' : int(globalsh.steptotake), 'lspinBox' : int(globalsh.lspinBox), 'rspinBox' : int(globalsh.rspinBox), 'uspinBox' : int(globalsh.uspinBox), 'dspinBox' : int(globalsh.dspinBox), 'comport' : int(globalsh.comport), 'baudrate' : int(globalsh.baudrate), 'autocnct' : int(globalsh.autocnct), 'minpixbright' : int(globalsh.minpixbright)}
    with open('settings.json', 'w') as f:
        json.dump(entry, f, indent = 2)

@smokesignal.on('read_json')     
def read_file():
    try:
        with open('settings.json', 'r') as f:
            retain = json.load(f)
            globalsh.stepdelay = int(retain['stepdelay'])
            globalsh.steptotake = int(retain['steptotake'])
            globalsh.lspinBox = int(retain['lspinBox'])
            globalsh.rspinBox = int(retain['rspinBox'])
            globalsh.uspinBox = int(retain['uspinBox'])
            globalsh.dspinBox = int(retain['dspinBox'])
            globalsh.comport = int(retain['comport'])
            globalsh.baudrate = int(retain['baudrate'])
            globalsh.autocnct = int(retain['autocnct'])
            globalsh.minpixbright = int(retain['minpixbright'])
    except ValueError:
        entry = {'stepdelay' : int(globalsh.stepdelay), 'steptotake' : int(globalsh.steptotake), 'lspinBox' : int(globalsh.lspinBox), 'rspinBox' : int(globalsh.rspinBox), 'uspinBox' : int(globalsh.uspinBox), 'dspinBox' : int(globalsh.dspinBox), 'comport' : int(globalsh.comport), 'baudrate' : int(globalsh.baudrate), 'autocnct' : int(globalsh.autocnct), 'minpixbright' : int(globalsh.minpixbright)}
        with open('settings.json', 'w') as f:
            json.dump(entry, f, indent = 2)
        print 'defaults written'
    except IOError:
        entry = {'stepdelay' : int(globalsh.stepdelay), 'steptotake' : int(globalsh.steptotake), 'lspinBox' : int(globalsh.lspinBox), 'rspinBox' : int(globalsh.rspinBox), 'uspinBox' : int(globalsh.uspinBox), 'dspinBox' : int(globalsh.dspinBox), 'comport' : int(globalsh.comport), 'baudrate' : int(globalsh.baudrate), 'autocnct' : int(globalsh.autocnct), 'minpixbright' : int(globalsh.minpixbright)}
        with open('settings.json', 'w') as f:
            json.dump(entry, f, indent = 2)
        print 'defaults written'