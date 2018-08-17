from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import time

import css_ui


class Beautiful(QDialog, css_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        systray_icon = QIcon("cstrike.ico")
        systray = QSystemTrayIcon(systray_icon, self)

        menu = QMenu()
        restore = QAction("Restore", self)
        close = QAction("Close", self)
        menu.addActions([restore, close])
        systray.setContextMenu(menu)
        systray.show()

        systray.showMessage("Beautiful", "A sample Notification", QSystemTrayIcon.Warning)
        close.triggered.connect(self.close)

        self.progressBar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.progressBar.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, position):
            menu = QMenu(self)
            reset = QAction("Reset", self)
            menu.addAction(reset)
            reset.triggered.connect(self.progressBar.reset)
            menu.popup(self.progressBar.mapToGlobal(position))


app = QApplication(sys.argv)
dialog = Beautiful()

splash_image = QPixmap("friends.jpg")
splash = QSplashScreen(splash_image)
splash.show()
time.sleep(2)
dialog.show()
splash.finish(dialog)
app.exec_()