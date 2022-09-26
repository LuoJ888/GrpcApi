import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel,QLineEdit
from PyQt5.QtGui import QPalette,QBrush,QPixmap
import pygame
pygame.mixer.init()
# import pymysql



class FirstUi(QMainWindow):
    """首先进入界面"""
    def __init__(self):
        super(FirstUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('登录首页')
        pygame.mixer.music.stop()
        #界面背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/登录首页背景.jpg")))
        self.setPalette(palette)

        # 左侧文字显示
        label_bj = 'border-width:2px;border-style:solid;font-size:15px;' \
                   'border-color:rgb(255,170,0);background-color:rgb(100,149,237);'
        label_kd = 250  # 文字框初始宽
        label_gd = 350  # 文字框初始高
        label_kkd = 120  # 文字框初始宽
        label_kgd = 30  # 文字框初始高

        self.label = QLabel(self)
        self.label.setText("用户名")
        self.label.move(label_kd, label_gd)
        self.label.setFixedSize(label_kkd, label_kgd)
        self.label.setStyleSheet(label_bj)

        self.label1 = QLabel(self)
        self.label1.setText("密 码")
        self.label1.move(label_kd, label_gd + 40)
        self.label1.setFixedSize(label_kkd, label_kgd)
        self.label1.setStyleSheet(label_bj)

        # 信息反馈
        self.label2 = QLabel(self)
        self.label2.setText("信息反馈")
        self.label2.move(label_kd, label_gd + 120)
        self.label2.setFixedSize(label_kkd + 230, label_kgd)
        self.label2.setStyleSheet(label_bj)

        # 按钮 发送邮件

        self.button = QPushButton(self)
        self.button.setText("注 册")
        self.button.move(label_kd, label_gd + 80)
        self.button.setFixedSize(label_kkd - 40, label_kgd)
        self.button.setStyleSheet(label_bj)

        self.button1 = QPushButton(self)
        self.button1.setText("登 录")
        self.button1.move(label_kd + 90, label_gd + 80)
        self.button1.setFixedSize(label_kkd - 40, label_kgd)
        self.button1.setStyleSheet(label_bj)

        self.button2 = QPushButton(self)
        self.button2.setText("忘记密码")
        self.button2.move(label_kd + 180, label_gd + 80)
        self.button2.setFixedSize(label_kkd - 40, label_kgd)
        self.button2.setStyleSheet(label_bj)

        self.button3 = QPushButton(self)
        self.button3.setText("修改密码")
        self.button3.move(label_kd + 270, label_gd + 80)
        self.button3.setFixedSize(label_kkd - 40, label_kgd)
        self.button3.setStyleSheet(label_bj)

        # 按键 注 册 点击触发
        self.button.clicked.connect(self.openimage_ze)
        # 按键 登 录 点击触发
        self.button1.clicked.connect(self.openimage_dl)
        # 按键忘记密码点击触发
        self.button2.clicked.connect(self.openimage_xg)
        # 按键忘记密码点击触发
        self.button3.clicked.connect(self.openimage_xgmm)


        lineEdit_kd = 380  # 文字框初始宽
        lineEdit_gd = 350  # 文字框初始高
        lineEdit_kkd = 220  # 文字框初始宽
        lineEdit_kgd = 30  # 文字框初始高
        # 右侧文字输入栏
        lineEdit_bj = 'border-width:2px;border-style:solid;font-size:15px;' \
                      'border-color:rgb(255,255,0);background-color:rgb(100,170,160);'

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText("zbjckm@163.com")
        self.lineEdit.move(lineEdit_kd, lineEdit_gd)
        self.lineEdit.setFixedSize(lineEdit_kkd - 10, lineEdit_kgd)
        self.lineEdit.setStyleSheet(lineEdit_bj)

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setText("szcNSP850219")
        self.lineEdit1.move(lineEdit_kd, lineEdit_gd + 40)
        self.lineEdit1.setFixedSize(lineEdit_kkd - 10, lineEdit_kgd)
        self.lineEdit1.setStyleSheet(lineEdit_bj)


    def slot_btn_functiona(self):
        self.hide()
        self.s = Jie_a_Ui()
        self.s.show()

    def slot_btn_functionb(self):
        self.hide()
        self.s = Jie_b_Ui()
        self.s.show()

    def sjk_lj(self):
        # 连接database 数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='szc', password='szcNSP850219', database='szc_sql',
                               charset='utf8')


    def openimage_ze(self):
        """注 册 按钮 """
        # 用户名
        self.user = self.lineEdit.text()
        # 密码
        self.password = self.lineEdit1.text()

        #登录数据库
        self.sjk_lj()
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()
        #查看用户名是否存在
        sql = "SELECT * FROM userinfo where username = '%s'" % self.user
        self.count = self.cursor.execute(sql)
        if self.count == 1:
            self.label2.setText(self.user+"：用户名已存在")
            return
        else:
            sql = "insert into userinfo (username,passwd,createdate,state,statedate) values('%s','%s',now(),'US10',now()) " % (
            self.user, self.password)
            self.count = self.cursor.execute(sql)
            self.conn.commit()
            self.label2.setText(self.user+"：恭喜您注册成功")

        # 关闭光标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()

    def openimage_dl(self):
        """登 录 按钮 """
        # 用户名
        self.user = self.lineEdit.text()
        # 密码
        self.password = self.lineEdit1.text()

        # 登录数据库
        self.sjk_lj()
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()
        # 查看用户名是否存在
        sql = "SELECT * FROM userinfo where username = '%s'" % self.user
        self.count = self.cursor.execute(sql)
        if self.count == 0:
            self.label2.setText(self.user + "：用户名不存在")
        else:
            sql = "SELECT passwd FROM userinfo where username = '%s'" % self.user
            self.cursor.execute(sql)
            self.sjk_mm = self.cursor.fetchone()[0]  # 获取密码
            if self.password == self.sjk_mm:
                self.slot_btn_functiona()
            else:
                self.label2.setText(self.user + "：您输入的密码不符")

        # 关闭光标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


    def openimage_xg(self):
        """忘记密码 按钮 """
        # 用户名
        self.user = self.lineEdit.text()
        # 密码
        self.password = self.lineEdit1.text()

        # 登录数据库
        self.sjk_lj()
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()
        # 查看用户名是否存在
        sql = "SELECT * FROM userinfo where username = '%s'" % self.user
        self.count = self.cursor.execute(sql)
        if self.count == 0:
            self.label2.setText(self.user + "：用户名不存在")
        else:
            sql = "SELECT passwd FROM userinfo where username = '%s'" % self.user
            self.cursor.execute(sql)
            self.sjk_mm = self.cursor.fetchone()[0]  # 获取密码
            self.label2.setText(self.user+" 您的密码:" +
                                self.sjk_mm[0:len(self.sjk_mm)-4] +'**' +
                                self.sjk_mm[len(self.sjk_mm)-2:len(self.sjk_mm)] )

        # 关闭光标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()

    def openimage_xgmm(self):
        """忘记密码 按钮 """
        self.slot_btn_functionb()


