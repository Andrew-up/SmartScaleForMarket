import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.recognition_widget_cnn import Ui_productListWidget
from frontend.model.product import Product
from frontend.service.imageService import ImageService
class ProductWidget(QWidget):
    def __init__(self, product: Product(), parent=None):
        super(ProductWidget, self).__init__(parent)
        self.ui = Ui_productListWidget()
        self.ui.setupUi(self)
        self.product = product
        self.fill_card()
        self.ui.label_name_product.clicked.connect(self.on_click_item)

    def on_click_item(self):
        print("test")
    def fill_card(self):
        self.ui.label_name_product.setText(self.product.name_Product)
        if self.product.image_Product != 0:
            # print(self.product.image_Product)
            pixmap = ImageService().base64_to_pixmap(self.product.image_Product)
            self.ui.label_image_product.setPixmap(pixmap)
            self.ui.label_image_product.setScaledContents(True)
        # self.ui.label_name_product.setText(str(idWidget))
        # self.id_wigdet = id_wigdet




if __name__ == '__main__':
    app = QApplication()
    p = Product()
    p.id_Product = 1
    p.name_Product = "Яблоко"
    window = ProductWidget(p)
    window.show()
    sys.exit(app.exec())
