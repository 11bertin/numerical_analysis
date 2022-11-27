# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/27 22:40
# @Author  : 赵丹彪
# @File    : test.py
# @Email   : bertin2002@163.com

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
        img = np.reshape(img, (28, 28, 1)) / 255.
        x = np.array([1 - img])

        y = self.cnn.model.predict(x)

        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得最大值的下标，即代表的数字
        print(image_path)
        print(y[0])
        print('        -> Predict digit', np.argmax(y[0]))


if __name__ == "__main__":
    app = Predict()
    app.predict('../test_img/1.png')
    app.predict('../test_img/2.png')
    app.predict('../test_img/3.png')