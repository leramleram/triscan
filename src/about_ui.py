# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\christian\Documents\GitHub\triscan\gui\about.ui'
#
# Created: Mon Mar 10 21:26:59 2014
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

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName(_fromUtf8("about"))
        about.resize(363, 153)
        self.buttonBox = QtGui.QDialogButtonBox(about)
        self.buttonBox.setGeometry(QtCore.QRect(300, 115, 46, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(about)
        self.label.setGeometry(QtCore.QRect(40, 25, 296, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(about)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), about.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), about.reject)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        about.setWindowTitle(_translate("about", "About Triscan", None))
        self.label.setText(_translate("about", "This is triscan, the free 3d scanning software, \n"
"written by Christian Rammelmüller in Python.\n"
"Version is very alpha, not everything is working yet.  \n"
"\n"
"Icons from  http://www.aha-soft.com\n"
"", None))

