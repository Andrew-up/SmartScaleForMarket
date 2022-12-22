import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from frontend.controller.productController import ProductController
from frontend.model.product import Product
from frontend.service.imageService import ImageService
from frontend.service.modelCNNService import categories, ModelPredict, LoadModel
from frontend.view.qt_ui.formwidget import ProductWidget
from frontend.view.qt_ui.new.mainwindow import Ui_MainWindow
from frontend.view.qt_ui.search_by_name import SearchByNameWidget
from frontend.view.qt_ui.search_by_number_widget import SearchByNumberWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.count: int = 0
        self.ui.button_search_by_number.clicked.connect(self.open_form_search_by_number)
        self.ui.button_search_by_name.clicked.connect(self.open_search_by_name_widget)
        self.form_search_by_number = SearchByNumberWidget()
        self.form_search_by_name = SearchByNameWidget()
        self.ui.getRandomImageButton.clicked.connect(self.add_image_to_label)
        self.load_model = LoadModel()
        self.load_model.signals.finished.connect(self.stop_th)
        self.start_th()
        self.ui.getRandomImageButton.setDisabled(True)
        self.model_predict_obj = ModelPredict()
        self.model_predict_obj.signals.finished.connect(self.stop_model_predict_obj)

        self.ui.button_YES_product.clicked.connect(self.click_yes_product)
        # p = ProductController(Product(), self)
        # for a in p.all_products():
        #     print(a.categorical_name)
        # categories[a.categorical_id] = a.categorical_name
        # print(categories)

    def click_yes_product(self):
        print("Печать чека для продукта")
        message = QMessageBox()
        message.setText(f"Продукт: {self.model_predict_obj.product.name_Product} \n "
                        f"id: {self.model_predict_obj.product.id_Product}\n"
                        f"категория: {self.model_predict_obj.product.categorical_name} \n")
        message.setWindowTitle("Печать чека")
        message.exec()

    def what_product(self, image):
        self.model_predict_obj.add_image_base64(image)
        self.model_predict_obj.setObjectName("IMAGE-PREDICT")
        self.model_predict_obj.start()
        self.ui.label_who_is_product.setText("Идет распознавание товара...")
        self.ui.getRandomImageButton.setDisabled(True)

    def add_image_to_label(self):
        image_service = ImageService()
        image_path = image_service.get_image_path()
        pixmap = image_service.path_to_pixmap(image_path)
        self.ui.image_to_cnn.setPixmap(pixmap)
        self.ui.image_to_cnn.setScaledContents(True)
        image_base64 = image_service.get_image_base64(image_path)
        print(image_base64)
        self.what_product(image_base64)

    def stop_model_predict_obj(self):
        for i in reversed(range(self.ui.product_List_Layout_2.count())):
            self.ui.product_List_Layout_2.itemAt(i).widget().deleteLater()
        string = ''
        for a in self.model_predict_obj.result:
            if float(a[1]) > float(90.0):
                self.count += 1
                c = ProductController(Product(), self)
                res = c.get_product_by_label(str(a[0]))
                string += a[0] + ' ' + str(a[1]) + '% \n'
                string += f"На весах {res.name_Product} ?"
                formwidget = ProductWidget(res)
                self.model_predict_obj.product = res
                self.ui.product_List_Layout_2.addWidget(formwidget)

        self.ui.label_who_is_product.setText(string)
        self.ui.getRandomImageButton.setDisabled(False)

    def start_th(self):
        self.load_model.start()
        self.load_model.setObjectName("LOAD_MODEL_THREAD")
        self.ui.label_who_is_product.setText("Идёт загрузка модели CNN...")
        print(f"Запущен поток: {self.load_model.objectName()}")

    def stop_th(self):
        # print("stop_th")
        self.ui.label_who_is_product.setText("Модель загружена.")
        self.ui.getRandomImageButton.setEnabled(True)
        print(f"Завершен поток: {self.load_model.objectName()}")

    # @Slot
    def open_form_search_by_number(self):
        self.form_search_by_number.setModal(True)
        self.form_search_by_number.exec()

    def open_search_by_name_widget(self):
        self.form_search_by_name.setModal(True)
        self.form_search_by_name.exec()


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
