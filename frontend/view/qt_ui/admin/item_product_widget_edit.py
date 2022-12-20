import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.item_product_widget_edit import Ui_Form
from frontend.view.qt_ui.admin.edit_product import ProductEditWidget
from frontend.model.product import Product
from frontend.service.imageService import base64_to_pixmap
from frontend.controller.productController import ProductController

class ItemProductEditWidget(QWidget):

    def __init__(self, product: Product, parent=None):
        super(ItemProductEditWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.product = product
        self.ui.pushButton.clicked.connect(self.edit_product)
        self.fill_product_cart()
        self.disabled_buttons()

    def disabled_buttons(self):
        self.ui.pushButton_2.setDisabled(True)

    def fill_product_cart(self):
        self.ui.id_product_label.setText(str(self.product.id_Product))
        self.ui.name_product_label.setText(self.product.name_Product)
        pixmap = base64_to_pixmap(self.product.image_Product)
        self.ui.image_product_label.setPixmap(pixmap)
        self.ui.image_product_label.setScaledContents(True)

    @Slot()
    def edit_product(self):
        product = self.product
        edit_p = ProductEditWidget(product)
        edit_p.exec()


if __name__ == '__main__':
    app = QApplication()
    controller = ProductController(Product(), ItemProductEditWidget)
    product = controller.get_Product_by_id(1)
    window = ItemProductEditWidget(product)
    window.show()
    sys.exit(app.exec())
