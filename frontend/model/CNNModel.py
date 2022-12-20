from backend.service import imageService


class CNNModel:

    def loadModel(self):
        model = imageService.loadModel()
        return model

    def send_image_to_result_cnn(self, image):

        pass