# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_edit_product_widget(object):
    def setupUi(self, edit_product_widget):
        if not edit_product_widget.objectName():
            edit_product_widget.setObjectName(u"edit_product_widget")
        edit_product_widget.resize(685, 377)
        self.verticalLayout_2 = QVBoxLayout(edit_product_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(edit_product_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 665, 263))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_item_widget = QVBoxLayout()
        self.list_item_widget.setObjectName(u"list_item_widget")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")

        self.list_item_widget.addWidget(self.widget)


        self.verticalLayout.addLayout(self.list_item_widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.widget_2 = QWidget(edit_product_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.update_list_widget_button = QPushButton(self.widget_2)
        self.update_list_widget_button.setObjectName(u"update_list_widget_button")
        self.update_list_widget_button.setMinimumSize(QSize(50, 70))

        self.horizontalLayout_6.addWidget(self.update_list_widget_button)

        self.add_new_product_button = QPushButton(self.widget_2)
        self.add_new_product_button.setObjectName(u"add_new_product_button")
        self.add_new_product_button.setMinimumSize(QSize(50, 70))

        self.horizontalLayout_6.addWidget(self.add_new_product_button)

        self.clear_all_product_button = QPushButton(self.widget_2)
        self.clear_all_product_button.setObjectName(u"clear_all_product_button")
        self.clear_all_product_button.setMinimumSize(QSize(50, 70))

        self.horizontalLayout_6.addWidget(self.clear_all_product_button)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(edit_product_widget)

        QMetaObject.connectSlotsByName(edit_product_widget)
    # setupUi

    def retranslateUi(self, edit_product_widget):
        edit_product_widget.setWindowTitle(QCoreApplication.translate("edit_product_widget", u"Form", None))
        self.update_list_widget_button.setText(QCoreApplication.translate("edit_product_widget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432", None))
        self.add_new_product_button.setText(QCoreApplication.translate("edit_product_widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.clear_all_product_button.setText(QCoreApplication.translate("edit_product_widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
    # retranslateUi

