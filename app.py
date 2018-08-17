from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

import helloworld_ui


class HelloWorld(QDialog, helloworld_ui.Ui_helloworld):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


app = QApplication(sys.argv)
helloworld = HelloWorld()
helloworld.show()
app.exec_()