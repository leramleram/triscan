# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:21:57 2014

@author: christian
"""

import cv2



class capture(cv2.VideoCapture()):
    def __init__(self):
        self.set(3, 800)
        self.set(4, 600)
        self.camwidth = self.get(3)
        self.camheight = self.get(4)
        self.fps = self.get(5)

cap = cv2.VideoCapture(0)
