from PyQt4 import QtGui, QtCore
import uifiles.xio_playvideo_ui as ui
import sys


class XioPlayVideo(QtGui.QWidget):
    def __init__(self):
        super(XioPlayVideo, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioPlayVideo()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())

