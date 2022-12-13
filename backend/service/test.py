import os

import imageService

path = '../models_cnn/data/testimage/banana/img_1.png'

model = 0

pathmodel = os.path.dirname(__file__) + '..\\..\\modelDataCNN\\resultModelCNN\\saved_model.h5'

if __name__ == '__main__':

    imageArray = imageService.imagePathToArray(path)
    load_model = imageService.loadModel(pathmodel)

    # print(imageService.whoIsImage(imageArray, categories))
    # print(model)

# print("True label:", sample_label)
