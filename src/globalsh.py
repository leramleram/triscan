# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:08:26 2014

@author: christian
"""

global scan_active
scan_active = False

global lspinBox
global rspinBox
global uspinBox
global dspinBox

lspinBox = 76
rspinBox = 77
uspinBox = 60
dspinBox = 59

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
steptotake = 400
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
minpixbright = 90

global camwidth 
global camheight
global cambright
global camexpo
camwidth = 800
camheight = 600
cambright = 195
camexpo = 50

global l_angle
global r_angle
global cam_angle
l_angle = 32.0
r_angle = 32.0
cam_angle = 10.0

global filestamp
filestamp = 'no_file_stamp'