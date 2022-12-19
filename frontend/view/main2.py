import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QScrollArea, QFrame, QHBoxLayout, QWidget, \
    QDialog, QVBoxLayout, QLineEdit
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.mainwindow import Ui_MainWindow
from frontend.view.qt_ui.formwidget import ProductWidget
from frontend.view.qt_ui.search_by_number_widget import SearchByNumberWidget
from frontend.view.qt_ui.search_by_name import SearchByNameWidget


class MainWindow(QMainWindow):
    delete = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_widget.clicked.connect(self.add)
        self.count: int = 0
        self.ui.button_search_by_number.clicked.connect(self.open_form_search_by_number)
        self.ui.button_search_by_name.clicked.connect(self.open_search_by_name_widget)
        self.form_search_by_number = SearchByNumberWidget()
        self.form_search_by_name = SearchByNameWidget()

    # @Slot
    def open_form_search_by_number(self):
        self.form_search_by_number.setModal(True)
        self.form_search_by_number.exec()

    def open_search_by_name_widget(self):
        self.form_search_by_name.setModal(True)
        self.form_search_by_name.exec()

    @Slot()
    def add(self):
        self.count += 1
        formwidget = ProductWidget(self.count)
        self.ui.product_List_Layout.addWidget(formwidget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
