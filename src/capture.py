# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:21:57 2014

@author: christian
"""

import cv2
import smokesignal
import globalsh
from numpy import interp
import time

#class capture(cv.VideoCapture()):
#    def __init__(self):
#        self.set(3, 800)
#        self.set(4, 600)
#        self.camwidth = self.get(3)
#        self.camheight = self.get(4)
#        self.fps = self.get(5)

cap = cv2.VideoCapture(0)
time.sleep(0.5)
cap.set(3, globalsh.camwidth)
cap.set(4, globalsh.camheight)
#cap.camwidth = cap.get(3)
#cap.camheight = cap.get(4)
#cap.fps = cap.get(5)

@smokesignal.on('capset_reso')
def set_reso():
    cap.set(3, globalsh.camwidth)
    cap.set(4, globalsh.camheight)
    
@smokesignal.on('refresh')    
def refresh(state):
        cap.open(0)
        camstate = state
        cap.set(3, globalsh.camwidth)
        cap.set(4, globalsh.camheight)
        smokesignal.emit('setborders')
        if camstate == 0:
            cv2.destroyAllWindows()
            camBox.setCheckState(0)
        while camstate == 2:
            #print 'yoaha'
            ret, feed = cap.read()  #first we draw a cross in the middle of the video frame
            cv2.line(feed,(int(globalsh.camwidth / 2),0),(int(globalsh.camwidth/2),int(globalsh.camheight)),(255,0,0),2)
            cv2.line(feed,(0,int(globalsh.camheight/2)),(int(globalsh.camwidth),int(globalsh.camheight/2)),(255,0,0),2)
            #then we draw the limitation lines
            cv2.line(feed,(globalsh.lborder,0),(globalsh.lborder,int(globalsh.camheight)),(0,255,0),2)
            cv2.line(feed,(int(globalsh.camwidth) - globalsh.rborder,0),(int(globalsh.camwidth) - globalsh.rborder,int(globalsh.camheight)),(0,255,0),2)
            cv2.line(feed,(0,globalsh.uborder),(int(globalsh.camwidth),globalsh.uborder),(255,255,0),2)
            cv2.line(feed,(0,int(globalsh.camheight) - globalsh.dborder),(int(globalsh.camwidth),int(globalsh.camheight) - globalsh.dborder),(255,255,0),2)        
            cv2.imshow("webcam", feed)
            #time.sleep(0.02)
            key = cv2.waitKey(20)
            if key in [27, ord('Q'), ord('q')]: # exit on ESC
                cv2.destroyAllWindows()
                #self.camBox.setCheckState(0)
                break
            
@smokesignal.on('setborders')
def setborders():
    
    globalsh.lborder = int(interp(globalsh.lspinBox,[0,100],[0,globalsh.camwidth/2])) 
    globalsh.rborder = int(interp(globalsh.rspinBox,[0,100],[0,globalsh.camwidth/2]))
    globalsh.uborder = int(interp(globalsh.uspinBox,[0,100],[0,globalsh.camheight/2]))
    globalsh.dborder = int(interp(globalsh.dspinBox,[0,100],[0,globalsh.camheight/2]))
