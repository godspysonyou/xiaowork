from PyQt4 import QtCore
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np


class Timer(QtCore.QThread):
    '''这个类用来向主线程发射信号，通知其每隔一段时间运行一个槽函数
    Qt只允许主线程（也就是main函数在的那个线程）使用界面类，因为界面类不是线程安全的，不可重入，
    在多个线程中使用可能会出现问题，因此Qt不建议主界面线程外的线程使用图形类和调用图形类接口。
    否则有可能报错
    '''

    def __init__(self, signal='updateTime()', sleep_time=0.04):
        super(Timer, self).__init__()
        self.signal = signal
        self.sleep_time = sleep_time

    def run(self):
        while True:
            self.emit(QtCore.SIGNAL(self.signal))
            time.sleep(self.sleep_time)  # 休眠固定时间


def show_image(image):
    '''
    显示图像的像素坐标，便于截取兴趣区域
    :param image:
    :return:
    '''
    i = plt.imread(image)
    plt.imshow(i)
    plt.show()


def roi_cut(filepath='../images/50.jpg', loc=(5, 130, 980, 1090)):
    '''
    截取一个矩形兴趣区域
    :param filepath:
    :param loc:
    :return:
    '''
    image = cv2.imread(filepath, 1)
    l = image[loc[0]:loc[1], loc[2]:loc[3]]
    cv2.imwrite(filepath[0:-4] + '1.jpg', l)

def gamma_trans(img,gamma):
    #具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    #实现映射用的是Opencv的查表函数
    return cv2.LUT(img,gamma_table)


if __name__ == '__main__':
    # show_image('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/447.jpg')
    img = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/280.jpg')
    img_gam = gamma_trans(img,0.45)

    hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

    lower = np.array([55, 100, 200])
    upper = np.array([140, 180, 255])
    mask = cv2.inRange(img, lower, upper)

    res = cv2.bitwise_and(img_gam, img_gam, mask=mask)

    print(img[240, 660])
    print(img[420,750])


    show_image('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/447.jpg')
    # cv2.imshow('img',img)
    cv2.imshow('ga', img_gam)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.waitKey(0)
