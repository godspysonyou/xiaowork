# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xio_all.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1440, 856)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1030, 40, 360, 280))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1030, 330, 360, 280))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.graphicsView_OEE = QtGui.QGraphicsView(Form)
        self.graphicsView_OEE.setGeometry(QtCore.QRect(540, 70, 450, 340))
        self.graphicsView_OEE.setObjectName(_fromUtf8("graphicsView_OEE"))
        self.graphicsView_Pie = QtGui.QGraphicsView(Form)
        self.graphicsView_Pie.setGeometry(QtCore.QRect(540, 440, 450, 340))
        self.graphicsView_Pie.setObjectName(_fromUtf8("graphicsView_Pie"))
        self.graphicsView_MT = QtGui.QGraphicsView(Form)
        self.graphicsView_MT.setGeometry(QtCore.QRect(50, 70, 450, 340))
        self.graphicsView_MT.setObjectName(_fromUtf8("graphicsView_MT"))
        self.graphicsView_Loss = QtGui.QGraphicsView(Form)
        self.graphicsView_Loss.setGeometry(QtCore.QRect(50, 440, 450, 340))
        self.graphicsView_Loss.setObjectName(_fromUtf8("graphicsView_Loss"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(1030, 630, 361, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))

