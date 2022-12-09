# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/27 22:40
# @Author  : 赵丹彪
# @File    : test.py
# @Email   : bertin2002@163.com
# 导入包
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from train import CNN

model = CNN()
latest = tf.train.latest_checkpoint('./model')
# 2. 读取模型
model.model.load_weights(latest)
# 3. 保存为h5文件
model.save('./model/cp2model.h5')
