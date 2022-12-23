import sys
import cv2
from PySide6.QtGui import QImage, QIcon, QPainter
from PySide6.QtCore import QTimer, QObject, QThread
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
import qimage2ndarray


class CameraStream(QWidget, QObject):
    print("p")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cameraStream = CameraStream()
    cameraStream.move(100, 100)
    cameraStream.resize(600, 500)
    cameraStream.show()
    sys.exit(app.exec_())