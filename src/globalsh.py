# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:08:26 2014

@author: christian
"""

global scan_active
scan_active = False

global cap
global lspinBox
global rspinBox
global uspinBox
global dspinBox

lspinBox = 21
rspinBox = 22
uspinBox = 23
dspinBox = 24

global lborder
global rborder
global uborder
global dborder

lborder = 0
rborder = 0
dborder = 0
uborder = 0

global progBarV
progBarV = 0

global updateBar
global steps_rev
global steptotake
global stepdelay
steps_rev = 400
steptotake = 10
stepdelay = 220

global dlg_title
global dlg_txt
dlg_title = 'default'
dlg_txt = 'default'

global dlg_issue
dlg_issue = 'default'

global availble_p
availble_p = []

global comport
comport = 15

global autocnct
autocnct = False

global baudrate
global baudlist
baudrate = 9600
baudlist = ('4800', '9600', '19200', '38400', '57600', '115200')

global minpixbright
minpixbright = 20

global camwidth 
global camheight
camwidth = 800
camheight = 600
