# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_by_name_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_search_by_name_widget(object):
    def setupUi(self, search_by_name_widget):
        if not search_by_name_widget.objectName():
            search_by_name_widget.setObjectName(u"search_by_name_widget")
        search_by_name_widget.resize(914, 687)
        search_by_name_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(search_by_name_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.button_line_edit_clear = QPushButton(search_by_name_widget)
        self.button_line_edit_clear.setObjectName(u"button_line_edit_clear")
        self.button_line_edit_clear.setMinimumSize(QSize(0, 50))
        self.button_line_edit_clear.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:hover{\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(195, 195, 195);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_line_edit_clear, 1, 2, 1, 1)

        self.go_main_menu_button = QPushButton(search_by_name_widget)
        self.go_main_menu_button.setObjectName(u"go_main_menu_button")
        self.go_main_menu_button.setMinimumSize(QSize(200, 50))
        self.go_main_menu_button.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:hover{\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(195, 195, 195);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.go_main_menu_button, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(search_by_name_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"   background-color: white;\n"
"   color: black;\n"
"    border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"    border-radius:  10px;\n"
"	font-size: 20pt;\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.widget_2 = QWidget(search_by_name_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 876, 443))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addLayout(self.gridLayout_2, 1, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget = QWidget(search_by_name_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"QPushButton {\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 20pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(195, 195, 195);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_for_keyboard_widget = QVBoxLayout()
        self.layout_for_keyboard_widget.setObjectName(u"layout_for_keyboard_widget")
        self.layout_for_keyboard_widget.setContentsMargins(-1, 10, -1, -1)

        self.verticalLayout.addLayout(self.layout_for_keyboard_widget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, -1, -1)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.open_close_keyboad_button = QPushButton(self.widget)
        self.open_close_keyboad_button.setObjectName(u"open_close_keyboad_button")
        self.open_close_keyboad_button.setStyleSheet(u"	padding-left: 10px;\n"
"	padding-right: 10px;")

        self.horizontalLayout_7.addWidget(self.open_close_keyboad_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(search_by_name_widget)

        QMetaObject.connectSlotsByName(search_by_name_widget)
    # setupUi

    def retranslateUi(self, search_by_name_widget):
        search_by_name_widget.setWindowTitle(QCoreApplication.translate("search_by_name_widget", u"Form", None))
        self.button_line_edit_clear.setText(QCoreApplication.translate("search_by_name_widget", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.go_main_menu_button.setText(QCoreApplication.translate("search_by_name_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.lineEdit.setText(QCoreApplication.translate("search_by_name_widget", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.open_close_keyboad_button.setText(QCoreApplication.translate("search_by_name_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0443", None))
    # retranslateUi

