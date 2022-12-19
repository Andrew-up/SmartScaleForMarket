import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.edit_product_widget import Ui_Form
from frontend.model.product import Product


class ProductEditWidget(QWidget):

    def __init__(self, product: Product, parent=None):
        super(ProductEditWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_2.setText(str(product.id_Product))
        self.ui.textEdit.setText(product.name_Product)


if __name__ == '__main__':
    app = QApplication()
    p = Product()
    p.id_Product = 1
    p.name_Product = "test"
    window = ProductEditWidget(p)
    window.show()
    sys.exit(app.exec())
