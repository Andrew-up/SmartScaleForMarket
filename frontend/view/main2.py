import sys
import time

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QScrollArea, QFrame, QHBoxLayout, QWidget, \
    QDialog, QVBoxLayout, QLineEdit
from PySide6.QtCore import Slot, Signal, QRunnable, QThreadPool, QObject, QTimer, QThread

from frontend.view.qt_ui.new.mainwindow import Ui_MainWindow
from frontend.view.qt_ui.formwidget import ProductWidget
from frontend.view.qt_ui.search_by_number_widget import SearchByNumberWidget
from frontend.view.qt_ui.search_by_name import SearchByNameWidget
import sys
import time
import traceback
from frontend.service.imageService import path_to_pixmap
from backend.service.imageService import whoIsImage, imagePathToArray, categories

from frontend.model.CNNModel import CNNModel
# from backend.service import imageService
from frontend.service import imageService


# from threading import Thread

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QThread):
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.value = 0
        self.signals = WorkerSignals()
        self.model = 0

    finished = Signal()  # QtCore.Signal

    def run(self):
        # while self.value < 10:
        #     self.value = self.value + 1
        #     print(self.value)
        #     time.sleep(0.1)
        cnn_model = CNNModel()
        cnn_model.loadModel()
        # model = CNNModel.loadModel()
        self.signals.finished.emit()
        # print('Done sleeping')


class ModelPredict(QThread):
    def __init__(self, parent=None):
        super(ModelPredict, self).__init__(parent)
        self.signals = WorkerSignals()
        self.image = ""
        self.result = ''
    finished = Signal()  # QtCore.Signal

    def add_path(self, image):
        self.image = image

    def run(self):
        p = imagePathToArray(imagePath=self.image)
        who = whoIsImage(p, categories)
        print(who)
        self.result = who
        self.signals.finished.emit()
        # return who
        # print('Done sleeping')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_widget.clicked.connect(self.add)
        self.count: int = 0
        self.ui.button_search_by_number.clicked.connect(self.open_form_search_by_number)
        self.ui.button_search_by_name.clicked.connect(self.open_search_by_name_widget)
        self.form_search_by_number = SearchByNumberWidget()
        self.form_search_by_name = SearchByNameWidget()
        # self.ui.button_YES_product.setText("START\nпоток")
        # self.ui.button_NO_product.setText("STOP\nпоток")
        # self.ui.button_YES_product.clicked.connect(self.start_th)
        # self.ui.button_NO_product.clicked.connect(self.stop_th)
        self.ui.getRandomImageButton.clicked.connect(self.add_image)
        self.worker = Worker()
        self.worker.signals.finished.connect(self.stop_th)
        self.start_th()
        self.ui.getRandomImageButton.setDisabled(True)
        self.model_predict_obj = ModelPredict()
        self.model_predict_obj.signals.finished.connect(self.stop_model_predict_obj)

    def random_image(self):
        image = imageService.get_random_image_path()
        print(image)
        self.model_predict_obj.add_path(image)
        self.model_predict_obj.start()
        self.ui.getRandomImageButton.setDisabled(True)
        self.ui.label_who_is_product.setText("Идет распознавание товара...")
        return image

    def add_image(self):
        pixmap = path_to_pixmap(self.random_image())
        self.ui.image_to_cnn.setPixmap(pixmap)
        self.ui.image_to_cnn.setScaledContents(True)

    def stop_model_predict_obj(self):
        self.model_predict_obj.quit()
        print("поток model_predict_obj остановлен")
        string = ''
        for a in self.model_predict_obj.result:
            string += a[0] + ' ' + str(a[1]) + '% \n'
        self.ui.label_who_is_product.setText(string)
        self.ui.getRandomImageButton.setDisabled(False)
    def start_th(self):
        self.worker.start()
        self.ui.label_who_is_product.setText("Идёт загрузка модели CNN...")
        # self.model_predict_obj.quit()
        print("start_th")

    def stop_th(self):
        # self.worker
        print("stop_th")
        self.ui.label_who_is_product.setText("Модель загружена.")
        self.ui.getRandomImageButton.setEnabled(True)

    # @Slot
    def open_form_search_by_number(self):
        self.form_search_by_number.setModal(True)
        self.form_search_by_number.exec()

    def open_search_by_name_widget(self):
        self.form_search_by_name.setModal(True)
        self.form_search_by_name.exec()

    @Slot()
    def add(self):
        self.count += 1
        formwidget = ProductWidget(self.count)
        self.ui.product_List_Layout.addWidget(formwidget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def startApp():
    # pass
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())