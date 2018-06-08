from PyQt4 import QtGui, QtCore
import uifiles.xio_figureplot_ui as ui
import sys
import threading
from utils.utils import Timer
from figure.figure_plot import Figure_Pie


class XioFigurePlot(QtGui.QWidget):
    '''这个类为绘制类
    '''
    def __init__(self):
        super(XioFigurePlot, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)

        self.thread_figure = Timer('updatePlay()', sleep_time=10)
        self.connect(self.thread_figure, QtCore.SIGNAL('updatePlay()'), self.draw)
        self.thread_figure.start()

    def draw(self):
        def draw_fp(): # 绘制损失饼图
            fp = Figure_Pie()
            fp.plot(*(1, 1, 1, 1)) # '*'有一个解包的功能，将（1，1，1，1）解包为 1 1 1 1
            graphicscene_fp = QtGui.QGraphicsScene()
            graphicscene_fp.addWidget(fp.canvas)
            self.ui.graphicsView_Pie.setScene(graphicscene_fp)
            self.ui.graphicsView_Pie.show()

        def draw_oee(): # 绘制oee日推图
            pass

        def draw_loss(): # 绘制损失直方图
            pass

        def draw_mt(): # 绘制耗材使用图
            pass

        draw_fp()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioFigurePlot()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
