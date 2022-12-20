# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)
import frontend.view.qt_ui.new.resourses_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 722)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.weight_label = QLabel(self.centralwidget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setGeometry(QRect(300, 20, 301, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setStrikeOut(False)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet(u"QLabel\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 20pt;\n"
"}\n"
"")
        self.weight_label.setAlignment(Qt.AlignCenter)
        self.sum_label = QLabel(self.centralwidget)
        self.sum_label.setObjectName(u"sum_label")
        self.sum_label.setGeometry(QRect(620, 20, 261, 61))
        self.sum_label.setStyleSheet(u"QLabel\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"font-size:20pt;\n"
"}\n"
"")
        self.sum_label.setAlignment(Qt.AlignCenter)
        self.label_who_is_product = QLabel(self.centralwidget)
        self.label_who_is_product.setObjectName(u"label_who_is_product")
        self.label_who_is_product.setGeometry(QRect(540, 100, 281, 71))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_who_is_product.setFont(font1)
        self.label_who_is_product.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_who_is_product.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 110, 391, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 389, 359))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.product_List_Layout = QHBoxLayout()
        self.product_List_Layout.setObjectName(u"product_List_Layout")

        self.horizontalLayout_2.addLayout(self.product_List_Layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.button_NO_product = QPushButton(self.centralwidget)
        self.button_NO_product.setObjectName(u"button_NO_product")
        self.button_NO_product.setGeometry(QRect(700, 180, 101, 100))
        font2 = QFont()
        font2.setPointSize(20)
        self.button_NO_product.setFont(font2)
        self.button_NO_product.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.button_YES_product = QPushButton(self.centralwidget)
        self.button_YES_product.setObjectName(u"button_YES_product")
        self.button_YES_product.setGeometry(QRect(560, 180, 100, 100))
        self.button_YES_product.setFont(font2)
        self.button_YES_product.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.add_widget = QPushButton(self.centralwidget)
        self.add_widget.setObjectName(u"add_widget")
        self.add_widget.setGeometry(QRect(460, 300, 121, 51))
        self.add_widget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.clear_widget = QPushButton(self.centralwidget)
        self.clear_widget.setObjectName(u"clear_widget")
        self.clear_widget.setGeometry(QRect(460, 370, 121, 51))
        self.clear_widget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 510, 1021, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 50, 0)
        self.button_search_by_name = QPushButton(self.layoutWidget)
        self.button_search_by_name.setObjectName(u"button_search_by_name")
        self.button_search_by_name.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(18)
        self.button_search_by_name.setFont(font3)
        self.button_search_by_name.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(200, 200, 200); /* Gray */\n"
"    color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.button_search_by_name)

        self.button_search_by_number = QPushButton(self.layoutWidget)
        self.button_search_by_number.setObjectName(u"button_search_by_number")
        self.button_search_by_number.setMinimumSize(QSize(0, 50))
        self.button_search_by_number.setSizeIncrement(QSize(1, 0))
        self.button_search_by_number.setFont(font3)
        self.button_search_by_number.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(200, 200, 200); /* Gray */\n"
"    color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.button_search_by_number)

        self.button_search_by_catalog = QPushButton(self.layoutWidget)
        self.button_search_by_catalog.setObjectName(u"button_search_by_catalog")
        self.button_search_by_catalog.setMinimumSize(QSize(0, 50))
        self.button_search_by_catalog.setFont(font3)
        self.button_search_by_catalog.setStyleSheet(u"QPushButton\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(200, 200, 200); /* Gray */\n"
"    color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.button_search_by_catalog)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 221, 61))
        self.label.setPixmap(QPixmap(u":/icon/logo.png"))
        self.label.setScaledContents(True)
        self.image_to_cnn = QLabel(self.centralwidget)
        self.image_to_cnn.setObjectName(u"image_to_cnn")
        self.image_to_cnn.setGeometry(QRect(830, 300, 175, 175))
        self.image_to_cnn.setStyleSheet(u"background-color: rgb(83, 94, 255);")
        self.getRandomImageButton = QPushButton(self.centralwidget)
        self.getRandomImageButton.setObjectName(u"getRandomImageButton")
        self.getRandomImageButton.setGeometry(QRect(610, 320, 161, 121))
        self.getRandomImageButton.setMouseTracking(False)
        self.getRandomImageButton.setCheckable(False)
        self.getRandomImageButton.setAutoRepeat(True)
        self.getRandomImageButton.setAutoExclusive(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.weight_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.sum_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_who_is_product.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442 \u043d\u0430 \u0432\u0435\u0441\u0430\u0445?", None))
        self.button_NO_product.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415\u0422", None))
        self.button_YES_product.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410", None))
        self.add_widget.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clear_widget.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.button_search_by_name.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.button_search_by_number.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u043e\u043c\u0435\u0440\u0443", None))
        self.button_search_by_catalog.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0443", None))
        self.label.setText("")
        self.image_to_cnn.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.getRandomImageButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \n"
" \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e\u0439 \n"
" \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438", None))
    # retranslateUi

