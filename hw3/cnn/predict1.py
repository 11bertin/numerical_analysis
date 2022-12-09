# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 14:34
# @Author  : 赵丹彪
# @File    : predict1.py
# @Email   : bertin2002@163.com
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from PIL import Image
import numpy as np


class Predict(object):
    def __init__(self):
        self.cnn = tf.keras.models.load_model('./model/cnn_mnist1205-1054.h5')
    def predict(self, image_path):
        # 以黑白方式读取图片
        img = Image.open(image_path).convert('L')
        # 将图片转换为28*28的像素矩阵
        img = img.resize((28, 28), Image.ANTIALIAS)
        img_arr = np.array(img).reshape(1, 28, 28, 1)
        # 像素值映射到 0 - 1 之间
        img_arr = img_arr / 255.0
        # 预测
        result = self.cnn.predict(img_arr)

        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得最大值的下标，即代表的数字

        print('正确结果： ', image_path[-5], '预测结果：', np.argmax(result[0]))


if __name__ == "__main__":
    main = Predict()
    # 遍历文件夹
    for root, dirs, files in os.walk('../test_img'):
        for file in files:
            # print(file)
            main.predict('../test_img/' + file)
