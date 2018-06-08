from PyQt4 import QtGui, QtCore
from PyQt4.QtNetwork import *
import uifiles.xio_shumei_ui as ui
import sys

import socket


def client_connect(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # socket上下文管理
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'utf-8')) # 向服务器发送信息
        response = str(sock.recv(1024), 'utf-8')
        print("Received: {}".format(response))


class XioShuMei(QtGui.QWidget):
    HOST = '192.168.2.125'
    PORT = 8081

    def __init__(self):
        super(XioShuMei, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_1: # 这里要设计逻辑避免工人误按
            client_connect(self.HOST, self.PORT, '1')

        elif QKeyEvent.key() == QtCore.Qt.Key_2:
            client_connect(self.HOST, self.PORT, '2')

        elif QKeyEvent.key() == QtCore.Qt.Key_3:
            client_connect(self.HOST, self.PORT, '3')

        elif QKeyEvent.key() == QtCore.Qt.Key_4:
            client_connect(self.HOST, self.PORT, '4')

        elif QKeyEvent.key() == QtCore.Qt.Key_5:
            client_connect(self.HOST, self.PORT, '5')

        elif QKeyEvent.key() == QtCore.Qt.Key_0:
            client_connect(self.HOST, self.PORT, '0')

        else:
            print('no key')





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioShuMei()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
