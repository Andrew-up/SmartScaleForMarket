import os.path

import keras.optimizers
import tensorflow as tf
from keras import layers
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential
from keras.utils import image_dataset_from_directory

from backend.helpers.plotsHelper import plot_history
from backend.helpers.tfHelpers import setLimitGPU
from backend.model.product import Product
from backend.service.imageService import get_image_base64
from backend.service.productService import addProduct, getProductByLabel, getLastProduct
from definitions import TRAIN_PATH, TEST_PATH, MODEL_CNN_PATH, LABELS_IMAGE

name_labels_to_ru = {
    'potato': 'Картофель',
    'apple': 'Яблоко',
    'background': 'Задний фон',
    'banana': 'Банан'
}



def build_image_generator():
    batch_size = 8
    img_height = 224
    img_width = 224

    train_dataset = image_dataset_from_directory(TRAIN_PATH,
                                                 labels='inferred',
                                                 label_mode='categorical',
                                                 subset='training',
                                                 validation_split=0.3,
                                                 batch_size=batch_size,
                                                 seed=12,
                                                 image_size=(img_height, img_width))

    validation_dataset = image_dataset_from_directory(TRAIN_PATH,
                                                      labels='inferred',
                                                      label_mode='categorical',
                                                      subset='validation',
                                                      validation_split=0.3,
                                                      batch_size=batch_size,
                                                      seed=12,
                                                      image_size=(img_height, img_width))

    test_dataset = image_dataset_from_directory(TEST_PATH,
                                                labels='inferred',
                                                label_mode='categorical',
                                                batch_size=batch_size,
                                                seed=12,
                                                image_size=(img_height, img_width))

    len_class_dataset = len(train_dataset.class_names)

    data_augmentation = tf.keras.Sequential([
        # layers.RandomFlip("horizontal"),
        # layers.RandomRotation(0.15),
        # layers.RandomContrast(factor=0.1),
        layers.Resizing(img_height, img_width),
        # layers.CenterCrop(img_height, img_width),
        layers.Rescaling(1. / 255),
    ])

    # len_train_dataset = len(np.concatenate([i for x, i in train_dataset], axis=0))
    # id_labels: int = 0
    # product_list = list(Product)

    for data in train_dataset.class_names:
        is_true = getProductByLabel(data)
        last_prod = getLastProduct()
        id_labels = 0
        if last_prod is not None:
            id_labels = last_prod.categorical_id
            id_labels += 1
        if last_prod is None:
            id_labels = 0
        path = LABELS_IMAGE + '/' + data + '.jpg'
        exist = os.path.exists(path)
        name = name_labels_to_ru[data]
        print(name)
        if is_true is None:
            product = Product()
            product.set_categorical_id(id_labels)
            product.set_categorical_name(str(data))
            if exist:
                image_array = get_image_base64(path)
                # print(image_array)
                product.set_image_Product(image_array.encode())
                product.set_name_Product(str(name))

            p = addProduct(product)

            # print(data)
            print(product)

    # add = addProducts(product_list)
    # print(add)

    # class_names = train_dataset.class_names
    # plt.figure(figsize=(10, 10))
    # for images, labels in train_dataset.take(1):
    #     for i in range(len_train_dataset):
    #         ax = plt.subplot(6, 6, i + 1)
    #         plt.imshow(data_augmentation(images[i].numpy().astype("uint8")))
    #         plt.title(class_names[np.argmax(labels[i])])
    #         plt.axis("off")
    # plt.show()

    model = Sequential()
    model.add(data_augmentation)
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    # model.add(Dropout(0.1))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.1))
    model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.35))
    model.add(Dense(len_class_dataset, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  # optimizer=keras.optimizers.Adam(),
                  optimizer=keras.optimizers.Adam(0.0002),
                  metrics=['accuracy'])

    callback_val_loss = tf.keras.callbacks.EarlyStopping(monitor="val_loss",
                                                         mode="auto",
                                                         patience=20)

    callback_val_accuracy = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy",
                                                             mode="auto",
                                                             patience=20)

    history = model.fit(train_dataset,
                        batch_size=batch_size,
                        epochs=50,
                        verbose=2,
                        validation_data=validation_dataset,
                        callbacks=[callback_val_loss, callback_val_accuracy],
                        )

    plot_history(history)
    print("структура модели")
    print(model.summary())
    print("сохранение модели")
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
