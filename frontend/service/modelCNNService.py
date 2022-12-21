from PySide6.QtCore import QObject, Signal, QThread

from backend.service.imageService import imagePathToArray, whoIsImage
from frontend.model.product import Product
from frontend.controller.modelCNNController import ModelCNNController

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
        self.product = Product
        self.image = ''

    finished = Signal()  # QtCore.Signal

    def add_path(self, image):
        self.image = image

    def run(self):
        m = ModelCNNController()
        p = imagePathToArray(imagePath=self.image)
        who = whoIsImage(p, categories)
        print(who)
        self.result = who
        self.signals.finished.emit()
        # return who
        # print('Done sleeping')
