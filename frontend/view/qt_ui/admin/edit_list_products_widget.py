import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.edit_product import Ui_edit_product_widget
from frontend.view.qt_ui.admin.item_product_widget_edit import ItemProductEditWidget
from frontend.controller.productController import ProductController
from frontend.model.product import Product


class EditProductWidget(QWidget):

    def __init__(self, parent=None):
        super(EditProductWidget, self).__init__(parent)
        self.ui = Ui_edit_product_widget()
        self.ui.setupUi(self)
        self.ui.update_list_widget_button.clicked.connect(self.update_list_product)

    def update_list_product(self):
        for i in reversed(range(self.ui.list_item_widget.count())):
            self.ui.list_item_widget.itemAt(i).widget().deleteLater()
        controller = ProductController(Product(), self)
        list_product = controller.all_products()
        for a in list_product:
            item = ItemProductEditWidget(a.id_Product)
            item.ui.pushButton.clicked.connect(self.opens)
            item.ui.id_product_label.setText(str(a.id_Product))
            item.ui.name_product_label.setText(a.name_Product)
            self.ui.list_item_widget.addWidget(item)

    def opens(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    window = EditProductWidget()
    window.show()
    sys.exit(app.exec())
