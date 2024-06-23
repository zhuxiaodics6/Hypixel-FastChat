import keyboard
import time
import tkinter as tk
from tkinter import *
import sys
import json

class key():
    def __init__(self, key_data:dict):
        self.key_li = list(key_data.keys())
        self.text_li = list(key_data.values())
        self.text_fk = ['f k','son of b','shut up']
        self.flag = False
        key.hotkey(self)
        key.fkloopkey(self)
        key.funckey(self)

    def listener(self, i):
        if self.flag:
            keyboard.release('ctrl,t,shift,alt,n')
            time.sleep(0.1)
            keyboard.press_and_release('t')
            time.sleep(0.1)
            keyboard.write(self.text_li[i])
            keyboard.press_and_release('enter')
            time.sleep(0.1)
            keyboard.press_and_release('q')
            keyboard.press_and_release('alt')
            MainWindow.refresh_data(self.text_li[i])

    def hotkey(self):
        for i in range(len(self.key_li)):
            keyboard.add_hotkey(self.key_li[i], key.listener, args=(self,i))

    def fkloop(self):
        for text in self.text_fk:
            keyboard.press_and_release('t')
            time.sleep(0.1)
            keyboard.write(text)
            keyboard.press_and_release('enter')
            time.sleep(0.1)
            keyboard.press_and_release('q')
            MainWindow.refresh_data(text)
            time.sleep(0.1)

    def fkloopkey(self):
        keyboard.add_hotkey('ctrl+alt+shift', key.fkloop, args=(self,))

    def func(self, mode):
        if self.flag or mode:
            self.flag = False
            MainWindow.refresh_data('已关闭')
            keyboard.release('ctrl,t')
            time.sleep(0.1)
            if not mode:
                keyboard.press_and_release('enter')
        else:
            self.flag = True
            MainWindow.refresh_data('已开启')
            keyboard.release('ctrl,t')
            time.sleep(0.1)
            keyboard.press_and_release('enter')

    def funckey(self):
        keyboard.add_hotkey('ctrl+t', key.func, args=(self,0))
        #keyboard.add_hotkey('t', key.func, args=(self,1))


class data():
    def __init__(self):
        self.path = sys.argv[1]

    def load(self):
        f = open(self.path, 'r')
        content = f.read()
        data_json = json.loads(content)
        return data_json
    
    def make(self, data_json):
        key_data = {}
        for x in data_json["key_list"]:
            key_data[x["hotkey"]] = x["text"]
        return key_data
    
class MainWindow(tk.Tk):
    def __init__(self):
        self.top = Tk()
        self.top.geometry("200x250")
        self.lbl = Label(self.top,text = "快捷聊天记录")
        self.top.resizable(False, False)
        self.listbox = Listbox(self.top)
        self.lbl.pack()
        self.listbox.pack()
        self.i = 1

    def refresh_data(self,text):
        y=time.strftime(r"%H:%M:%S--", time.localtime(time.time()))
        self.listbox.insert(self.i,y+text)
        self.i+=1
        self.listbox.update()

    def ml(self):
        self.top.mainloop()

d = data()
key_data = d.make(d.load())
MainWindow = MainWindow()
k = key(key_data)
MainWindow.ml()