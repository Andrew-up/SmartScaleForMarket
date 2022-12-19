import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Slot, Signal

from frontend.view.qt_ui.new.keyboard_widget import Ui_Form


class KeyBoardWidget(QWidget):

    def __init__(self, parent=None):
        super(KeyBoardWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = KeyBoardWidget()
    window.show()
    sys.exit(app.exec())
