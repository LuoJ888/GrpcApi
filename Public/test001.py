import sys

from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import QMessageBox

import ui_login

import main

class frmLogin(QtWidgets.QWidget, ui_login.Ui_frmLogin):

        def __init__(self):

            super(frmLogin, self).__init__()

            self.setupUi(self)

            self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #禁止最大化按钮

        # 创建槽函数 槽函数直接使用元件的名称：on_元件名称_信号名称(槽装饰器, 区分参数)

        @QtCore.pyqtSlot() #@QtCore.pyqtSlot(bool)

        def on_btnLogin_clicked(self): #自动对应click

            user = self.edtUser.text().strip()

            passwd = self.edtPasswd.text().strip()

        if user == "":

           QMessageBox.warning(self,"警告","用户号不能为空，请输入！")

        return

        if passwd == "":

           QMessageBox.warning(self,"警告","密码不能为空，请输入！")

        return

        if len(user) != 7:

            QMessageBox.warning(self,"警告","用户号长度必须为7位！")

        return

        if len(passwd) < 6:

           QMessageBox.warning(self,"警告","密码长度不能小于6位！")

        return

        if passwd != '123456':

           QMessageBox.warning(self,"警告","密码不符无法登陆!")

        return

        frmMain.show() #打开新窗口

        self.close() #关闭本窗口

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    frmLogin = frmLogin()

    frmMain = main.frmMain()

    frmLogin.show()

    sys.exit(app.exec_())