import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog, QFileDialog
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.edit_product_widget import Ui_Form
from frontend.model.product import Product
from frontend.controller.productController import ProductController
from frontend.service.imageService import base64_to_pixmap
import base64

class ProductEditWidget(QDialog):

    def __init__(self, product: Product, parent=None):
        super(ProductEditWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id_product = product.id_Product
        self.image_Product = product.image_Product
        self.ui.label_2.setText(str(self.id_product))
        self.ui.textEdit.setText(product.name_Product)
        self.ui.pushButton.clicked.connect(self.saveProduct)
        self.new_image_blob = 0
        # print(product.image_Product)
        # Добавить изображение
        pixmap = base64_to_pixmap(product.image_Product)
        self.ui.label_5.setPixmap(pixmap)
        self.ui.label_5.setScaledContents(True)
        self.ui.pushButton_5.clicked.connect(self.open_new_image)

    def open_new_image(self):
        fileName = QFileDialog.getOpenFileName(self, ("Open Image"), "C:", ("Image Files (*.png *.jpg)"))
        print(fileName)
        with open(fileName[0], "rb") as image_file:
            self.new_image_blob = base64.b64encode(image_file.read())
            # print(self.new_image_blob)
            pixmap = base64_to_pixmap(self.new_image_blob)
            self.ui.label_5.setPixmap(pixmap)
            self.ui.label_5.setScaledContents(True)

    def saveProduct(self):
        controller = ProductController(Product(), self)
        new_Product = Product()
        new_Product.name_Product = self.ui.textEdit.toPlainText()
        new_Product.image_Product = self.new_image_blob
        edit = controller.edit_product(self.id_product, new_Product=new_Product)

        print(edit)
        print("Сохранение")


if __name__ == '__main__':
    app = QApplication()
    c = ProductController(Product(), 0)
    get = c.get_Product_by_id(1)
    window = ProductEditWidget(get)
    window.show()
    sys.exit(app.exec())
