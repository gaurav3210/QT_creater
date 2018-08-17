# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_helloworld(object):
    def setupUi(self, helloworld):
        helloworld.setObjectName("helloworld")
        helloworld.resize(151, 149)
        helloworld.setSizeGripEnabled(False)
        helloworld.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(helloworld)
        self.verticalLayout.setObjectName("verticalLayout")
        self.url = QtWidgets.QLineEdit(helloworld)
        self.url.setObjectName("url")
        self.verticalLayout.addWidget(self.url)
        self.save_location = QtWidgets.QLineEdit(helloworld)
        self.save_location.setObjectName("save_location")
        self.verticalLayout.addWidget(self.save_location)
        self.browse = QtWidgets.QPushButton(helloworld)
        self.browse.setObjectName("browse")
        self.verticalLayout.addWidget(self.browse)
        self.progress = QtWidgets.QProgressBar(helloworld)
        self.progress.setProperty("value", 0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)
        self.download = QtWidgets.QPushButton(helloworld)
        self.download.setObjectName("download")
        self.verticalLayout.addWidget(self.download)

        self.retranslateUi(helloworld)
        QtCore.QMetaObject.connectSlotsByName(helloworld)

    def retranslateUi(self, helloworld):
        _translate = QtCore.QCoreApplication.translate
        helloworld.setWindowTitle(_translate("helloworld", "QDesigner"))
        self.url.setPlaceholderText(_translate("helloworld", "URL"))
        self.save_location.setPlaceholderText(_translate("helloworld", "File Save Location"))
        self.browse.setText(_translate("helloworld", "Browse"))
        self.download.setText(_translate("helloworld", "Download"))

