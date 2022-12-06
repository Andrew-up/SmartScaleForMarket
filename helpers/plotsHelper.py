import math

import matplotlib.pyplot as plt
import numpy as np
from keras.models import Model, load_model
import tensorflow as tf
from keras.utils import img_to_array


def plot_images(images, labels=None, class_names=None, one_hot_label=False):
    num_images = len(images)
    num_cols = 8
    num_rows = math.ceil(num_images / num_cols)
    plt.figure(figsize=(num_cols * 2, num_rows * 2))
    for i, image in enumerate(images):
        plt.subplot(num_rows, num_cols, i + 1)
        plt.imshow(image)
        if labels is not None:
            label = labels[i]
            if one_hot_label:
                label = np.argmax(label)
            if class_names is not None:
                label = class_names[label]
            plt.title(label)
        plt.axis('off')
    plt.show()


def plot_history(history, metrics=None, start=0):
    if metrics is None:
        metrics = [('accuracy', 'val_accuracy'), ('loss', 'val_loss')]
    elif isinstance(metrics, str):
        metrics = [(metrics,)]

    num_metrics = len(metrics)
    plt.figure(figsize=(6 * num_metrics, 4))
    for i, group in enumerate(metrics):
        if isinstance(group, str):
            group = (group,)
        plt.subplot(1, num_metrics, i + 1)
        for key in group:
            epochs = range(len(history.history[key][start:]))
            plt.plot(epochs, history.history[key][start:], label=key)
        plt.legend()
    plt.show()


def visualize_CNN_model(CNNLayer, pathModel, class_names, dataset):
    model = load_model(pathModel)
    activation_model = Model(inputs=model.input, outputs=model.layers[CNNLayer].output)
    activation_model.summary()
    one_images_batch = 0
    images_title = ''
    len_train_dataset = len(np.concatenate([i for x, i in dataset], axis=0))

    for i in range(len_train_dataset):
        for batch_x, batch_y in dataset:
            one_images_batch = batch_x[i].numpy().astype("uint8")
            images_title = class_names[np.argmax(batch_y[i])], 100 * np.max(batch_y[i])

        img_array = img_to_array(one_images_batch, data_format='channels_last')
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        activation = activation_model.predict(img_array)

        images_per_row = 16
        n_filters = activation.shape[-1]
        size = activation.shape[1]
        n_cols = n_filters // images_per_row
        display_grid = np.zeros((n_cols * size, images_per_row * size))

        for col in range(n_cols):
            for row in range(images_per_row):
                channel_image = activation[0, :, :, col * images_per_row + row]
                channel_image -= channel_image.mean()
                channel_image /= channel_image.std()
                # print(channel_image)
                channel_image *= 64
                channel_image += 128
                channel_image = np.clip(channel_image, 0, 255).astype('uint8')
                display_grid[col * size: (col + 1) * size, row * size: (row + 1) * size] = channel_image

        scale = 1. / size
        plt.figure(figsize=(scale * display_grid.shape[1], scale * display_grid.shape[0]))
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
        # print(f"{images_title[0]} {images_title[1]:.3f} % ")
        plt.title(f'CNN Layer: {CNNLayer}, id image: '+str(i) + ' : ' + f" {images_title[0]}", fontdict={'fontsize': 50})
        # plt.imshow(one_images_batch)
        plt.show()
    # pass
