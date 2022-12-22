from PySide6.QtCore import QObject, Signal, QThread

from frontend.controller.modelCNNController import ModelCNNController
from frontend.model.product import Product

categories = {}


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class ModelPredict(QThread):
    def __init__(self, parent=None):
        super(ModelPredict, self).__init__(parent)
        self.signals = WorkerSignals()
        self.result = ''
        self.product = Product()
        self.image_base64 = ''

    finished = Signal()  # QtCore.Signal

    def add_image_base64(self, image):
        self.image_base64 = image

    def predict_product(self, imageBase64):
        self.image_base64 = imageBase64

    def run(self):
        print(f"Поток {self.objectName()} запущен ")
        con = ModelCNNController().image_predict_from_image_base64(self.image_base64)
        # print(con)
        self.result = con
        self.signals.finished.emit()
        print(f"поток {self.objectName()} остановлен")

class LoadModel(QThread):
    def __init__(self, parent=None):
        super(LoadModel, self).__init__(parent)
        self.signals = WorkerSignals()

    def run(self):
        cnn_model = ModelCNNController()
        cnn_model.loadModel()
        self.signals.finished.emit()
