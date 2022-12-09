# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 14:14
# @Author  : 赵丹彪
# @File    : train1.py
# @Email   : bertin2002@163.com
import os
from datetime import datetime

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models


# lenet-5
class CNN(object):
    def __init__(self):
        self.model = models.Sequential()
        # 第一个卷积层
        self.model.add(layers.Conv2D(32, (5, 5), activation='tanh',input_shape=(28, 28, 1)))
        # 第一个池化层
        self.model.add(layers.MaxPool2D((2, 2)))
        # 第二个卷积层
        self.model.add(layers.Conv2D(64, (5, 5), activation='tanh'))
        # 第二个池化层
        self.model.add(layers.MaxPool2D((2, 2)))
        # 全连接层
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(1024, activation='tanh'))
        # 输出层
        self.model.add(layers.Dense(10, activation='softmax'))

        # 编译模型
        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])
        # 打印模型结构
        self.model.summary()

    def train(self, x_train, y_train, x_test, y_test, epochs=5):
        logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
        # 训练模型
        self.model.fit(x_train, y_train, verbose=1, epochs=epochs, validation_data=(x_test, y_test),callbacks=[tensorboard_callback])
        # 保存模型
        if not os.path.exists('./model'):
            os.mkdir('./model')
        save_path = './model/cnn_mnist' + datetime.now().strftime("%m%d-%H%M") + '.h5'
        self.model.save(save_path)

    def evaluate(self, x_test, y_test):
        test_loss, test_acc = self.model.evaluate(x_test, y_test, verbose=2)
        print('test_loss: ', test_loss)
        print('test_acc: ', test_acc)


class main(object):
    def __init__(self):
        self.cnn = CNN()

    def load_mnint(self):
        # 加载数据集
        data_path = os.path.abspath(os.path.dirname(__file__)) + '/../data_set/mnist.npz'
        (x_train, y_train), (x_test, y_test) = datasets.mnist.load_data(path=data_path)
        # 将数据集转换为张量
        x_train, x_test = x_train / 255.0, x_test / 255.0
        x_train = x_train[..., tf.newaxis]
        x_test = x_test[..., tf.newaxis]
        return x_train, y_train, x_test, y_test

    def train(self, epochs=5):
        x_train, y_train, x_test, y_test = self.load_mnint()
        self.cnn.train(x_train, y_train, x_test, y_test, epochs)
        self.cnn.evaluate(x_test, y_test)


if __name__ == "__main__":
    main = main()
    x_train, y_train, x_test, y_test = main.load_mnint()
    main.train(epochs=5)
    print("训练完成")
