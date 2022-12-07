import keras.optimizers
from keras.utils import image_dataset_from_directory
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras import layers
import os
import numpy as np
import tensorflow as tf
from helpers.plotsHelper import plot_history, visualize_CNN_model
from helpers.tfHelpers import setLimitGPU
from definitions import TRAIN_PATH, TEST_PATH, MODEL_CNN_PATH

def build_image_generator():
    batch_size = 32
    img_height = 224
    img_width = 224

    train_dataset = image_dataset_from_directory(TRAIN_PATH,
                                                 labels='inferred',
                                                 label_mode='categorical',
                                                 subset='training',
                                                 validation_split=0.25,
                                                 batch_size=batch_size,
                                                 seed=123,
                                                 image_size=(img_height, img_width))

    validation_dataset = image_dataset_from_directory(TRAIN_PATH,
                                                      labels='inferred',
                                                      label_mode='categorical',
                                                      subset='validation',
                                                      validation_split=0.25,
                                                      batch_size=batch_size,
                                                      seed=123,
                                                      image_size=(img_height, img_width))

    test_dataset = image_dataset_from_directory(TEST_PATH,
                                                labels='inferred',
                                                label_mode='categorical',
                                                batch_size=batch_size,
                                                seed=123,
                                                image_size=(img_height, img_width))
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.3),
        layers.RandomContrast(factor=0.2),
        layers.Rescaling(1. / 255),
        layers.Resizing(img_height, img_width),

    ])

    model = Sequential()
    model.add(data_augmentation)
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.35))
    model.add(Dense(3, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    callback_val_loss = tf.keras.callbacks.EarlyStopping(monitor="val_loss",
                                                         mode="auto",
                                                         patience=10)

    callback_val_accuracy = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy",
                                                             mode="auto",
                                                             patience=10)

    history = model.fit(train_dataset,
                        batch_size=32,
                        epochs=50,
                        verbose=2,
                        validation_data=validation_dataset,
                        callbacks=[callback_val_loss, callback_val_accuracy],
                        )

    plot_history(history)
    print(model.summary())

    model.save(MODEL_CNN_PATH)

    # visualize_CNN_model(6, path_model + name_saved_model, class_names, train_dataset)

    test_evaluate = model.evaluate(test_dataset)
    print(test_evaluate)

    return 0


def main():
    setLimitGPU(1024)
    model = build_image_generator()



if __name__ == '__main__':
    main()
