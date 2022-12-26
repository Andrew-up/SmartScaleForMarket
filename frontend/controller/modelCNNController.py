from backend.service import imageService
from backend.service.imageService import whoIsImageBase64



class ModelCNNController:

    def __init__(self, parent=None):
        super(ModelCNNController, self).__init__()
        self.resultWorkCNN = ''

    def image_predict_from_image_base64(self, image_base64):
        who = whoIsImageBase64(image_base64)
        return who

    def loadModel(self):
        model = imageService.loadModel()
        return model


if __name__ == '__main__':
    m = ModelCNNController()
