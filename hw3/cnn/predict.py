# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/27 22:40
# @Author  : 赵丹彪
# @File    : test.py
# @Email   : bertin2002@163.com
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from PIL import Image
import numpy as np
from train import CNN

class Predict(object):
    def __init__(self):
        latest = tf.train.latest_checkpoint('./model')
        self.cnn = CNN()
        # 恢复网络权重
        self.cnn.model.load_weights(latest)

    def predict(self, image_path):
        # 以黑白方式读取图片
        img = Image.open(image_path).convert('L')
        # 将图片转换为28*28的像素矩阵
        img = img.resize((28, 28), Image.ANTIALIAS)
        img_arr = np.array(img).reshape(1, 28, 28, 1)
        # 像素值映射到 0 - 1 之间
        img_arr = img_arr / 255.0
        # 预测
        result = self.cnn.model.predict(img_arr)
        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得最大值的下标，即代表的数字

        print('正确结果： ',image_path[-5], '预测结果：', np.argmax(result[0]))


if __name__ == "__main__":
    main = Predict()
    # 遍历文件夹
    for root, dirs, files in os.walk('../test_img'):
        for file in files:
            # print(file)
            main.predict('../test_img/'+file)