import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.recognition_widget_cnn import Ui_productListWidget


class ProductWidget(QWidget):
    delete = Signal(int)

    def __init__(self, idWidget: int, parent=None):
        super(ProductWidget, self).__init__(parent)
        self.ui = Ui_productListWidget()
        self.ui.setupUi(self)
        self.ui.label_name_product.setText(str(idWidget))
        # self.id_wigdet = id_wigdet


if __name__ == '__main__':
    app = QApplication()
    window = ProductWidget(1)
    window.show()
    sys.exit(app.exec())
