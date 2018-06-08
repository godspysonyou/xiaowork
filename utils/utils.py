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
    cut roi in a image
    :param filepath:
    :param loc:
    :return:
    '''
    image = cv2.imread(filepath, 1)
    l = image[loc[0]:loc[1], loc[2]:loc[3]]
    cv2.imwrite(filepath[0:-4] + '1.jpg', l)


if __name__ == '__main__':
    # show_image('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/447.jpg')
    img = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/447.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([-60, 20, 80])
    upper = np.array([80, 80, 250])
    mask = cv2.inRange(img, lower, upper)

    res = cv2.bitwise_and(img, img, mask=mask)

    #print(img[250,700])

    cv2.imshow('res', res)
    cv2.waitKey(0)
