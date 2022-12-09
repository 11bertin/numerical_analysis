# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 21:02
# @Author  : 赵丹彪
# @File    : a.py
# @Email   : bertin2002@163.com
# 导入语音识别库和麦克风访问库
# 导入speech_recognition模块
import speech_recognition as sr

# 创建Recognizer实例
r = sr.Recognizer()

# 获取麦克风输入
with sr.Microphone() as source:
    print("请讲话：")
    audio = r.listen(source,timeout=5)
print('结束')
# 识别音频
try:
    print("您说的是：" + r.recognize_google(audio, language="zh-CN"))
except sr.UnknownValueError:
    print("无法识别您的语音")
except sr.RequestError as e:
    print("无法连接到服务器：{0}".format(e))
