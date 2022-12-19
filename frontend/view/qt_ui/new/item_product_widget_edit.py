# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_product_widget_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(574, 88)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.id_product_label = QLabel(Form)
        self.id_product_label.setObjectName(u"id_product_label")
        self.id_product_label.setMaximumSize(QSize(16777215, 70))
        self.id_product_label.setStyleSheet(u"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 12pt;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;")

        self.horizontalLayout.addWidget(self.id_product_label)

        self.name_product_label = QLabel(Form)
        self.name_product_label.setObjectName(u"name_product_label")
        self.name_product_label.setMaximumSize(QSize(16777215, 70))
        self.name_product_label.setStyleSheet(u"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 12pt;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;")

        self.horizontalLayout.addWidget(self.name_product_label)

        self.image_product_label = QLabel(Form)
        self.image_product_label.setObjectName(u"image_product_label")
        self.image_product_label.setMaximumSize(QSize(70, 70))
        self.image_product_label.setStyleSheet(u"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 12pt;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;")

        self.horizontalLayout.addWidget(self.image_product_label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 70))
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 70))
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_product_label.setText(QCoreApplication.translate("Form", u"id \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.name_product_label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.image_product_label.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

