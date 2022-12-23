from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
import cv2
from definitions import VIDEO_OR_IMAGE_TEST_PATH


class VideoWorker(QThread):
    changePixmap = Signal(QImage)
    end_video = Signal()

    def run(self):
        cap = cv2.VideoCapture(VIDEO_OR_IMAGE_TEST_PATH+'video/video1.mp4')
        frameTime = 5
        while True:
            ret, frame = cap.read()
            # print(cap.get(cv2.CAP_PROP_FPS))
            # print(ret)
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format.Format_RGB888)
                p = convertToQtFormat.scaled(500, 500, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
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
