import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


class Figure_Origin():
    '''这个类是绘图父类
    '''

    def __init__(self):
        self.figure = plt.figure(figsize=(6.5, 4), facecolor='lightgoldenrodyellow')  # 等下继承一个父类
        self.canvas = FigureCanvas(self.figure)

    def plot(self, *args, **kwargs):
        pass


class Figure_MT(Figure_Origin):
    '''这个类是绘制耗材图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_MT, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_mt():
            pass

        pass


class Figure_OEE(Figure_Origin):
    '''这个类是绘制OEE日推图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_OEE, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_oee():
            pass

        pass


class Figure_Loss(Figure_Origin):
    '''这个类是绘制损失占比图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_Loss, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_loss():
            pass

        pass


class Figure_Pie(Figure_Origin):
    '''这个类是绘制饼图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_Pie, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_pie():
            ax = self.figure.add_subplot(111)
            labels = 'e1', 'e2', 'e3', 'e4'
            sizes = args
            explode = (0, 0.1, 0, 0)  # 第一个异常在饼图冲凸显，凸显度为0.1
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True,
                   startangle=90)
            ax.axis('equal')
            #plt.show()
            self.canvas.draw()

        plot_pie()


if __name__ == "__main__":
    p = Figure_Pie()
    p.plot(1, 1, 1, 1)
