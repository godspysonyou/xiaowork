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
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 109, 1421, 741))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.graphicsView_MT = QtGui.QGraphicsView(self.tab)
        self.graphicsView_MT.setGeometry(QtCore.QRect(60, 10, 480, 340))
        self.graphicsView_MT.setObjectName(_fromUtf8("graphicsView_MT"))
        self.graphicsView_OEE = QtGui.QGraphicsView(self.tab)
        self.graphicsView_OEE.setGeometry(QtCore.QRect(550, 10, 480, 340))
        self.graphicsView_OEE.setObjectName(_fromUtf8("graphicsView_OEE"))
        self.graphicsView_Loss = QtGui.QGraphicsView(self.tab)
        self.graphicsView_Loss.setGeometry(QtCore.QRect(60, 360, 480, 340))
        self.graphicsView_Loss.setObjectName(_fromUtf8("graphicsView_Loss"))
        self.graphicsView_Pie = QtGui.QGraphicsView(self.tab)
        self.graphicsView_Pie.setGeometry(QtCore.QRect(550, 360, 480, 340))
        self.graphicsView_Pie.setObjectName(_fromUtf8("graphicsView_Pie"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(1040, 260, 360, 240))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(1040, 10, 360, 240))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(1040, 510, 361, 191))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 0, 1421, 20))
        self.line.setStyleSheet(_fromUtf8(""))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 1421, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "主界面", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "管理中心", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "月数据分析", None))

