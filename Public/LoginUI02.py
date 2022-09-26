import tkinter as tk

window = tk.Tk()
window.title("Login:你个鸡儿")

l1 = tk.Label(window, text="用户名：", font=("kaiti", 20))
l1.pack()

e1 = tk.Entry(window, font=("kaiti", 20))
e1.pack()

l2 = tk.Label(window, text="密码：", font=("kaiti", 20))
l2.pack()

e2 = tk.Entry(window, font=("kaiti", 20), show="*")
e2.place(width=50, height=50)
e2.pack()


def on():
    e2["show"] = ""
    b1["state"] = "disable"
    b2["state"] = "normal"


def off():
    e2["show"] = "*"
    b1["state"] = "normal"
    b2["state"] = "disable"


b1 = tk.Button(window, text="显示密码", font=("kaiti", 20), command=on)
b1.pack()

b2 = tk.Button(window, text="隐藏密码", font=("kaiti", 20), state="disable", command=off)
b2.pack()

window.mainloop()
