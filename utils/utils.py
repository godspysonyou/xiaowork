from PyQt4 import QtCore
import time


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
