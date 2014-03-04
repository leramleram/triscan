# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 18:05:48 2014

@author: christian
"""
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random
import globalsh
import smokesignal
import matplotlib.pyplot as plt
fig = pylab.figure()
ax = Axes3D(fig)
@smokesignal.on('showplot')
def showplot():
    pyplot.show()
@smokesignal.on('drawplot')
def drawplot():
    if globalsh.plotlock == False:
        ax.scatter(globalsh.X_plot, globalsh.Y_plot, globalsh.Z_plot)
        pyplot.draw()