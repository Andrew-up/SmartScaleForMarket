import os
import random
import sys

import cv2
import time
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize, QThread, Signal, Slot, Qt, QRect
from PySide6.QtGui import QImage, QPixmap, QFont
from UI.qt_ui.ui_mainwindow2 import Ui_MainWindow
from definitions import MODEL_CNN_PATH, TEST_PATH
from service.productService import findAll, addProduct
import cv2
from service import imageService

a = 0


def iterator():
    global a
    a += 1

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        imageService.loadModel(MODEL_CNN_PATH)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.gridLayout.setColumnStretch(3, 0)
        self.ui.pushButton.clicked.connect(self.getAllProduct)
        self.ui.addProductButton.clicked.connect(self.addProduct)
        self.counter_id: int = 0
        self.ui.pushButton_3.setText("Очистить")
        self.ui.pushButton_3.clicked.connect(self.clear)
        self.ui.pushButton_4.setText("Случайная\nкартинка")
        self.ui.pushButton_4.clicked.connect(self.randomImage)

    def randomImage(self):

        imagePath = imageService.getRandomImage()
        image = cv2.imread(imagePath)
        imageArray = imageService.imagePathToArray(imagePath)
        res = imageService.whoIsImage(imageArray, imageService.categories)
        # print(res)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
        label = self.ui.label
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        x, y, z = image.shape
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.setGeometry(QRect(label.geometry().x(), 200, x, y))
        # print(pixmap.width(), pixmap.height())
        font = QFont("Arial", 16)
        string = ''
        self.ui.listWidget.setFont(font)
        self.ui.listWidget.clear()
        for a in res:
            string += a[0] + ' ' + str(a[1]) + '% \n'
            if a[1] > 90:
                textItem = a[0]
                self.ui.listWidget.addItem(textItem)

        self.ui.textProduct.setFont(font)
        self.ui.textProduct.setText(string)

    def clear(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(i).widget().deleteLater()

    def getAllProduct(self):
        result = findAll()
        for row in result:
            iterator()
            print(row.id_Product)
            self.counter_id += 1
            button = QPushButton()
            button.setText(row.name_Product)
            button.setFixedSize(QSize(75, 75))
            button.clicked.connect(self.print_this)
            self.ui.gridLayout.addWidget(button)

    def addProduct(self):
        text = self.ui.lineEdit.text()
        record = addProduct(text)
        print("добавлена новая запись, id: " + str(record))
        iterator()

    def print_this(self):
        sender = self.sender()
        self.ui.listWidget.addItem(sender.text())
        print(sender)


def startApp():
    # pass
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())