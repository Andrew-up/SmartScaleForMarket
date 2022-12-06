import os
import random

from keras.models import load_model
from keras.utils import load_img, img_to_array
import tensorflow as tf
import numpy as np
from heapq import nlargest

model = 0

categories = {
    0: "apple",
    1: "banana",
    2: "potato"
}


def imageToArray(image):
    pass


def getRandomImage():
    firstpath = os.path.dirname(__file__) +'\\..\\modelData/data/testimage/'
    # print(os.listdir(firstpath))
    twopatch = firstpath + '/' + os.path.join(random.choice(os.listdir(firstpath))) + '/'
    imagePath = os.path.join(twopatch, random.choice(os.listdir(twopatch)))
    return imagePath


def imagePathToArray(imagePath):
    img = load_img(imagePath, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    return img_array


def whoIsImage(imageArray, categories):
    predictions = model.predict(imageArray)
    a = 0
    zzzz = []
    for i in (predictions[0]):
        zzzz += [(categories[a], round(i * 100, 3))]
        a += 1

    zzzz = (sorted(zzzz, key=lambda x: (x[1]), reverse=True)[:2])
    return zzzz


def loadModel(pathModel):
    global model
    if model == 0:
        model = load_model(pathModel)
        print("test")
    pass
