import cv2
import numpy as np


def gamma_trans(img, gamma):
    '''
    将图像光照归一化
    :param img:
    :param gamma:
    :return:
    '''
    # 具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    # 实现映射用的是Opencv的查表函数
    return cv2.LUT(img, gamma_table)


def find_spark_left(img_gam, spark_roi):
    '''
    在固定区域检测火花
    :param img:
    :param spark_roi: 这个参数为一个不规则mask，二值图
    :return:
    '''
    hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

    # 火花颜色
    lower = np.array([0, 0, 250])
    upper = np.array([360, 10, 255])
    mask = cv2.inRange(hsv, lower, upper)
    # res_1 = cv2.bitwise_and(hsv,hsv,mask=mask) # hsv颜色选取火花颜色
    res = cv2.bitwise_and(mask, mask, mask=spark_roi)  # 在该区域检索
    num_res = res/255
    s = np.sum(num_res)
    print(s)
    if s > 1000:
        return True
    return False


def find_spark_right(img_gam, spark_roi):
    return find_spark_left(img_gam, spark_roi)


def classify(source_image, compare_image, threshold_1, threshold_2):
    '''
    比较两幅图的相似度
    :param source_image: 基图, 灰度图
    :param compare_image: 随时待比较的图，灰度图
    :param threshold_1: 阈值1, 划定相似点质量
    :param threshold_2: 阈值2， 达到质量的相似点个数
    :return:
    '''
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(source_image, None)
    kp2, des2 = orb.detectAndCompute(compare_image, None)

    if des2 is None:  # 待比较的图比较单一，没有特征，显然与基图不相似
        return False

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # 暴力匹配
    matches = bf.match(des1, des2)
    matches = list(filter(lambda x: x.distance < threshold_1, matches))  # 过滤不合格的相似点
    if len(matches) > threshold_2:
        return True
    else:
        return False


class Vision():
    def __init__(self):
        self.machine_back = cv2.imread('./images/machine_back.jpg', 0)  # 机器一般静止图，后向
        self.machine_forward = cv2.imread('./images/machine_forward.jpg', 0)
        self.mb_loc = (80, 470, 250, 590)  # 机器一般静止位置，后向，这里可以改成切片模式
        self.mf_loc = (180, 420, 600, 810)

        self.mask_left = cv2.imread('./images/mask_1.jpg', 0)
        self.mask_right = cv2.imread('./images/mask_2.jpg', 0)

    def find_spark(self, img):
        img_gam = gamma_trans(img, 0.75)  # 光照归一化
        return find_spark_left(img_gam, self.mask_left) or find_spark_right(img_gam, self.mask_right)

    def judge_machine_static(self, framegray):
        '''
        判断机器是否在一般静止位置
        :param framegray: 原始帧的灰度图
        :return:
        '''

        def judge_machine_back_similar(roi):  # 机器处于后向
            return classify(self.machine_back, roi, 50, 50)

        def judge_machine_forward_similar(roi):  # 机器处于前向
            return classify(self.machine_back, roi, 50, 50)

        mb_roi = framegray[self.mb_loc[0]:self.mb_loc[1], self.mb_loc[2]:self.mb_loc[3]]
        mf_roi = framegray[self.mf_loc[0]:self.mf_loc[1], self.mf_loc[2]:self.mf_loc[3]]
        mb_flag = judge_machine_back_similar(mb_roi)
        mf_flag = judge_machine_forward_similar(mf_roi)
        if mb_flag is True:
            print('机器处于后向')
        if mf_flag is True:
            print('机器处于前向')
        return mb_flag or mf_flag


if __name__ == '__main__':
    v = Vision()
    cap = cv2.VideoCapture('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/videos/left_cam.mp4')
    while (1):
        # Take each frame
        _, img = cap.read()

        print(v.find_spark(img))


