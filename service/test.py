import os

from keras.backend import expand_dims
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv2
import keras.utils
import tensorflow as tf
from tensorflow.python.ops import nn
from helpers.plotsHelper import visualize_CNN_model

import imageService

path = '../modelData/data/testimage/banana/img_1.png'



model = 0

pathmodel = os.path.dirname(__file__) + '..\\..\\modelData\\resultModelCNN\\saved_model.h5'

if __name__ == '__main__':

    imageArray = imageService.imagePathToArray(path)
    load_model = imageService.loadModel(pathmodel)

    # print(imageService.whoIsImage(imageArray, categories))
    # print(model)

# print("True label:", sample_label)
