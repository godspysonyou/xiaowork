from PyQt4 import QtGui, QtCore
import uifiles.xio_playvideo_ui as ui
import sys
import cv2
import threading
import time


class Timer(QtCore.QThread):
    def __init__(self, signal='updateTime()', sleep_time=0.04):
        super(Timer, self).__init__()
        self.signal = signal
        self.sleep_time = sleep_time

    def run(self):
        while True:
            self.emit(QtCore.SIGNAL(self.signal))
            time.sleep(self.sleep_time)


class XioPlayVideo(QtGui.QWidget):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super(XioPlayVideo, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.left_cam = cv2.VideoCapture('./videos/left_cam.mp4')  # left camara
        self.right_cam = cv2.VideoCapture('./videos/right_cam.mp4')
        self.frame_left = None
        self.frame_right = None

        self.thread_video_receive = threading.Thread(target=self.video_receive_local)
        self.thread_video_receive.start()
        self.thread_time = Timer('updatePlay()')
        self.connect(self.thread_time, QtCore.SIGNAL('updatePlay()'), self.video_play)
        self.thread_time.start()

    def video_receive_local(self, cam1='./videos/left_cam.mp4', cam2='./videos/right_cam.mp4', time_flag=True):
        if self.left_cam.isOpened() is False:
            self.left_cam = cv2.VideoCapture(cam1)
        if self.right_cam.isOpened() is False:
            self.right_cam = cv2.VideoCapture(cam2)
        ret_1, frame_1 = self.left_cam.read()
        ret_2, frame_2 = self.right_cam.read()
        while True:
            self.frame_left = frame_1
            self.frame_right = frame_2
            if ret_1 is False:
                self.left_cam = cv2.VideoCapture(cam1)
            if ret_2 is False:
                self.right_cam = cv2.VideoCapture(cam2)
            ret_1, frame_1 = self.left_cam.read()
            ret_1, frame_2 = self.right_cam.read()
            if time_flag is True:
                time.sleep(0.04)

    def video_receive_rstp(self, cam1='rstp:', cam2='rstp:'):
        self.video_receive_local(cam1=cam1, cam2=cam2, time_flag=False)

    def video_play(self):
        def label_show_left(frame, label=self.ui.label):
            height, width, _ = frame.shape
            frame_change = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resize = cv2.resize(frame_change, (500, 300), interpolation=cv2.INTER_AREA)
            image = QtGui.QImage(frame_resize.data, frame_resize.shape[1], frame_resize.shape[0],
                                 QtGui.QImage.Format_RGB888)
            label.setPixmap(QtGui.QPixmap.fromImage(image))

        def label_show_right(frame ,label=self.ui.label_2):
            label_show_left(frame,label)

        if self.frame_left is not None:
            label_show_left(self.frame_left)
        if self.frame_right is not None:
            label_show_right(self.frame_right)

    def monitoring(self):
        def label_show(frame):
            height, width, _ = frame.shape
            frame_change = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resize = cv2.resize(frame_change, (400, 300), interpolation=cv2.INTER_AREA)
            image = QtGui.QImage(frame_resize.data, frame_resize.shape[1], frame_resize.shape[0],
                                 QtGui.QImage.Format_RGB888)
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(image))

        ret_1, frame_1 = self.left_cam.read()
        while ret_1:
            label_show(frame_1)
            ret_1, frame_1 = self.left_cam.read()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioPlayVideo()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
