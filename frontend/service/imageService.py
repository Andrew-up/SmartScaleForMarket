import os
import random

from PySide6.QtCore import QByteArray
from PySide6.QtGui import QImage, QPixmap

from definitions import TEST_PATH


def base64_to_pixmap(blob_image):
    ba = QByteArray.fromBase64(blob_image)
    img = QImage.fromData(ba, 'PNG')
    pixmap = QPixmap.fromImage(img)
    return pixmap


def path_to_pixmap(path):
    pixmap = QPixmap(path)
    return pixmap


