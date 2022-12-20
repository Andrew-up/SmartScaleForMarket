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


def get_random_image_path():
    twopatch = TEST_PATH + '/' + os.path.join(random.choice(os.listdir(TEST_PATH))) + '/'
    imagePath = os.path.join(twopatch, random.choice(os.listdir(twopatch)))
    return imagePath
