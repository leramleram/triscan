# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\christian\Documents\GitHub\triscan\gui\dlg.ui'
#
# Created: Mon Mar 10 21:26:56 2014
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

class Ui_dlg(object):
    def setupUi(self, dlg):
        dlg.setObjectName(_fromUtf8("dlg"))
        dlg.resize(289, 135)
        self.btnBox_dlg = QtGui.QDialogButtonBox(dlg)
        self.btnBox_dlg.setGeometry(QtCore.QRect(140, 90, 126, 32))
        self.btnBox_dlg.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox_dlg.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox_dlg.setObjectName(_fromUtf8("btnBox_dlg"))
        self.label_dlg = QtGui.QLabel(dlg)
        self.label_dlg.setGeometry(QtCore.QRect(10, 10, 271, 61))
        self.label_dlg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dlg.setWordWrap(True)
        self.label_dlg.setObjectName(_fromUtf8("label_dlg"))
        self.pushButton = QtGui.QPushButton(dlg)
        self.pushButton.setGeometry(QtCore.QRect(20, 75, 61, 51))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/48x48/png/48x48/Warning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(dlg)
        QtCore.QObject.connect(self.btnBox_dlg, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg.accept)
        QtCore.QObject.connect(self.btnBox_dlg, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg)

    def retranslateUi(self, dlg):
        dlg.setWindowTitle(_translate("dlg", "Warning! Δ▲", None))
        self.label_dlg.setText(_translate("dlg", "TextLabel", None))

import resources_rc
