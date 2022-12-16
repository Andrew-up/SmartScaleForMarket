import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Slot, Signal, Qt

from frontend.view.qt_ui.new.search_by_name_widget import Ui_search_by_name_widget
from frontend.view.qt_ui.new.item_product_wigdet import ItemProductWidget


class SearchByNameWidget(QDialog):
    delete = Signal(int)

    def __init__(self, parent=None):
        super(SearchByNameWidget, self).__init__(parent)
        self.ui = Ui_search_by_name_widget()
        self.ui.setupUi(self)
        self.ui.key_Q.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_W.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_E.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_R.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_T.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_Y.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_U.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_I.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_O.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_P.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_bracket_left.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_bracket_rigth.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_A.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_S.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_D.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_F.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_G.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_H.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_J.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_K.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.key_L.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Colon.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Quotes.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Z.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_X.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_C.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_V.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_B.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_N.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_M.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Comma.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Dot.clicked.connect(self.add_letter_line_edit_by_name_button)
        self.ui.Key_Space.clicked.connect(self.add_space)
        self.ui.key_backspace.clicked.connect(self.backspace)
        self.ui.button_line_edit_clear.clicked.connect(self.clear_line_edit)
        self.ui.go_main_menu_button.clicked.connect(self.close_widget)
        self.ui.lineEdit.setText("")
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.ui.Key_Space.clicked.connect(self.add)
        # self.ui.gridLayout_2
        self.num_row: int = 0
        self.num_column: int = 0


        for a in range(6):
            self.add()

    def add_space(self):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + " ")

    def backspace(self):
        text = self.ui.lineEdit.text()
        # self.ui.lineEdit.setText(Qt.Key_Backspace)
        if len(text) != 1:
            self.ui.lineEdit.setText(text[:-1])
        else:
            self.ui.lineEdit.setText("")

    def add_letter_line_edit_by_name_button(self):
        sender = self.sender()
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + sender.text())
        # self.id_wigdet = id_wigdet

    def clear_line_edit(self):
        self.ui.lineEdit.setText("")

    def close_widget(self):
        self.close()
        # pass

    @Slot()
    def add(self):
        item_widget = ItemProductWidget()
        self.ui.gridLayout_2.addWidget(item_widget, self.num_row, self.num_column)
        self.num_column += 1
        if self.num_column % 4 == 0:
            self.num_column = 0
            self.num_row += 1


if __name__ == '__main__':
    app = QApplication()
    window = SearchByNameWidget()
    window.show()
    sys.exit(app.exec())
