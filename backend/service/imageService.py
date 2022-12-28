import base64
import os
import random
from io import BytesIO

from PySide6.QtCore import QByteArray, QIODevice, QBuffer
from PySide6.QtGui import QImage
from keras.models import load_model
from keras.utils import load_img, img_to_array
import tensorflow as tf
from definitions import TEST_PATH, TRAIN_PATH, MODEL_CNN_PATH
from backend.service.productService import findAllCategories

model = 0
pathModel = MODEL_CNN_PATH

categories = {}


def get_image_base64(image_path):
    with open(str(image_path), "rb") as img_file:
        image = QImage(img_file.name)
        image = image.scaledToWidth(224)
        image = image.scaledToHeight(224)
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        base64_data = ba.toBase64().data()
        string_utf_8 = base64_data.decode('utf-8')
        return string_utf_8

def imageToArray(image):
    pass


def getRandomImagePath():
    twopatch = TEST_PATH + '/' + os.path.join(random.choice(os.listdir(TEST_PATH))) + '/'
    imagePath = os.path.join(twopatch, random.choice(os.listdir(twopatch)))
    return imagePath


def imagePathToArray(imagePath):
    img = load_img(imagePath, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    return img_array

def whoIsImageBase64(imageBase64):
    img = load_img(BytesIO(base64.b64decode(imageBase64)), target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    loadModel()
    zzz = whoIsImage(img_array, categories)
    return zzz


def whoIsImage(imageArray, categories):
    predictions = model.predict(imageArray)
    a = 0
    zzzz = []
    for i in (predictions[0]):
        zzzz += [(categories[a], round(i * 100, 3))]
        a += 1
    print(len(zzzz))
    zzzz = (sorted(zzzz, key=lambda x: (x[1]), reverse=True)[:2])
    return zzzz


def loadModel():
    global categories
    categories = findAllCategories()
    global model
    if model == 0:
        model = load_model(pathModel)
        return "Ok"
        # print("test")
    pass
