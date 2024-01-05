import tkinter as tk
from tkinter import messagebox


def me():
    msg = e.get()
    messagebox.showinfo('', f'你的年龄为{msg}岁')


# 初始化窗口
root = tk.Tk()
root.title('年龄计算器')  # 标题
root.geometry('400x200')  # 窗口大小

lb = tk.Label(root, text='请输入你的年龄', font=('Arial', 12), height='2')
# pack ==> 显示
lb.place(relx=0.3, y=5, width=200)

e = tk.Entry(root, width=100)
e.place(relx=0.3, y=50, width=200)

b = tk.Button(root, text='点击', height='2', command=me)
b.place(relx=0.3, y=100, width=200)

root.mainloop()
