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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_search_by_name_widget(object):
    def setupUi(self, search_by_name_widget):
        if not search_by_name_widget.objectName():
            search_by_name_widget.setObjectName(u"search_by_name_widget")
        search_by_name_widget.resize(797, 687)
        search_by_name_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(search_by_name_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.lineEdit = QLineEdit(search_by_name_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 100))
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

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.button_line_edit_clear = QPushButton(search_by_name_widget)
        self.button_line_edit_clear.setObjectName(u"button_line_edit_clear")
        self.button_line_edit_clear.setMinimumSize(QSize(0, 100))
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

        self.horizontalLayout_6.addWidget(self.button_line_edit_clear)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.widget_2 = QWidget(search_by_name_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 759, 226))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addLayout(self.gridLayout_2, 1, 4, 1, 1)

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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.key_Q = QPushButton(self.widget)
        self.key_Q.setObjectName(u"key_Q")
        self.key_Q.setMinimumSize(QSize(50, 50))
        self.key_Q.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_Q)

        self.key_W = QPushButton(self.widget)
        self.key_W.setObjectName(u"key_W")
        self.key_W.setMinimumSize(QSize(50, 50))
        self.key_W.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_W)

        self.key_E = QPushButton(self.widget)
        self.key_E.setObjectName(u"key_E")
        self.key_E.setMinimumSize(QSize(50, 50))
        self.key_E.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_E)

        self.key_R = QPushButton(self.widget)
        self.key_R.setObjectName(u"key_R")
        self.key_R.setMinimumSize(QSize(50, 50))
        self.key_R.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_R)

        self.key_T = QPushButton(self.widget)
        self.key_T.setObjectName(u"key_T")
        self.key_T.setMinimumSize(QSize(50, 50))
        self.key_T.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_T)

        self.key_Y = QPushButton(self.widget)
        self.key_Y.setObjectName(u"key_Y")
        self.key_Y.setMinimumSize(QSize(50, 50))
        self.key_Y.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_Y)

        self.key_U = QPushButton(self.widget)
        self.key_U.setObjectName(u"key_U")
        self.key_U.setMinimumSize(QSize(50, 50))
        self.key_U.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_U)

        self.key_I = QPushButton(self.widget)
        self.key_I.setObjectName(u"key_I")
        self.key_I.setMinimumSize(QSize(50, 50))
        self.key_I.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_I)

        self.key_O = QPushButton(self.widget)
        self.key_O.setObjectName(u"key_O")
        self.key_O.setMinimumSize(QSize(50, 50))
        self.key_O.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_O)

        self.key_P = QPushButton(self.widget)
        self.key_P.setObjectName(u"key_P")
        self.key_P.setMinimumSize(QSize(50, 50))
        self.key_P.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_P)

        self.key_bracket_left = QPushButton(self.widget)
        self.key_bracket_left.setObjectName(u"key_bracket_left")
        self.key_bracket_left.setMinimumSize(QSize(50, 50))
        self.key_bracket_left.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_bracket_left)

        self.key_bracket_rigth = QPushButton(self.widget)
        self.key_bracket_rigth.setObjectName(u"key_bracket_rigth")
        self.key_bracket_rigth.setMinimumSize(QSize(50, 50))
        self.key_bracket_rigth.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_bracket_rigth)

        self.key_backspace = QPushButton(self.widget)
        self.key_backspace.setObjectName(u"key_backspace")
        self.key_backspace.setMinimumSize(QSize(75, 50))
        self.key_backspace.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.key_backspace)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.key_A = QPushButton(self.widget)
        self.key_A.setObjectName(u"key_A")
        self.key_A.setMinimumSize(QSize(50, 50))
        self.key_A.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_A)

        self.key_S = QPushButton(self.widget)
        self.key_S.setObjectName(u"key_S")
        self.key_S.setMinimumSize(QSize(50, 50))
        self.key_S.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_S)

        self.key_D = QPushButton(self.widget)
        self.key_D.setObjectName(u"key_D")
        self.key_D.setMinimumSize(QSize(50, 50))
        self.key_D.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_D)

        self.key_F = QPushButton(self.widget)
        self.key_F.setObjectName(u"key_F")
        self.key_F.setMinimumSize(QSize(50, 50))
        self.key_F.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_F)

        self.key_G = QPushButton(self.widget)
        self.key_G.setObjectName(u"key_G")
        self.key_G.setMinimumSize(QSize(50, 50))
        self.key_G.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_G)

        self.key_H = QPushButton(self.widget)
        self.key_H.setObjectName(u"key_H")
        self.key_H.setMinimumSize(QSize(50, 50))
        self.key_H.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_H)

        self.key_J = QPushButton(self.widget)
        self.key_J.setObjectName(u"key_J")
        self.key_J.setMinimumSize(QSize(50, 50))
        self.key_J.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_J)

        self.key_K = QPushButton(self.widget)
        self.key_K.setObjectName(u"key_K")
        self.key_K.setMinimumSize(QSize(50, 50))
        self.key_K.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_K)

        self.key_L = QPushButton(self.widget)
        self.key_L.setObjectName(u"key_L")
        self.key_L.setMinimumSize(QSize(50, 50))
        self.key_L.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.key_L)

        self.Key_Colon = QPushButton(self.widget)
        self.Key_Colon.setObjectName(u"Key_Colon")
        self.Key_Colon.setMinimumSize(QSize(50, 50))
        self.Key_Colon.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.Key_Colon)

        self.Key_Quotes = QPushButton(self.widget)
        self.Key_Quotes.setObjectName(u"Key_Quotes")
        self.Key_Quotes.setMinimumSize(QSize(50, 50))
        self.Key_Quotes.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.Key_Quotes)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.Key_Z = QPushButton(self.widget)
        self.Key_Z.setObjectName(u"Key_Z")
        self.Key_Z.setMinimumSize(QSize(50, 50))
        self.Key_Z.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_Z)

        self.Key_X = QPushButton(self.widget)
        self.Key_X.setObjectName(u"Key_X")
        self.Key_X.setMinimumSize(QSize(50, 50))
        self.Key_X.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_X)

        self.Key_C = QPushButton(self.widget)
        self.Key_C.setObjectName(u"Key_C")
        self.Key_C.setMinimumSize(QSize(50, 50))
        self.Key_C.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_C)

        self.Key_V = QPushButton(self.widget)
        self.Key_V.setObjectName(u"Key_V")
        self.Key_V.setMinimumSize(QSize(50, 50))
        self.Key_V.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_V)

        self.Key_B = QPushButton(self.widget)
        self.Key_B.setObjectName(u"Key_B")
        self.Key_B.setMinimumSize(QSize(50, 50))
        self.Key_B.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_B)

        self.Key_N = QPushButton(self.widget)
        self.Key_N.setObjectName(u"Key_N")
        self.Key_N.setMinimumSize(QSize(50, 50))
        self.Key_N.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_N)

        self.Key_M = QPushButton(self.widget)
        self.Key_M.setObjectName(u"Key_M")
        self.Key_M.setMinimumSize(QSize(50, 50))
        self.Key_M.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_M)

        self.Key_Comma = QPushButton(self.widget)
        self.Key_Comma.setObjectName(u"Key_Comma")
        self.Key_Comma.setMinimumSize(QSize(50, 50))
        self.Key_Comma.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_Comma)

        self.Key_Dot = QPushButton(self.widget)
        self.Key_Dot.setObjectName(u"Key_Dot")
        self.Key_Dot.setMinimumSize(QSize(50, 50))
        self.Key_Dot.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.Key_Dot)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.Key_Space = QPushButton(self.widget)
        self.Key_Space.setObjectName(u"Key_Space")
        self.Key_Space.setMinimumSize(QSize(300, 0))
        self.Key_Space.setMaximumSize(QSize(800, 16777215))

        self.horizontalLayout_5.addWidget(self.Key_Space)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, -1, -1)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.go_main_menu_button = QPushButton(self.widget)
        self.go_main_menu_button.setObjectName(u"go_main_menu_button")
        self.go_main_menu_button.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_7.addWidget(self.go_main_menu_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(search_by_name_widget)

        QMetaObject.connectSlotsByName(search_by_name_widget)
    # setupUi

    def retranslateUi(self, search_by_name_widget):
        search_by_name_widget.setWindowTitle(QCoreApplication.translate("search_by_name_widget", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("search_by_name_widget", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.button_line_edit_clear.setText(QCoreApplication.translate("search_by_name_widget", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.key_Q.setText(QCoreApplication.translate("search_by_name_widget", u"\u0419", None))
        self.key_W.setText(QCoreApplication.translate("search_by_name_widget", u"\u0426", None))
        self.key_E.setText(QCoreApplication.translate("search_by_name_widget", u"\u0423", None))
        self.key_R.setText(QCoreApplication.translate("search_by_name_widget", u"\u041a", None))
        self.key_T.setText(QCoreApplication.translate("search_by_name_widget", u"\u0415", None))
        self.key_Y.setText(QCoreApplication.translate("search_by_name_widget", u"\u041d", None))
        self.key_U.setText(QCoreApplication.translate("search_by_name_widget", u"\u0413", None))
        self.key_I.setText(QCoreApplication.translate("search_by_name_widget", u"\u0428", None))
        self.key_O.setText(QCoreApplication.translate("search_by_name_widget", u"\u0429", None))
        self.key_P.setText(QCoreApplication.translate("search_by_name_widget", u"\u0417", None))
        self.key_bracket_left.setText(QCoreApplication.translate("search_by_name_widget", u"\u0425", None))
        self.key_bracket_rigth.setText(QCoreApplication.translate("search_by_name_widget", u"\u042a", None))
        self.key_backspace.setText(QCoreApplication.translate("search_by_name_widget", u"\u232b", None))
        self.key_A.setText(QCoreApplication.translate("search_by_name_widget", u"\u0424", None))
        self.key_S.setText(QCoreApplication.translate("search_by_name_widget", u"\u042b", None))
        self.key_D.setText(QCoreApplication.translate("search_by_name_widget", u"\u0412", None))
        self.key_F.setText(QCoreApplication.translate("search_by_name_widget", u"\u0410", None))
        self.key_G.setText(QCoreApplication.translate("search_by_name_widget", u"\u041f", None))
        self.key_H.setText(QCoreApplication.translate("search_by_name_widget", u"\u0420", None))
        self.key_J.setText(QCoreApplication.translate("search_by_name_widget", u"\u041e", None))
        self.key_K.setText(QCoreApplication.translate("search_by_name_widget", u"\u041b", None))
        self.key_L.setText(QCoreApplication.translate("search_by_name_widget", u"\u0414", None))
        self.Key_Colon.setText(QCoreApplication.translate("search_by_name_widget", u"\u0416", None))
        self.Key_Quotes.setText(QCoreApplication.translate("search_by_name_widget", u"\u042d", None))
        self.Key_Z.setText(QCoreApplication.translate("search_by_name_widget", u"\u042f", None))
        self.Key_X.setText(QCoreApplication.translate("search_by_name_widget", u"\u0427", None))
        self.Key_C.setText(QCoreApplication.translate("search_by_name_widget", u"\u0421", None))
        self.Key_V.setText(QCoreApplication.translate("search_by_name_widget", u"\u041c", None))
        self.Key_B.setText(QCoreApplication.translate("search_by_name_widget", u"\u0418", None))
        self.Key_N.setText(QCoreApplication.translate("search_by_name_widget", u"\u0422", None))
        self.Key_M.setText(QCoreApplication.translate("search_by_name_widget", u"\u042c", None))
        self.Key_Comma.setText(QCoreApplication.translate("search_by_name_widget", u"\u0411", None))
        self.Key_Dot.setText(QCoreApplication.translate("search_by_name_widget", u"\u042e", None))
        self.Key_Space.setText(QCoreApplication.translate("search_by_name_widget", u"Space", None))
        self.go_main_menu_button.setText(QCoreApplication.translate("search_by_name_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

