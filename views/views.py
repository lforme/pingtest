from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
import hashlib
from checkss import checkIPs


class CheckView():
    def __init__(self, init_window_name):
        self.path = tk.StringVar(init_window_name)
        self.init_window_name = init_window_name
        self.data_log_list = []
        self.ping_succeed_count = ""
        self.ping_failing_count = ""
        self.cost_time = ""

    def set_init_window_name(self):
        self.init_window_name.title("VPN测试工具 by:WHY")
        self.init_window_name.geometry('350x500+10+10')
        self.init_data_label = Label(self.init_window_name, text="服务器ip地址的路径")
        self.init_data_label.grid(row=0, column=0)
        self.init_entry = Entry(self.init_window_name, textvariable=self.path).grid(row=1, column=0)
        self.init_select_path = Button(self.init_window_name, text="路径选择", command=self.selectPath).grid(row=2, column=0)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=4, column=0, columnspan=10)
        self.test_button = Button(self.init_window_name, text="开始测试", command=self.ping_test).grid(row=3, column=0)

    def selectPath(self):
        filename = tk.filedialog.askopenfilename()
        if filename != '':
            self.path.set(filename)
        else:
            self.log_data_Text.insert(END, "你没有选取任何文件")


    def ping_test(self):

        str_path = self.path.get()
        my_tuple = checkIPs(str_path)
        self.cost_time = my_tuple[0]
        self.ping_succeed_count = my_tuple[1]
        self.ping_failing_count = my_tuple[2]
        self.data_log_list = my_tuple[3]

        result = map(lambda x: x + " 连接成功" + "\n", self.data_log_list)
        for item in result:
            self.log_data_Text.insert(END, item)




def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    check_view = CheckView(init_window)
    # 设置根窗口默认属性
    check_view.set_init_window_name()
    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
