# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\christian\Documents\GitHub\triscan\gui\opt.ui'
#
# Created: Mon Mar 10 21:26:52 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_optwndw(object):
    def setupUi(self, optwndw):
        optwndw.setObjectName(_fromUtf8("optwndw"))
        optwndw.setWindowModality(QtCore.Qt.WindowModal)
        optwndw.resize(338, 297)
        self.closeButton = QtGui.QPushButton(optwndw)
        self.closeButton.setGeometry(QtCore.QRect(245, 265, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/48x48/png/48x48/Run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.saveButton = QtGui.QPushButton(optwndw)
        self.saveButton.setGeometry(QtCore.QRect(155, 265, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/48x48/png/48x48/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.tabWidget = QtGui.QTabWidget(optwndw)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 326, 251))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 321, 181))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.cambright_sdr = QtGui.QSlider(self.frame)
        self.cambright_sdr.setGeometry(QtCore.QRect(20, 65, 281, 19))
        self.cambright_sdr.setMaximum(255)
        self.cambright_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.cambright_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cambright_sdr.setTickInterval(25)
        self.cambright_sdr.setObjectName(_fromUtf8("cambright_sdr"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pixbright_sdr = QtGui.QSlider(self.frame)
        self.pixbright_sdr.setGeometry(QtCore.QRect(20, 30, 281, 19))
        self.pixbright_sdr.setMinimum(10)
        self.pixbright_sdr.setMaximum(255)
        self.pixbright_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.pixbright_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.pixbright_sdr.setTickInterval(25)
        self.pixbright_sdr.setObjectName(_fromUtf8("pixbright_sdr"))
        self.pixbright_lbl = QtGui.QLabel(self.frame)
        self.pixbright_lbl.setGeometry(QtCore.QRect(165, 10, 41, 21))
        self.pixbright_lbl.setObjectName(_fromUtf8("pixbright_lbl"))
        self.cambright_lbl = QtGui.QLabel(self.frame)
        self.cambright_lbl.setGeometry(QtCore.QRect(165, 45, 41, 21))
        self.cambright_lbl.setObjectName(_fromUtf8("cambright_lbl"))
        self.exposure_sdr = QtGui.QSlider(self.frame)
        self.exposure_sdr.setGeometry(QtCore.QRect(20, 100, 281, 19))
        self.exposure_sdr.setMinimum(0)
        self.exposure_sdr.setMaximum(5)
        self.exposure_sdr.setSingleStep(1)
        self.exposure_sdr.setPageStep(1)
        self.exposure_sdr.setSliderPosition(0)
        self.exposure_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.exposure_sdr.setInvertedAppearance(False)
        self.exposure_sdr.setInvertedControls(False)
        self.exposure_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.exposure_sdr.setTickInterval(1)
        self.exposure_sdr.setObjectName(_fromUtf8("exposure_sdr"))
        self.exposure_lbl = QtGui.QLabel(self.frame)
        self.exposure_lbl.setGeometry(QtCore.QRect(165, 80, 41, 21))
        self.exposure_lbl.setObjectName(_fromUtf8("exposure_lbl"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gain_lbl = QtGui.QLabel(self.frame)
        self.gain_lbl.setGeometry(QtCore.QRect(165, 120, 41, 21))
        self.gain_lbl.setObjectName(_fromUtf8("gain_lbl"))
        self.gain_sdr = QtGui.QSlider(self.frame)
        self.gain_sdr.setGeometry(QtCore.QRect(20, 140, 281, 19))
        self.gain_sdr.setMinimum(0)
        self.gain_sdr.setMaximum(5000)
        self.gain_sdr.setPageStep(1)
        self.gain_sdr.setSliderPosition(0)
        self.gain_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.gain_sdr.setInvertedAppearance(False)
        self.gain_sdr.setInvertedControls(False)
        self.gain_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.gain_sdr.setTickInterval(25)
        self.gain_sdr.setObjectName(_fromUtf8("gain_sdr"))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.resoBox = QtGui.QComboBox(self.tab)
        self.resoBox.setGeometry(QtCore.QRect(205, 205, 101, 22))
        self.resoBox.setObjectName(_fromUtf8("resoBox"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(205, 185, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame_2 = QtGui.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 316, 231))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.scanrev_lbl = QtGui.QLabel(self.frame_2)
        self.scanrev_lbl.setGeometry(QtCore.QRect(25, 5, 131, 16))
        self.scanrev_lbl.setObjectName(_fromUtf8("scanrev_lbl"))
        self.scansrev_sdr = QtGui.QSlider(self.frame_2)
        self.scansrev_sdr.setGeometry(QtCore.QRect(15, 25, 286, 19))
        self.scansrev_sdr.setMinimum(100)
        self.scansrev_sdr.setMaximum(400)
        self.scansrev_sdr.setSingleStep(100)
        self.scansrev_sdr.setPageStep(100)
        self.scansrev_sdr.setSliderPosition(100)
        self.scansrev_sdr.setTracking(True)
        self.scansrev_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.scansrev_sdr.setInvertedAppearance(False)
        self.scansrev_sdr.setInvertedControls(False)
        self.scansrev_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.scansrev_sdr.setTickInterval(100)
        self.scansrev_sdr.setObjectName(_fromUtf8("scansrev_sdr"))
        self.steps_lbl = QtGui.QLabel(self.frame_2)
        self.steps_lbl.setGeometry(QtCore.QRect(85, 5, 41, 21))
        self.steps_lbl.setObjectName(_fromUtf8("steps_lbl"))
        self.stepdelay_sdr = QtGui.QSlider(self.frame_2)
        self.stepdelay_sdr.setGeometry(QtCore.QRect(15, 65, 286, 19))
        self.stepdelay_sdr.setMinimum(100)
        self.stepdelay_sdr.setMaximum(1200)
        self.stepdelay_sdr.setSingleStep(10)
        self.stepdelay_sdr.setPageStep(50)
        self.stepdelay_sdr.setProperty("value", 200)
        self.stepdelay_sdr.setSliderPosition(200)
        self.stepdelay_sdr.setTracking(True)
        self.stepdelay_sdr.setOrientation(QtCore.Qt.Horizontal)
        self.stepdelay_sdr.setInvertedAppearance(False)
        self.stepdelay_sdr.setInvertedControls(False)
        self.stepdelay_sdr.setTickPosition(QtGui.QSlider.TicksAbove)
        self.stepdelay_sdr.setTickInterval(100)
        self.stepdelay_sdr.setObjectName(_fromUtf8("stepdelay_sdr"))
        self.stepdelay_lbl = QtGui.QLabel(self.frame_2)
        self.stepdelay_lbl.setGeometry(QtCore.QRect(25, 45, 131, 16))
        self.stepdelay_lbl.setObjectName(_fromUtf8("stepdelay_lbl"))
        self.delay_lbl = QtGui.QLabel(self.frame_2)
        self.delay_lbl.setGeometry(QtCore.QRect(85, 45, 41, 21))
        self.delay_lbl.setObjectName(_fromUtf8("delay_lbl"))
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(130, 150, 181, 76))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.dspinBox = QtGui.QSpinBox(self.frame_3)
        self.dspinBox.setGeometry(QtCore.QRect(66, 50, 51, 22))
        self.dspinBox.setMaximum(100)
        self.dspinBox.setSingleStep(2)
        self.dspinBox.setProperty("value", 0)
        self.dspinBox.setObjectName(_fromUtf8("dspinBox"))
        self.rspinBox = QtGui.QSpinBox(self.frame_3)
        self.rspinBox.setGeometry(QtCore.QRect(125, 25, 51, 22))
        self.rspinBox.setMaximum(100)
        self.rspinBox.setSingleStep(2)
        self.rspinBox.setProperty("value", 0)
        self.rspinBox.setObjectName(_fromUtf8("rspinBox"))
        self.lspinBox = QtGui.QSpinBox(self.frame_3)
        self.lspinBox.setGeometry(QtCore.QRect(5, 25, 51, 22))
        self.lspinBox.setMaximum(100)
        self.lspinBox.setSingleStep(2)
        self.lspinBox.setProperty("value", 0)
        self.lspinBox.setObjectName(_fromUtf8("lspinBox"))
        self.uspinBox = QtGui.QSpinBox(self.frame_3)
        self.uspinBox.setGeometry(QtCore.QRect(66, 5, 51, 22))
        self.uspinBox.setFrame(True)
        self.uspinBox.setMaximum(100)
        self.uspinBox.setSingleStep(2)
        self.uspinBox.setProperty("value", 0)
        self.uspinBox.setObjectName(_fromUtf8("uspinBox"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(55, 25, 61, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame_6 = QtGui.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(5, 90, 306, 61))
        self.frame_6.setFrameShape(QtGui.QFrame.Box)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_11 = QtGui.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(205, 5, 101, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.r_angleBox = QtGui.QDoubleSpinBox(self.frame_6)
        self.r_angleBox.setGeometry(QtCore.QRect(115, 30, 62, 22))
        self.r_angleBox.setDecimals(2)
        self.r_angleBox.setMaximum(90.0)
        self.r_angleBox.setSingleStep(0.5)
        self.r_angleBox.setObjectName(_fromUtf8("r_angleBox"))
        self.cam_angleBox = QtGui.QDoubleSpinBox(self.frame_6)
        self.cam_angleBox.setGeometry(QtCore.QRect(215, 30, 62, 22))
        self.cam_angleBox.setMaximum(90.0)
        self.cam_angleBox.setSingleStep(0.5)
        self.cam_angleBox.setObjectName(_fromUtf8("cam_angleBox"))
        self.label_6 = QtGui.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(105, 5, 96, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_10 = QtGui.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(10, 5, 96, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.l_angleBox = QtGui.QDoubleSpinBox(self.frame_6)
        self.l_angleBox.setGeometry(QtCore.QRect(20, 30, 62, 22))
        self.l_angleBox.setDecimals(2)
        self.l_angleBox.setMaximum(90.0)
        self.l_angleBox.setSingleStep(0.5)
        self.l_angleBox.setObjectName(_fromUtf8("l_angleBox"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame_4 = QtGui.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 316, 231))
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_7 = QtGui.QFrame(self.frame_4)
        self.frame_7.setGeometry(QtCore.QRect(155, 20, 156, 61))
        self.frame_7.setFrameShape(QtGui.QFrame.Box)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.connectBtn = QtGui.QPushButton(self.frame_7)
        self.connectBtn.setGeometry(QtCore.QRect(80, 35, 71, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/myres/png/48x48/OK.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectBtn.setIcon(icon2)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.connectBox = QtGui.QCheckBox(self.frame_7)
        self.connectBox.setGeometry(QtCore.QRect(15, 5, 91, 17))
        self.connectBox.setObjectName(_fromUtf8("connectBox"))
        self.frame_8 = QtGui.QFrame(self.frame_4)
        self.frame_8.setGeometry(QtCore.QRect(5, 20, 146, 61))
        self.frame_8.setFrameShape(QtGui.QFrame.Box)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.label_9 = QtGui.QLabel(self.frame_8)
        self.label_9.setGeometry(QtCore.QRect(0, 35, 61, 16))
        self.label_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comBox = QtGui.QComboBox(self.frame_8)
        self.comBox.setGeometry(QtCore.QRect(65, 5, 71, 21))
        self.comBox.setObjectName(_fromUtf8("comBox"))
        self.baudBox = QtGui.QComboBox(self.frame_8)
        self.baudBox.setGeometry(QtCore.QRect(65, 35, 71, 21))
        self.baudBox.setObjectName(_fromUtf8("baudBox"))
        self.label_8 = QtGui.QLabel(self.frame_8)
        self.label_8.setGeometry(QtCore.QRect(0, 5, 61, 16))
        self.label_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.frame_5 = QtGui.QFrame(self.tab_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 316, 231))
        self.frame_5.setFrameShape(QtGui.QFrame.Box)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.selectfileButton = QtGui.QPushButton(self.frame_5)
        self.selectfileButton.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.selectfileButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/48x48/png/48x48/View.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectfileButton.setIcon(icon3)
        self.selectfileButton.setIconSize(QtCore.QSize(24, 24))
        self.selectfileButton.setObjectName(_fromUtf8("selectfileButton"))
        self.folderlabel = QtGui.QTextEdit(self.frame_5)
        self.folderlabel.setGeometry(QtCore.QRect(10, 60, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.folderlabel.setFont(font)
        self.folderlabel.setObjectName(_fromUtf8("folderlabel"))
        self.label_3 = QtGui.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(70, 25, 211, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.aboutButton = QtGui.QPushButton(self.frame_5)
        self.aboutButton.setGeometry(QtCore.QRect(280, 195, 31, 31))
        self.aboutButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/48x48/png/48x48/Info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutButton.setIcon(icon4)
        self.aboutButton.setIconSize(QtCore.QSize(24, 24))
        self.aboutButton.setObjectName(_fromUtf8("aboutButton"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(optwndw)
        self.tabWidget.setCurrentIndex(3)
        self.resoBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(optwndw)

    def retranslateUi(self, optwndw):
        optwndw.setWindowTitle(_translate("optwndw", "Options ▲Δ", None))
        self.closeButton.setText(_translate("optwndw", "close", None))
        self.saveButton.setText(_translate("optwndw", "save", None))
        self.cambright_sdr.setToolTip(_translate("optwndw", "webcam brightness", None))
        self.label_2.setText(_translate("optwndw", "Webcam Brightness", None))
        self.label.setText(_translate("optwndw", "Minimum pixel brightness", None))
        self.pixbright_sdr.setToolTip(_translate("optwndw", "how bright a pixel must be at minimum to be detected", None))
        self.pixbright_lbl.setText(_translate("optwndw", "0", None))
        self.cambright_lbl.setText(_translate("optwndw", "0", None))
        self.exposure_lbl.setText(_translate("optwndw", "0", None))
        self.label_7.setText(_translate("optwndw", "Webcam Exposure", None))
        self.gain_lbl.setText(_translate("optwndw", "0", None))
        self.label_12.setText(_translate("optwndw", "Webcam Gain", None))
        self.label_4.setText(_translate("optwndw", "Resolution", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("optwndw", "Camera", None))
        self.scanrev_lbl.setText(_translate("optwndw", "scans/rev", None))
        self.scansrev_sdr.setToolTip(_translate("optwndw", "how many scans per revolution should we take?", None))
        self.steps_lbl.setText(_translate("optwndw", "0", None))
        self.stepdelay_sdr.setToolTip(_translate("optwndw", "this is the delay between each step; make it as low as possible to increase scan speed, \n"
"but only as high as there are no scan errors because the cam needs time to settle", None))
        self.stepdelay_lbl.setText(_translate("optwndw", "stepdelay                    ms", None))
        self.delay_lbl.setText(_translate("optwndw", "0", None))
        self.dspinBox.setToolTip(_translate("optwndw", "lower border of scan area", None))
        self.rspinBox.setToolTip(_translate("optwndw", "right border of scan area", None))
        self.lspinBox.setToolTip(_translate("optwndw", "left border of scan area", None))
        self.uspinBox.setToolTip(_translate("optwndw", "upper border of scan area", None))
        self.label_5.setText(_translate("optwndw", "Borders", None))
        self.label_11.setText(_translate("optwndw", "[°]Cam>turntable", None))
        self.r_angleBox.setToolTip(_translate("optwndw", "this is the angle between the webcam and the right laser. (positive value)", None))
        self.cam_angleBox.setToolTip(_translate("optwndw", "this is the angle between the webcam and the turntable. (positive value)", None))
        self.label_6.setText(_translate("optwndw", "[°]Cam>right laser", None))
        self.label_10.setText(_translate("optwndw", "[°]Cam>left laser", None))
        self.l_angleBox.setToolTip(_translate("optwndw", "this is the angle between the webcam and the left laser. (positive value)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("optwndw", "Scan", None))
        self.connectBtn.setToolTip(_translate("optwndw", "connect", None))
        self.connectBtn.setText(_translate("optwndw", "Connect", None))
        self.connectBox.setToolTip(_translate("optwndw", "connect the comport at startup?", None))
        self.connectBox.setText(_translate("optwndw", "Auto Connect", None))
        self.label_9.setText(_translate("optwndw", "Baud", None))
        self.comBox.setToolTip(_translate("optwndw", "comports are scanned when you open the program; \n"
"if you changed the ports etc. you need a restart of the program to refresh the list.", None))
        self.label_8.setText(_translate("optwndw", "Com Port", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("optwndw", "Serial", None))
        self.folderlabel.setHtml(_translate("optwndw", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">default</span></p></body></html>", None))
        self.label_3.setText(_translate("optwndw", "Please select your working directory", None))
        self.aboutButton.setToolTip(_translate("optwndw", "about", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("optwndw", "System", None))

import resources_rc
