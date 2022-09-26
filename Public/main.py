from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import Qt

import ui_main


class frmMain(QtWidgets.QMainWindow, ui_main.Ui_frmMain):

    def __init__(self):

        super(frmMain, self).__init__()

        self.setupUi(self)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '提示信息', "您是否退出程序?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:

            event.accept()

        else:

            event.ignore()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
