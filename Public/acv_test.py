import tkinter
import re
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

from xmindToExcel import XmindToXsl


# class Main:
#     def checkNameAndPwd(self, user, pwd):
#         """获取文本框中数据，并调用XmindToXsl类"""
#         user = self.username.get()
#         pwd = self.pwd1.get()
#         print(f"账号：{user}\n密码：{pwd}")
#         if user == '':
#             print('用户名不能为空')
#         if 2 <= len(user) < 8:
#             pass
#         else:
#             print('用户名长度仅可在2-7之间')
#         # if type(pwd) is not int:
#         #     print('密码类型只能是数字')
#         if 6 <= len(str(pwd)) < 10:
#             pass
#         else:
#             a = '密码长度仅可在6-9之间'
#             return a
#         try:
#             if pwd == '':
#                 a = '密码不能为空'
#                 return a
#         except Exception as e1:
#             return e1
#
#
# Main.checkNameAndPwd()


class MainUI(object):

    def __init__(self, geometrysize="350x250", geometry="+800+350"):
        self.top = tkinter.Tk()  # 生成主窗口
        self.top.title("Shopping App")  # 设置窗口的标题
        self.top.geometry(geometrysize)  # 设置窗口的大小
        self.top.geometry(geometry)  # 设置窗口出现的位置
        self.top.resizable(0, 0)  # 将窗口大小设置为不可变
        self.client_likes = tkinter.StringVar()  # 生成一个StringVar 对象，来保存下面输入框中的内容
        # self.pwd1 = tkinter.StringVar()

        # 调用自己写的create_widgets()方法
        self.create_widgets()

    def verf_typ(self):
        """密码类型验证"""
        pwd = self.client_likes.get()
        print(type(pwd))

        if type(pwd) is int:
            messagebox.showinfo(title='提示', message=f'输入字符类型正确')
        # finally:
        #     messagebox.showinfo(title='提示', message=f'输入字符类型错误')

        # if type(pwd) is not int:
        #     print('密码类型只能是数字')
        # if 6 <= len(str(pwd)) < 10:
        #     pass
        # else:
        #     a = '密码长度仅可在6-9之间'
        #     messagebox.showinfo(title='提示', message=f'请输入正确的账号+密码，谢谢！')
        #     print(a)
        # try:
        #     if pwd == '':
        #         print('密码不能为空')
        # except Exception as e1:
        #     print(f'{e1}')
        # regvalue = '.*\.xmind$'
        # xmind_reg = re.match(regvalue, user)
        # if xmind_reg:
        # # xmind转换成xls
        # xmind_to_xls = XmindToXsl(user)
        # xmind_to_xls.write_excel(performer=pwd)

    def select_path(self):
        """选择要转换成excel的xmind地址"""
        path_ = askopenfilename()
        self.client_likes.set(path_)

    def create_widgets(self):
        """创建窗口中的各种元素"""
        # 账号
        first_label = tkinter.Label(self.top, text='密码：')  # 生成一个标签
        first_label.place(x=-10, y=70, width=170, height=25)  # 设置输入框的大小，及在top窗口显示位置
        # first_label.grid(row=0, column=0)  # 使用grid布局，标签显示在第一行，第一列

        first_entry = tkinter.Entry(self.top, textvariable=self.client_likes)
        first_entry.index(6)  # 生成一个文本框，内容保存在上面变量中
        # first_entry.grid(row=0, column=1)  # 使用grid布局，文本框显示在第一行，第二列
        first_entry.place(x=90, y=70, width=170, height=25)

        # 登录按钮
        way_button = tkinter.Button(self.top, text="校验", command=self.verf_typ, bg='light blue')
        # command = self.select_path,
        # way_button.grid(row=0, column=2)  # 使用grid布局，按钮显示在第一行，第三列
        way_button.place(x=130, y=150, width=80, height=25)

        # 密码
        # second_label = tkinter.Label(self.top, text="密码：")
        # # second_label.grid(row=1, column=0)
        # second_label.place(x=-10, y=100, width=170, height=25)
        # second_entry = tkinter.Entry(self.top, textvariable=self.pwd1)
        # second_entry.place(x=90, y=100, width=170, height=25)

        # def on():
        #     second_entry["show"] = ""
        #     b1["state"] = "disable"
        #     b2["state"] = "normal"
        #
        # def off():
        #     second_entry["show"] = "*"
        #     b1["state"] = "normal"
        #     b2["state"] = "disable"

        # 显示密码按钮
        # b1 = tkinter.Button(self.top, text="显示密码", font=("kaiti", 13), state="disable", command=on, bg='light blue')
        # b1.place(x=130, y=150, width=80, height=25)
        # b1.pack()
        #
        # # 隐藏密码按钮
        # b2 = tkinter.Button(self.top, text="隐藏密码", font=("kaiti", 13), command=off, bg='light blue')
        # b2.place(x=130, y=200, width=80, height=25)
        # b2.pack()
        # second_entry.grid(row=1, column=1)

        # # 登录按钮
        # f_btn = tkinter.Frame(self.top, bg='red')  # 设置一个frame框架，并设置背景颜色为红色
        # f_btn.place(x=0, y=190, width=350, height=30)  # 设置框架的大小，及在top窗口显示位置
        # submit_button = tkinter.Button(f_btn, text="登录", command=self.get_value,
        #                                bg='light blue')  # 设置按钮的文字，调用方法，大小，颜色，显示框架
        # submit_button.grid(row=0, column=2)  # 使用grid布局，按钮显示在第一行，第一列
        # # submit_button.place(x=130, y=150, width=80, height=25)

        # 进入消息循环（必需组件）
        self.top.mainloop()

    # def showQuitDialog(self):
    #     qu = self.top.quit()
    #     return qu
    # showQuitDialog()


if __name__ == "__main__":
    mu = MainUI()
