# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recognition_widget_cnn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_productListWidget(object):
    def setupUi(self, productListWidget):
        if not productListWidget.objectName():
            productListWidget.setObjectName(u"productListWidget")
        productListWidget.resize(275, 320)
        productListWidget.setMinimumSize(QSize(275, 320))
        self.frame = QFrame(productListWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setGeometry(QRect(10, 10, 250, 300))
        self.frame.setMinimumSize(QSize(250, 300))
        self.frame.setMaximumSize(QSize(250, 300))
        self.frame.setStyleSheet(u"QFrame#frame\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 20pt;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_image_product = QLabel(self.frame)
        self.label_image_product.setObjectName(u"label_image_product")
        self.label_image_product.setGeometry(QRect(20, 20, 200, 200))
        self.label_image_product.setStyleSheet(u"QLabel\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"}")
        self.label_name_product = QLabel(self.frame)
        self.label_name_product.setObjectName(u"label_name_product")
        self.label_name_product.setGeometry(QRect(30, 230, 181, 51))
        self.label_name_product.setStyleSheet(u"QLabel\n"
"{\n"
"   color: black;\n"
"	font-size: 20pt;\n"
"}")
        self.label_name_product.setAlignment(Qt.AlignCenter)

        self.retranslateUi(productListWidget)

        QMetaObject.connectSlotsByName(productListWidget)
    # setupUi

    def retranslateUi(self, productListWidget):
        productListWidget.setWindowTitle(QCoreApplication.translate("productListWidget", u"Form", None))
        self.label_image_product.setText(QCoreApplication.translate("productListWidget", u"TextLabel", None))
        self.label_name_product.setText(QCoreApplication.translate("productListWidget", u"TextLabel", None))
    # retranslateUi

