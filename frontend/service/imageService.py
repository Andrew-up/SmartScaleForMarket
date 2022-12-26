import os
import random
from io import BytesIO

from PySide6.QtCore import QByteArray, QBuffer, QIODevice

from definitions import TEST_PATH
import base64
from PySide6.QtGui import QImage, QPixmap
from frontend.controller.modelCNNController import ModelCNNController


class ImageService:

    def __init__(self, parent=None):
        super(ImageService, self).__init__()
        self.image_path = ''
        self.image_base64 = ''

    def get_image_path(self):
        twopatch = TEST_PATH + '/' + os.path.join(random.choice(os.listdir(TEST_PATH))) + '/'
        imagePath = os.path.join(twopatch, random.choice(os.listdir(twopatch)))
        self.image_path = imagePath
        return imagePath

    def path_to_pixmap(self, path):
        pixmap = QPixmap(path)
        return pixmap

    def base64_to_pixmap(self, blob_image):
        ba = QByteArray.fromBase64(blob_image)
        img = QImage.fromData(ba, 'PNG')
        pixmap = QPixmap.fromImage(img)
        return pixmap

    def get_image_base64(self, image_path):
        with open(str(image_path), "rb") as img_file:
            image = QImage(img_file.name)
            image = image.scaledToWidth(224)
            image = image.scaledToHeight(224)
            ba = QByteArray()
            buffer = QBuffer(ba)
            buffer.open(QIODevice.WriteOnly)
            image.save(buffer, 'PNG')
            base64_data = ba.toBase64().data()
            string_utf_8 = base64_data.decode('utf-8')
            self.image_path = string_utf_8
            return string_utf_8

    def QImage_to_base64(self, qimage: QImage):
        image = qimage.scaledToWidth(300)
        image = qimage.scaledToHeight(300)
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        base64_data = ba.toBase64().data()
        string_utf_8 = base64_data.decode('utf-8')
        # print(string_utf_8)
        return string_utf_8

    def get_image_qimage(self):
        image = QImage(self.get_image_path())
        image = image.scaledToWidth(224)
        image = image.scaledToHeight(224)
        return image


if __name__ == '__main__':
    image_service = ImageService()
    image_path = image_service.get_image_path()
    image_base64 = image_service.get_image_base64(image_path)
    con = ModelCNNController().image_predict_from_image_base64(image_base64)
    pass
