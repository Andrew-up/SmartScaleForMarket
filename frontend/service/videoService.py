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
        image_draw = image_resize.copy()
        image_draw_rectangle = cv2.rectangle(image_draw, (x, y), (x + w, y + h), (0, 0, 255), 7)
        convertToQtFormat = QImage(image_draw_rectangle.data, image_draw_rectangle.shape[1], image_draw_rectangle.shape[0],
                      QImage.Format.Format_BGR888)
        image_detect_qt_format = convertToQtFormat.scaled(224, 224, Qt.KeepAspectRatio)

        crop = image_resize[y:h + y, x:w + x]
        if crop.shape[0] > 70 and crop.shape[1] > 70:
            crop_resize = cv2.resize(crop, (holst.shape[1], holst.shape[0]))
            convertToQtFormats = QImage(crop_resize.data, crop_resize.shape[1], crop_resize.shape[0],
                                       QImage.Format.Format_BGR888)
            crop_resize_qt = convertToQtFormats.scaled(224, 224, Qt.KeepAspectRatio)
            return image_detect_qt_format, crop_resize_qt

    convertToQtFormat = QImage(image_resize.data, image_resize.shape[1], image_resize.shape[0],
                                QImage.Format.Format_BGR888)
    image_not_detect = convertToQtFormat.scaled(224, 224, Qt.KeepAspectRatio)

    return image_not_detect, False


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
                    image_frame, image_crop = image_crop_opencv(frame)
                    self.changePixmap.emit(image_frame)

                    # if image_resize != -1:
                    #
                    #     if time.time() - timer >= 0.5:
                    #         timer = time.time()
                    if image_crop is not False:
                        if time.time() - timer >= 0.2:
                            timer = time.time()
                            self.timer.emit(image_crop)

                    if image_crop is False:
                        if time.time() - timer >= 0.5:
                            timer = time.time()
                            self.timer.emit(image_frame)



                        # cv2.rectangle(img_crop, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        #


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
