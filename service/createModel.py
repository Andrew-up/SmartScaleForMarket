import keras.optimizers
from keras.utils import image_dataset_from_directory
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras import layers

import numpy as np
import tensorflow as tf
from helpers.plotsHelper import plot_history, visualize_CNN_model
from helpers.tfHelpers import setLimitGPU

train_path = '../modelData/data/train'
valid_path = '../modelData/data/test'
test_path = '../modelData/data/testimage'
cats_path = '../modelData/data/cats'
path_model = '../modelData/resultModelCNN/'
name_saved_model = 'saved_model.h5'


def build_image_generator():
    batch_size = 32
    img_height = 224
    img_width = 224

    train_dataset = image_dataset_from_directory(train_path,
                                                 labels='inferred',
                                                 label_mode='categorical',
                                                 subset='training',
                                                 validation_split=0.25,
                                                 batch_size=batch_size,
                                                 seed=123,
                                                 image_size=(img_height, img_width))

    validation_dataset = image_dataset_from_directory(train_path,
                                                      labels='inferred',
                                                      label_mode='categorical',
                                                      subset='validation',
                                                      validation_split=0.25,
                                                      batch_size=batch_size,
                                                      seed=123,
                                                      image_size=(img_height, img_width))

    test_dataset = image_dataset_from_directory(test_path,
                                                labels='inferred',
                                                label_mode='categorical',
                                                batch_size=batch_size,
                                                seed=123,
                                                image_size=(img_height, img_width))

    # len_train_dataset = len(np.concatenate([i for x, i in train_dataset], axis=0))

    data_augmentation = tf.keras.Sequential([
        # layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.3),
        layers.RandomContrast(factor=0.2),
        layers.Rescaling(1. / 255),
        layers.Resizing(img_height, img_width),

    ])

    # data_iterator = train_dataset.as_numpy_iterator()
    # batch = data_iterator.next()
    # print(batch[0])
    # one_images_batch = 0
    # for batch_x, batch_y in train_dataset:
    #     one_images_batch = batch_x[0].numpy().astype("uint8")
    #
    # plt.imshow(one_images_batch)
    # plt.show()

    # print(one_images_batch)

    # plt.figure(figsize=(10, 10))
    # plt.imshow(batch[0].numpy().astype("uint8"))
    # plt.imshow(images2[0].numpy().astype("uint8"))
    # plt.show()

    class_names = train_dataset.class_names
    # plt.figure(figsize=(10, 10))
    # for images, labels in train_dataset.take(1):
    #     for i in range(len_train_dataset):
    #         ax = plt.subplot(6, 6, i + 1)
    #         plt.imshow(data_augmentation(images[i].numpy().astype("uint8")))
    #         plt.title(class_names[np.argmax(labels[i])])
    #         plt.axis("off")

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
                                                         patience=7)

    callback_val_accuracy = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy",
                                                             mode="auto",
                                                             patience=7)

    history = model.fit(train_dataset,
                        batch_size=32,
                        epochs=50,
                        verbose=2,
                        validation_data=validation_dataset,
                        callbacks=[callback_val_loss, callback_val_accuracy],
                        )

    plot_history(history)
    print(model.summary())

    model.save(path_model + name_saved_model)

    # visualize_CNN_model(6, path_model + name_saved_model, class_names, train_dataset)

    test_evaluate = model.evaluate(test_dataset)
    print(test_evaluate)

    return 0


def main():
    setLimitGPU(1024)
    model = build_image_generator()


if __name__ == '__main__':
    main()