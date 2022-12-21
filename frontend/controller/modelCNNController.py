import os
from backend.service.imageService import getRandomImagePath, imagePathToArray, whoIsImage
# import base64
from PySide6.QtGui import  QImage
# from PySide6.QtCore import QString
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QByteArray

class ModelCNNController:

    def __init__(self, parent=None):
        super(ModelCNNController, self).__init__()
        self.image_path = ''
        # self.resultWorkCNN = ''
        # self.resultWorkCNN = ''
        self.image_base64 = ''

    def get_random_image(self):
        self.image_path = getRandomImagePath()

    def image_path_to_base64(self):
        with open(self.image_path, "rb") as image_path:
            print(f'{image_path.name}')
            pixmap = QPixmap(f"{image_path.name}")
            print(pixmap)
            # pixmap.scaled(200, 200)
            # ba = QByteArray.fromBase64(pixmap.toImage())
            # print(ba)
            # base64s = base64.b64encode(pixmap.toImage())

            # print(base64s)
            # print(pixmap)
            # qimage = QImage()
            # qimage.loadFromData(image_path)
            # qimage.scaled(150, 150)
            # print(qimage)
            # encoded_string = base64.b64encode(image_path.read())
            # encoded_string.decode('utf-8')
            # self.image_base64 = encoded_string
    #
    # def who_is_image(self):
    #     self.resultWorkCNN = whoIsImage(self.array_image, self.categories)


if __name__ == '__main__':
    m = ModelCNNController()
    m.get_random_image()
    m.image_path_to_base64()
    # print(m.image_path)
    # print(m.image_base64)

