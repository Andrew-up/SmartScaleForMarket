import time

from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
import cv2
from definitions import VIDEO_OR_IMAGE_TEST_PATH


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
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                               QImage.Format.Format_RGB888)
                    p = convertToQtFormat.scaled(224, 224, Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)
                    if time.time() - timer >= 0.5:
                        timer = time.time()
                        self.timer.emit(p)

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
