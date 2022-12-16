import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Slot, Signal, Qt
from frontend.view.qt_ui.new.search_by_number_dialog import Ui_Form


class SearchByNumberWidget(QDialog):

    def __init__(self, parent=None):
        super(SearchByNumberWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setText("")
        self.ui.button_n_0.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_1.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_2.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_3.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_4.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_5.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_6.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_7.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_8.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_n_9.clicked.connect(self.add_number_label_by_name_button)
        self.ui.button_no.clicked.connect(self.clear_label)
        self.ui.button_yes.clicked.connect(self.search_product_by_label)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setFixedSize(self.size())
        # self.ui.widget.setMaximumWidth(500)
        # self.ui.widget.setMaximumHeight(300)
        self.ui.button_go_main_menu.clicked.connect(self.go_main_menu)

    # @Slot
    def add_number_label_by_name_button(self):
        sender = self.sender()
        self.ui.label.setText(self.ui.label.text() + sender.text())

    def clear_label(self):
        self.ui.label.setText("")

    def search_product_by_label(self):
        print(f"Ищу продукты с id: {self.ui.label.text()}")

    def go_main_menu(self):
        self.close()


if __name__ == '__main__':
    app = QApplication()
    window = SearchByNumberWidget()
    window.show()
    sys.exit(app.exec())
