# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_product.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(168, 168)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.item_widget = QWidget(Form)
        self.item_widget.setObjectName(u"item_widget")
        self.item_widget.setMinimumSize(QSize(150, 150))
        self.item_widget.setMaximumSize(QSize(150, 150))
        self.item_widget.setStyleSheet(u"QObject#item_widget\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 20pt;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QObject#item_widget:hover\n"
"{\n"
"  box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;\n"
"  background-color: #e3e3e3;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.item_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.item_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"height :80%;\n"
"background-color: rgb(208, 208, 208);\n"
"border: 2px solid black ; /* Black */\n"
"border-radius:  10px;\n"
"font-size: 20px;")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.item_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"max-height :40%;\n"
"border: 2px solid black ; /* Black */\n"
"border-radius:  10px;\n"
"font-size: 12px;\n"
"font-weight: bold;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout.addWidget(self.item_widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"IMAGE", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NAME PRODUCT ", None))
    # retranslateUi

