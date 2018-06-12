from PyQt4 import QtGui, QtCore
from PyQt4.QtNetwork import *
import uifiles.xio_shumei_ui as ui
import sys
import time

import socket


def client_connect(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # socket上下文管理
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'utf-8'))  # 向服务器发送信息
        response = str(sock.recv(1024), 'utf-8')
        print("Received: {}".format(response))


class XioShuMei(QtGui.QWidget):
    HOST = 'localhost'
    PORT = 8081

    def __init__(self):
        super(XioShuMei, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.type = "end"

    def keyPressEvent(self, QKeyEvent):
        def key_press_operation(action='打孔'):
            info_box = QtGui.QMessageBox()
            reply = info_box.question(self, 'Message', '确定' + action, info_box.Yes | info_box.No, info_box.No)
            if reply == info_box.Yes:
                client_connect(self.HOST, self.PORT, action)
            else:
                print('误触')
        if QKeyEvent.key() == QtCore.Qt.Key_1:  # 这里要设计逻辑避免工人误按
            key_press_operation('action1')

        elif QKeyEvent.key() == QtCore.Qt.Key_2:
            key_press_operation('action2')

        elif QKeyEvent.key() == QtCore.Qt.Key_3:
            key_press_operation('action3')

        elif QKeyEvent.key() == QtCore.Qt.Key_4:
            key_press_operation('action4')

        elif QKeyEvent.key() == QtCore.Qt.Key_5:
            key_press_operation('action5')

        elif QKeyEvent.key() == QtCore.Qt.Key_6:
            key_press_operation('action6')

        else:
            print('no key')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioShuMei()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
