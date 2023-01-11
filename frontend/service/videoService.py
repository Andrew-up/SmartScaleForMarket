import time

from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
import cv2
from definitions import VIDEO_OR_IMAGE_TEST_PATH
import numpy as np

kernel = np.ones((10, 10), np.uint8)


def image_crop_opencv(image):
    h, w = image.shape[1] // 2, image.shape[0] // 2
    image_resize = cv2.resize(image, (h, w), cv2.INTER_AREA)
    nul = np.zeros((image_resize.shape[0], 50, 3))
    nul[:, :] = [255, 255, 255]
    img = np.hstack((nul, image_resize))
    image = (np.hstack((img, nul))).astype(np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gaus = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(gaus, 120, 255, cv2.THRESH_BINARY)
    dilation = cv2.erode(thresh, kernel, iterations=10)
    edged = cv2.Canny(dilation, 100, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    holst = np.zeros([224, 224, 3], np.uint8)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # cv2.rectangle(image_resize, (x, y), (x + w, y + h), (0, 255, 0), 2)
        crop = image_resize[y:h + y, x:w + x]

        if crop.shape[0] > 1 and crop.shape[1] > 1:
            crop_resize = cv2.resize(crop, (holst.shape[1], holst.shape[0]))
            # cv2.imshow('image', crop_resize)
            convertToQtFormat = QImage(crop_resize.data, crop_resize.shape[1], crop_resize.shape[0],
                                       QImage.Format.Format_BGR888)
            p2 = convertToQtFormat.scaled(224, 224, Qt.KeepAspectRatio)
            return p2

    return -1
    # pass


class VideoWorker(QThread):
    changePixmap = Signal(QImage)
    end_video = Signal()
    timer = Signal(QImage)
    playVideo = False

    def run(self):
        cap = cv2.VideoCapture(VIDEO_OR_IMAGE_TEST_PATH + 'video/video3.mp4')
        frameTime = 20
        timer = time.time()
        while True:
            # print(self.playVideo)
            if self.playVideo is False:
                # self.
                # print("pause")
                time.sleep(0.1)
                continue

            if self.playVideo:
                ret, frame = cap.read()
                if ret:
                    img_crop = image_crop_opencv(frame)
                    if img_crop != -1:
                        print(img_crop)

                        if time.time() - timer >= 0.5:
                            timer = time.time()
                            self.timer.emit(img_crop)

                        # cv2.rectangle(img_crop, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        # convertToQtFormat = QImage(img_crop.data, img_crop.shape[1], img_crop.shape[0],
                        #                            QImage.Format.Format_BGR888)
                        #
                        # p = convertToQtFormat.scaled(224, 224, Qt.KeepAspectRatio)
                        self.changePixmap.emit(img_crop)

                if ret is False:
                    self.end_video.emit()
                    break

                if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                    break


if __name__ == '__main__':
    pass
    # displayFrame()
    # v = VideoService()
    # v.start()
    # Test().start()
    # th.changePixmap.connect()
    # th.start()
