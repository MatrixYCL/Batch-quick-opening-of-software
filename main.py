# -*- coding:utf-8 -*-
import time,os
import random
import pyautogui as gui
QQ_dir = r'D:\Software\Domestic\Tencent\QQ\Bin\QQ.exe'	        # QQ路径
Wechat = r'D:\Software\Domestic\Tencent\Wechat\WeChat.exe'      # 微信路径
BaowuPC = r'D:\Software\work_job\OA4.0\baowuPC.exe'             # 宝武OA路径
Chrome = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' # Chrome 路径

def Software_login():
    os.startfile(QQ_dir)        # 登录QQ
    time.sleep(random.randint(6,9))
    os.startfile(Wechat)
    time.sleep(random.randint(2,6))
    gui.hotkey('Enter')
    time.sleep(3)           # 随机时间 3 秒

    os.startfile(BaowuPC)
    time.sleep(random.randint(0,6))
    os.startfile(Chrome)

    print('正在打开QQ')
    print('正在打开Wechat')
    print('正在打开宝武OA')
    print('正在打开Chrome')

if __name__ == "__main__":
    Software_login()


