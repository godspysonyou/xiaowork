from PyQt4 import QtGui, QtCore
import uifiles.xio_all_ui as ui
import sys
import cv2
import threading
import time
from utils.utils import Timer, MyQueue
from utils.vision import Vision
import socketserver
import time
from figure.figure_plot import *


def data_deal(func):  # 要接受参数就要改成三层装饰器
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
    @data_deal
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        print(data)
        if data == '1':
            pass
        elif data == '2':
            pass
        elif data == '3':
            pass
        elif data == '4':
            pass
        elif data == '5':
            pass
        elif data == '0':
            pass


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class XioAll(QtGui.QWidget):
    '''这个类为主程序类
    '''
    HOST = 'localhost'
    PORT = 8081
    TOTAL = 0

    def __init__(self):
        super(XioAll, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)

        self.frame_left = None
        self.frame_right = None
        self.isWork = True
        self.q = MyQueue()  # 存放帧队列
        self.vision = Vision()

        self.thread_figure = Timer('updatePlay()', sleep_time=120)  # 该线程用来每隔2分钟刷新绘图区
        self.connect(self.thread_figure, QtCore.SIGNAL('updatePlay()'), self.draw)
        self.thread_figure.start()

        self.server = ThreadedTCPServer((self.HOST, self.PORT), ThreadedTCPRequestHandler)  # 该线程用来一直监听客户端的请求
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

        self.thread_video_receive = threading.Thread(target=self.video_receive_local)  # 该线程用来读取视频流
        self.thread_video_receive.start()

        self.thread_time = Timer('updatePlay()')  # 该线程用来每隔0.04秒在label上绘图
        self.connect(self.thread_time, QtCore.SIGNAL('updatePlay()'), self.video_play)
        self.thread_time.start()

        self.thread_recog = Timer('updatePlay()', sleep_time=1)  # 该线程用来每隔一秒分析图像
        self.connect(self.thread_recog, QtCore.SIGNAL('updatePlay()'), self.video_recog)
        self.thread_recog.start()

        self.thread_data = Timer('updatePlay()', sleep_time=1800)  # 该线程用来每隔半小时向数据库读取数据
        self.connect(self.thread_data, QtCore.SIGNAL('updatePlay()'), self.data_read)
        self.thread_data.start()

    def video_receive_local(self, cam1='./videos/left_cam.mp4', cam2='./videos/right_cam.mp4', time_flag=True):
        '''该方法用来接收本地视频
        :param cam1: 左摄像头数据源
        :param cam2: 右摄像头数据源
        :param time_flag: 是否休眠，本地视频为True
        :return: None
        '''
        self.left_cam = cv2.VideoCapture(cam1)
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
        '''该方法用来接收网络视频
        :param cam1: 左摄像头数据源
        :param cam2: 右摄像头数据源
        :return: None
        '''
        self.video_receive_local(cam1=cam1, cam2=cam2, time_flag=False)

    def video_play(self):
        '''该方法用来播放视频
        :return: None
        '''

        def label_show_left(frame, label=self.ui.label):  # 左控件label播放
            height, width, _ = frame.shape
            frame_change = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resize = cv2.resize(frame_change, (500, 300), interpolation=cv2.INTER_AREA)
            image = QtGui.QImage(frame_resize.data, frame_resize.shape[1], frame_resize.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 处理成QImage
            label.setPixmap(QtGui.QPixmap.fromImage(image))

        def label_show_right(frame, label=self.ui.label_2):  # 右空间Lable播放
            label_show_left(frame, label)

        if self.frame_left is not None:
            label_show_left(self.frame_left)
        if self.frame_right is not None:
            label_show_right(self.frame_right)

    def draw(self):
        '''
        展示图标
        :return:
        '''

        def draw_fp():  # 绘制损失饼图
            fp = Figure_Pie()
            fp.plot(*(1, 1, 1, 1))  # '*'有一个解包的功能，将（1，1，1，1）解包为 1 1 1 1
            graphicscene_fp = QtGui.QGraphicsScene()
            graphicscene_fp.addWidget(fp.canvas)
            self.ui.graphicsView_Pie.setScene(graphicscene_fp)
            self.ui.graphicsView_Pie.show()

        def draw_oee():  # 绘制oee日推图
            oee = Figure_OEE()
            oee.plot()  # 参数
            graphicscene_oee = QtGui.QGraphicsScene()
            graphicscene_oee.addWidget(oee.canvas)
            self.ui.graphicsView_OEE.setScene(graphicscene_oee)
            self.ui.graphicsView_OEE.show()

        def draw_loss():  # 绘制损失直方图
            loss = Figure_Loss()
            loss.plot()
            graphicscene_loss = QtGui.QGraphicsScene()
            graphicscene_loss.addWidget(loss.canvas)
            self.ui.graphicsView_Loss.setScene(graphicscene_loss)
            self.ui.graphicsView_Loss.show()

        def draw_mt():  # 绘制耗材使用图
            mt = Figure_MT()
            mt.plot()
            graphicscene_mt = QtGui.QGraphicsScene()
            graphicscene_mt.addWidget(mt.canvas)
            self.ui.graphicsView_MT.setScene(graphicscene_mt)
            self.ui.graphicsView_MT.show()

        draw_fp()
        draw_loss()
        draw_mt()
        draw_oee()

    def video_recog(self):
        self.TOTAL += 1

        def video_recog_left():
            '''
            做摄像头识别
            :return:
            '''
            has_spark = False

            if not self.q.is_full():  # 续满,先这样，可能要写入读图像中
                if self.frame_left is not None:
                    self.q.enqueue(self.frame_left)

            else:
                self.q.dequeue()
                if self.frame_left is not None:
                    self.q.enqueue(self.frame_left)

                for frame in self.q.queue:
                    # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    if self.vision.find_spark(frame):
                        has_spark = True
                        break
                if has_spark:
                    # print('工作')
                    pass
                else:
                    print('静止了，往catch文件夹中查看原因')
                    t = time.localtime()
                    hour = t[3]
                    mini = t[4]
                    seco = t[5]
                    filename = str(hour) + '-' + str(mini) + '-' + str(seco)
                    if self.TOTAL % 60 == 0:
                        cv2.imwrite('./catch/' + filename + '.jpg', frame)

            pass

        def video_recog_right():
            pass

        video_recog_left()

    def data_read(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioAll()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
