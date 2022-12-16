import sys

from PySide6.QtWidgets import QWidget, QApplication
from frontend.view.qt_ui.new.item_product import Ui_Form


class ItemProductWidget(QWidget):

    def __init__(self, parent=None):
        super(ItemProductWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = ItemProductWidget()
    window.show()
    sys.exit(app.exec())

