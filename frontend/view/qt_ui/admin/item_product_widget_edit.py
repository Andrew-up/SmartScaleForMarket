import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.item_product_widget_edit import Ui_Form
from frontend.view.qt_ui.admin.edit_product import ProductEditWidget
from frontend.model.product import Product


class ItemProductEditWidget(QWidget):

    def __init__(self, product: Product, parent=None):
        super(ItemProductEditWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_product = product.id_Product
        self.image_Product = product.image_Product
        self.name_product = product.name_Product
        self.ui.pushButton.clicked.connect(self.edit_product)

    @Slot()
    def edit_product(self):
        p = Product()
        p.id_Product = self.id_product
        p.name_Product = self.name_product
        p.image_Product = self.image_Product
        edit_p = ProductEditWidget(p)
        edit_p.exec()
        print(self.id_product)


if __name__ == '__main__':
    app = QApplication()
    p = Product()
    p.id_Product = 1
    p.name_Product = "test"
    window = ItemProductEditWidget(p)
    window.show()
    sys.exit(app.exec())
