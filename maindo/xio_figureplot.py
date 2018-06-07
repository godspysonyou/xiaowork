from PyQt4 import QtGui, QtCore
import uifiles.xio_figureplot_ui as ui
import sys


class XioFigurePlot(QtGui.QWidget):
    def __init__(self):
        super(XioFigurePlot, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)

        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioFigurePlot()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
