import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.item_product_widget_edit import Ui_Form
from frontend.view.qt_ui.admin.edit_product import ProductEditWidget

class ItemProductEditWidget(QWidget):

    def __init__(self, id_product: int, parent=None):
        super(ItemProductEditWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_product = id_product
        self.ui.pushButton.clicked.connect(self.edit_product)


    @Slot()
    def edit_product(self):
        print(self.id_product)

    def get_id(self):
        return self.id_product


if __name__ == '__main__':
    app = QApplication()
    window = ItemProductEditWidget(1)
    window.show()
    sys.exit(app.exec())
