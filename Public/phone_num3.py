from tkinter import *
from tkinter import messagebox

root=Tk()

def com():
    try:
        float(e1.get())#获取e1的值，转为浮点数，如果不能转捕获异常
        l1.config(text=e1.get())
    except:
        messagebox.showwarning('警告','请输入数字')

e1=Entry(root)
e1.pack()

Button(root,text='获取',command=com).pack()

l1=Label(root,text='只能数字')
l1.pack()

mainloop()