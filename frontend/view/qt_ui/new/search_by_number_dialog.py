# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_by_number_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import frontend.view.qt_ui.new.resourses_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(348, 518)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(330, 500))
        self.widget.setMaximumSize(QSize(330, 500))
        self.widget.setStyleSheet(u"QWidget\n"
"{\n"
"   background-color: white;\n"
"   color: black;\n"
"   border: 2px solid black ; /* Black */\n"
"	text-align: center;\n"
"   border-radius:  10px;\n"
"	font-size: 30pt;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_n_7 = QPushButton(self.widget)
        self.button_n_7.setObjectName(u"button_n_7")
        self.button_n_7.setMinimumSize(QSize(75, 75))
        self.button_n_7.setMaximumSize(QSize(75, 75))
        self.button_n_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_7, 3, 0, 1, 1)

        self.button_n_1 = QPushButton(self.widget)
        self.button_n_1.setObjectName(u"button_n_1")
        self.button_n_1.setMinimumSize(QSize(75, 75))
        self.button_n_1.setMaximumSize(QSize(75, 75))
        self.button_n_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_1, 0, 0, 1, 1)

        self.button_n_3 = QPushButton(self.widget)
        self.button_n_3.setObjectName(u"button_n_3")
        self.button_n_3.setMinimumSize(QSize(75, 75))
        self.button_n_3.setMaximumSize(QSize(75, 75))
        self.button_n_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_3, 0, 2, 1, 1)

        self.button_n_4 = QPushButton(self.widget)
        self.button_n_4.setObjectName(u"button_n_4")
        self.button_n_4.setMinimumSize(QSize(75, 75))
        self.button_n_4.setMaximumSize(QSize(75, 75))
        self.button_n_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_4, 2, 0, 1, 1)

        self.button_n_8 = QPushButton(self.widget)
        self.button_n_8.setObjectName(u"button_n_8")
        self.button_n_8.setMinimumSize(QSize(75, 75))
        self.button_n_8.setMaximumSize(QSize(75, 75))
        self.button_n_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_8, 3, 1, 1, 1)

        self.button_n_2 = QPushButton(self.widget)
        self.button_n_2.setObjectName(u"button_n_2")
        self.button_n_2.setMinimumSize(QSize(75, 75))
        self.button_n_2.setMaximumSize(QSize(75, 75))
        self.button_n_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_2, 0, 1, 1, 1)

        self.button_n_6 = QPushButton(self.widget)
        self.button_n_6.setObjectName(u"button_n_6")
        self.button_n_6.setMinimumSize(QSize(75, 75))
        self.button_n_6.setMaximumSize(QSize(75, 75))
        self.button_n_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_6, 2, 2, 1, 1)

        self.button_n_5 = QPushButton(self.widget)
        self.button_n_5.setObjectName(u"button_n_5")
        self.button_n_5.setMinimumSize(QSize(75, 75))
        self.button_n_5.setMaximumSize(QSize(75, 75))
        self.button_n_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_5, 2, 1, 1, 1)

        self.button_n_9 = QPushButton(self.widget)
        self.button_n_9.setObjectName(u"button_n_9")
        self.button_n_9.setMinimumSize(QSize(75, 75))
        self.button_n_9.setMaximumSize(QSize(75, 75))
        self.button_n_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_9, 3, 2, 1, 1)

        self.button_yes = QPushButton(self.widget)
        self.button_yes.setObjectName(u"button_yes")
        self.button_yes.setMinimumSize(QSize(75, 75))
        self.button_yes.setMaximumSize(QSize(75, 75))
        self.button_yes.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/yes_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_yes.setIcon(icon)
        self.button_yes.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.button_yes, 4, 0, 1, 1)

        self.button_n_0 = QPushButton(self.widget)
        self.button_n_0.setObjectName(u"button_n_0")
        self.button_n_0.setMinimumSize(QSize(75, 75))
        self.button_n_0.setMaximumSize(QSize(75, 75))
        self.button_n_0.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_n_0, 4, 1, 1, 1)

        self.button_no = QPushButton(self.widget)
        self.button_no.setObjectName(u"button_no")
        self.button_no.setMinimumSize(QSize(75, 75))
        self.button_no.setMaximumSize(QSize(75, 75))
        self.button_no.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/no_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_no.setIcon(icon1)
        self.button_no.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.button_no, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_go_main_menu = QPushButton(self.widget)
        self.button_go_main_menu.setObjectName(u"button_go_main_menu")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.button_go_main_menu.setFont(font)

        self.verticalLayout.addWidget(self.button_go_main_menu)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button_n_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.button_n_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button_n_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.button_n_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button_n_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button_n_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.button_n_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.button_n_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button_n_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.button_yes.setText("")
        self.button_n_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button_no.setText("")
        self.button_go_main_menu.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

