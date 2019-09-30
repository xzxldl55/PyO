# -*- coding:utf-8 -*-

'''
图形第三方库：
Tk
wxWidgets
Qt
GTk

python自带支持Tk的Tkinter，无需进行安装
'''
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        # 每个元素都是一个Widgets，而Frame则是用来容纳Widgets的
        # 其中.pack()方法为将Widget添加到Frame中
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.alertButton = Button(self, text='Message', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo("Message", 'Hello, %s' % name)
# 实例化application
app = Application()
# 设置窗口标题
app.master.title('Hello, GUI')
# 主消息循环
app.mainloop()