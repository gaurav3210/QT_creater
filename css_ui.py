# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'css.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QLineEdit{\n"
"padding: 6px 12px;\n"
"font-size:14px;\n"
"color:#555;\n"
"background-color:#fff;\n"
"border:1px solid #ccc;\n"
"border-radius:4px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border-color:#66afe9;\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(250, 250, 250,90), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom: 1px solid darkgrey;\n"
"}\n"
"\n"
"QToolButton{\n"
"background-color:transparent;\n"
"border: none;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
"background-color: rgb(193,210,238);\n"
"border: 1px solid rgb(60,127,177);\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(224,232,246);\n"
"}\n"
"QToolButton::checked:hover{\n"
"background-color:rgb(193,210,238);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.facebook = QtWidgets.QToolButton(self.frame)
        self.facebook.setGeometry(QtCore.QRect(20, 20, 71, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebook.setIcon(icon)
        self.facebook.setIconSize(QtCore.QSize(32, 32))
        self.facebook.setCheckable(True)
        self.facebook.setAutoExclusive(True)
        self.facebook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.facebook.setObjectName("facebook")
        self.twitter = QtWidgets.QToolButton(self.frame)
        self.twitter.setGeometry(QtCore.QRect(140, 20, 71, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter.setIcon(icon1)
        self.twitter.setIconSize(QtCore.QSize(32, 32))
        self.twitter.setCheckable(True)
        self.twitter.setAutoExclusive(True)
        self.twitter.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.twitter.setObjectName("twitter")
        self.googleplus = QtWidgets.QToolButton(self.frame)
        self.googleplus.setGeometry(QtCore.QRect(260, 20, 71, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/googleplus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.googleplus.setIcon(icon2)
        self.googleplus.setIconSize(QtCore.QSize(32, 32))
        self.googleplus.setCheckable(True)
        self.googleplus.setAutoExclusive(True)
        self.googleplus.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.googleplus.setObjectName("googleplus")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 160, 141, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(130, 200, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"border:2px solidgrey;\n"
"border-radius:4px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar:chunk\n"
"{\n"
"background-color:#3366ff;\n"
"width:10px;\n"
"margin:1px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"font-size:14px;\n"
"border:1px solid transparent;\n"
"border-radius:4px;\n"
"color:#fff;\n"
"background-color: #428bca;\n"
"border-color: 3357ebd;\n"
"}\n"
"QProgressBar\n"
"{\n"
"color: #fff;\n"
"background-color:#3071a9;\n"
"border-color:#285e8e;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.facebook.setText(_translate("Dialog", "facebook"))
        self.twitter.setText(_translate("Dialog", "Twitter"))
        self.googleplus.setText(_translate("Dialog", "Google+"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Log In"))
