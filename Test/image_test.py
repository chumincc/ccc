import imutils
from skimage.measure import compare_ssim
import cv2
import numpy as np
import os

class MarkDiffImg:
    @staticmethod
    def cv_imread(file_path):
        """
        读取图片（解决路径中含有中文无法读取的问题），一般是直接cv2.imread(filea_path)
        :param file_path:图片的路径
        :return:
        """
        cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return cv_img

    # def mark_diff_img(self, result, basesnapshot_png, runningsnapshot_png, DiffSnapshot_Dir, casename, name):
    def mark_diff_img(self,  basesnapshot_png, runningsnapshot_png, DiffSnapshot_Dir, name):
        """
        对比图片并标出差异，保存差异图片
        :param basesnapshot_png:
        :param runningsnapshot_png:
        :param DiffSnapshot_Dir:
        :param casename:
        :param name:
        :return:
        """
        # 加载两张图片并将他们转换为灰度：
        image_a = self.cv_imread(basesnapshot_png)
        image_b = self.cv_imread(runningsnapshot_png)
        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

        # 计算两个灰度图像之间的结构相似度指数：
        (score, diff) = compare_ssim(gray_a, gray_b, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM:{}".format(score))

        # 找到不同点的轮廓以致于我们可以在被标识为“不同”的区域周围放置矩形：
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # 找到一系列区域，在区域周围放置矩形：
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image_a, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(image_b, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 基础快照标出与运行时快照的差异 图片
        diffsnapshot_png_a = DiffSnapshot_Dir + '/' + name + '_base.png'
        # 运行时快照标出与基础快照的差异 图片
        diffsnapshot_png_b = DiffSnapshot_Dir + '/' + name + '_running.png'
        # 保存差异图片
        cv2.imencode('.jpg', image_a)[1].tofile(diffsnapshot_png_a)
        cv2.imencode('.jpg', image_b)[1].tofile(diffsnapshot_png_b)
        # result["对比快照-基础快照路径"] = diffsnapshot_png_a
        # result["对比快照-运行时快照路径"] = diffsnapshot_png_b
        return score,diffsnapshot_png_a, diffsnapshot_png_b


if __name__ == '__main__':
    t = MarkDiffImg()
    path = os.path.dirname(__file__)
    print(path)
    snapshot_base = path + '/snapshot/4.jpg'
    snapshot_run = path + '/snapshot/5.jpg'
    DiffSnapshot_Dir = path + '/DiffSnapshot'
    name = 'diff'
    res = t.mark_diff_img(snapshot_base, snapshot_run, DiffSnapshot_Dir, name)
    print(res[0])
    if int(res[0]) == 1:
        print('same')
    else:
        print('diff')