class Jie_a_Ui(QWidget):
    """二层界面"""
    def __init__(self):
        super(Jie_a_Ui, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('登录界面')
        # 界面背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/登录背景.jpg")))
        self.setPalette(palette)
        #背景音乐
        pygame.mixer.music.load('./images/爱笑的眼睛.MP3')
        pygame.mixer.music.play()

        self.btn = QPushButton('退回首页', self)
        self.btn.setGeometry(50, 500, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        self.hide()
        self.f = FirstUi()
        self.f.show()

class Jie_b_Ui(QWidget):
    """二层界面"""
    def __init__(self):
        super(Jie_b_Ui, self).__init__()
        self.init_ui()
        # 界面背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/修改密码.jpg")))
        self.setPalette(palette)
        # 背景音乐
        pygame.mixer.music.load('./images/修炼爱情.MP3')
        pygame.mixer.music.play()

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('修改密码')

        label_bj = 'border-width:2px;border-style:solid;font-size:15px;' \
                   'border-color:rgb(255,170,0);background-color:rgb(100,149,237);'
        label_kd = 250  # 文字框初始宽
        label_gd = 350  # 文字框初始高
        label_kkd = 120  # 文字框初始宽
        label_kgd = 30  # 文字框初始高

        self.label = QLabel(self)
        self.label.setText("用户名")
        self.label.move(label_kd, label_gd)
        self.label.setFixedSize(label_kkd, label_kgd)
        self.label.setStyleSheet(label_bj)

        self.label1 = QLabel(self)
        self.label1.setText("密 码")
        self.label1.move(label_kd, label_gd + 40)
        self.label1.setFixedSize(label_kkd, label_kgd)
        self.label1.setStyleSheet(label_bj)

        # 信息反馈
        self.label2 = QLabel(self)
        self.label2.setText("新密码")
        self.label2.move(label_kd, label_gd + 80)
        self.label2.setFixedSize(label_kkd , label_kgd)
        self.label2.setStyleSheet(label_bj)

        # 信息反馈
        self.label3 = QLabel(self)
        self.label3.setText("信息反馈")
        self.label3.move(label_kd, label_gd + 160)
        self.label3.setFixedSize(label_kkd + 230, label_kgd)
        self.label3.setStyleSheet(label_bj)

        # 右侧文字输入栏
        lineEdit_bj = 'border-width:2px;border-style:solid;font-size:15px;' \
                      'border-color:rgb(255,255,0);background-color:rgb(100,170,160);'
        lineEdit_kd = 380  # 文字框初始宽
        lineEdit_gd = 350  # 文字框初始高
        lineEdit_kkd = 220  # 文字框初始宽
        lineEdit_kgd = 30  # 文字框初始高

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText("zbjckm@163.com")
        self.lineEdit.move(lineEdit_kd, lineEdit_gd)
        self.lineEdit.setFixedSize(lineEdit_kkd - 10, lineEdit_kgd)
        self.lineEdit.setStyleSheet(lineEdit_bj)

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setText("szcNSP850219")
        self.lineEdit1.move(lineEdit_kd, lineEdit_gd + 40)
        self.lineEdit1.setFixedSize(lineEdit_kkd - 10, lineEdit_kgd)
        self.lineEdit1.setStyleSheet(lineEdit_bj)

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setText("新密码输入框")
        self.lineEdit2.move(lineEdit_kd, lineEdit_gd + 80)
        self.lineEdit2.setFixedSize(lineEdit_kkd - 10, lineEdit_kgd)
        self.lineEdit2.setStyleSheet(lineEdit_bj)

        self.button2 = QPushButton(self)
        self.button2.setText("修改密码")
        self.button2.move(label_kd , label_gd + 120)
        self.button2.setFixedSize(label_kkd +50, label_kgd)
        self.button2.setStyleSheet(label_bj)

        # 按键修改密码点击触发
        self.button2.clicked.connect(self.openimage_xg)

        self.button3 = QPushButton(self)
        self.button3.setText("退回首页")
        self.button3.move(label_kd +180, label_gd + 120)
        self.button3.setFixedSize(label_kkd +50, label_kgd)
        self.button3.setStyleSheet(label_bj)

        # 按键修改密码点击触发
        self.button3.clicked.connect(self.slot_btn_function)


    def sjk_lj(self):
        # 连接database 数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='szc', password='szcNSP850219', database='szc_sql',
                               charset='utf8')

    def openimage_xg(self):
        """修改密码 按钮 """
        # 用户名
        self.user = self.lineEdit.text()
        # 密码
        self.password = self.lineEdit1.text()

        # 登录数据库
        self.sjk_lj()
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()
        self.password_new = self.lineEdit2.text()

        # 查看用户名是否存在
        sql = "SELECT * FROM userinfo where username = '%s'" % self.user
        self.count = self.cursor.execute(sql)
        if self.count == 0:
            self.label3.setText(self.user + "：用户名不存在")
        else:
            sql = "SELECT passwd FROM userinfo where username = '%s'" % self.user
            self.cursor.execute(sql)
            self.sjk_mm = self.cursor.fetchone()[0]  # 获取密码
            if self.password == self.sjk_mm:

                sql = "update userinfo set passwd='%s' where username ='%s' " % (self.password_new, self.user)
                self.count = self.cursor.execute(sql)
                self.conn.commit()
                self.label3.setText(self.user + "：您的密码已修改")
            else:
                self.label3.setText(self.user + "：您输入的密码不符")

        # 关闭光标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


    def slot_btn_function(self):
        self.hide()
        self.f = FirstUi()
        self.f.show()



def main():
    #主界面打开函数
    app = QApplication(sys.argv)
    w = FirstUi()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()