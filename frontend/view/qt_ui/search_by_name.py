import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Slot, Signal, Qt

from frontend.view.qt_ui.new.search_by_name_widget import Ui_search_by_name_widget
from frontend.view.qt_ui.new.item_product_wigdet import ItemProductWidget
from frontend.view.qt_ui.keyboard_widget import KeyBoardWidget
from frontend.controller.productController import ProductController
from frontend.model.product import Product


class SearchByNameWidget(QDialog):

    def __init__(self, parent=None):
        super(SearchByNameWidget, self).__init__(parent)
        self.ui = Ui_search_by_name_widget()
        self.ui.setupUi(self)
        self.ui.button_line_edit_clear.clicked.connect(self.clear_line_edit)
        self.ui.go_main_menu_button.clicked.connect(self.close_widget)
        self.ui.lineEdit.setText("")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.ui.Key_Space.clicked.connect(self.add)
        # self.ui.gridLayout_2
        self.num_row: int = 0
        self.num_column: int = 0
        self.keyboard_widget = KeyBoardWidget()
        self.initKeyboard(self.keyboard_widget)  # Добавить виджет клавиатуры
        self.ui.lineEdit.setFocus()  # Установить фокус на ввод текста
        self.fill_card_all_product()  # Заполнить карточку всеми товарами

    def fill_card_all_product(self):
        p = ProductController(Product(), self)
        for a in p.all_products():
            self.add(a.name_Product)

    def initKeyboard(self, keyboard: KeyBoardWidget):
        # Добавление виджета
        self.ui.layout_for_keyboard_widget.addWidget(self.keyboard_widget)
        self.ui.layout_for_keyboard_widget.setContentsMargins(0, 0, 0, 0)
        # Кнопка открыть/закрыть клавиатуру
        self.ui.open_close_keyboad_button.clicked.connect(self.open_close_keyboard)
        # Инициализация кнопок
        keyboard.ui.key_W.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_E.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_R.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_T.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_Y.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_U.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_I.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_O.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_P.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_bracket_left.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_bracket_rigth.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_A.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_S.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_D.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_F.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_G.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_H.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_J.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_K.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.key_L.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Colon.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Quotes.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Z.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_X.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_C.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_V.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_B.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_N.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_M.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Comma.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Dot.clicked.connect(self.add_letter_line_edit_by_name_button)
        keyboard.ui.Key_Space.clicked.connect(self.add_space)
        keyboard.ui.key_backspace.clicked.connect(self.backspace)

    def add_letter_line_edit_by_name_button(self):
        sender = self.sender()
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + sender.text())

    def add_space(self):
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + " ")

    def backspace(self):
        self.ui.lineEdit.setFocus()
        text = self.ui.lineEdit.text()
        if len(text) != 1:
            self.ui.lineEdit.setText(text[:-1])
        else:
            self.ui.lineEdit.setText("")

    @Slot()
    def open_close_keyboard(self):
        if self.keyboard_widget.isHidden():
            self.keyboard_widget.show()
            self.ui.open_close_keyboad_button.setText("Закрыть клавиатуру")
        else:
            self.keyboard_widget.hide()
            self.ui.open_close_keyboad_button.setText("Открыть клавиатуру")

    def clear_line_edit(self):
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText("")

    def close_widget(self):
        self.close()
        # pass

    @Slot()
    def add(self, name_product: str):
        item_widget = ItemProductWidget()
        item_widget.ui.label_2.setText(name_product)
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
