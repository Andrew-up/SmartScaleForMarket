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
        self.disabled_buttons()
    def disabled_buttons(self):
        self.ui.add_new_product_button.setDisabled(True)
        self.ui.clear_all_product_button.setDisabled(True)

    def update_list_product(self):
        for i in reversed(range(self.ui.list_item_widget.count())):
            self.ui.list_item_widget.itemAt(i).widget().deleteLater()
        controller = ProductController(Product(), self)
        list_product = controller.all_products()
        for a in list_product:
            item = ItemProductEditWidget(a)
            self.ui.list_item_widget.addWidget(item)


if __name__ == '__main__':
    app = QApplication()
    window = EditProductWidget()
    window.show()
    sys.exit(app.exec())
