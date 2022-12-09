# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/27 22:40
# @Author  : 赵丹彪
# @File    : test.py
# @Email   : bertin2002@163.com

import os
from datetime import datetime

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from tensorflow.keras import datasets, layers, models


class CNN(object):
    def __init__(self):
        model = models.Sequential()
        # 第1层卷积，卷积核大小为3*3，32个，28*28为待训练图片的大小
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        # 第2层卷积，卷积核大小为3*3，64个
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        # 第3层卷积，卷积核大小为3*3，64个
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        # 将卷积层的输出转换为一维向量
        model.add(layers.Flatten())
        # 全连接层，128个神经元
        model.add(layers.Dense(64, activation='relu'))
        # 全连接层，10个神经元，对应10个类别
        model.add(layers.Dense(10, activation='softmax'))
        # 编译模型
        model.summary()

        self.model = model

    def save(self, path):
        self.model.save(path)


class DataSource(object):
    def __init__(self):
        # mnist数据集存储的位置，如何不存在将自动下载
        data_path = os.path.abspath(os.path.dirname(__file__)) + '/../data_set/mnist.npz'
        (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data(path=data_path)
        # 6万张训练图片，1万张测试图片
        train_images = train_images.reshape((60000, 28, 28, 1))
        # # 只用到了训练集的前10000张图片
        # train_images = train_images[:10000]
        test_images = test_images.reshape((10000, 28, 28, 1))
        # 像素值映射到 0 - 1 之间
        train_images, test_images = train_images / 255.0, test_images / 255.0

        self.train_images, self.train_labels = train_images, train_labels
        self.test_images, self.test_labels = test_images, test_labels


class Train:
    def __init__(self):
        self.cnn = CNN()
        self.data = DataSource()

    def train(self, epochs=5):
        check_path = './model/cp-{epoch:04d}.ckpt'
        # period 每隔5epoch保存一次
        save_model_cb = tf.keras.callbacks.ModelCheckpoint(check_path, save_weights_only=True, verbose=0, period=5)

        self.cnn.model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                               loss='sparse_categorical_crossentropy',
                               metrics=['accuracy'])
        logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
        # 训练模型
        self.cnn.model.fit(self.data.train_images, self.data.train_labels, epochs=epochs,
                           validation_data=(self.data.test_images, self.data.test_labels),
                           verbose=1,
                           callbacks=[save_model_cb, tensorboard_callback])
        # 评估模型
        test_loss, test_acc = self.cnn.model.evaluate(self.data.test_images, self.data.test_labels)
        print("准确率: %.4f，共测试了%d张图片 " % (test_acc, len(self.data.test_labels)))


if __name__ == "__main__":
    app = Train()
    app.train(epochs=5)
    print("训练完成")