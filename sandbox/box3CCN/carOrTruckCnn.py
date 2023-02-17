# Part of kaggle's computer vision course. https://www.kaggle.com/learn/computer-vision

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Loading the data and pre-processing
dataset_train = image_dataset_from_directory(
    'C:/Users/Palmg/Desktop/machineLearning/sandbox/box3CCN/training_data/train',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=True
)

dataset_valid = image_dataset_from_directory(
    'C:/Users/Palmg/Desktop/machineLearning/sandbox/box3CCN/training_data/train',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

def convert_to_float(image, label):
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label

AUTOTUNE = tf.data.experimental.AUTOTUNE
dataset_training = (
    dataset_train
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)
dataset_validation = (
    dataset_valid
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)

# Building the model
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=5, activation="relu", padding="same", input_shape=[128,128,3]),
    layers.MaxPool2D(), 

    layers.Conv2D(filters=64, kernel_size=3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.Conv2D(filters=128, kernel_size=3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.Flatten(),
    layers.Dense(units=6, activation="relu"),
    layers.Dense(units=1, activation="sigmoid")
])

# Training

model.compile(
    optimizer=tf.keras.optimizers.Adam(epsilon=0.01),
    loss="binary_crossentropy",
    metrics=["binary_accuracy"]
)

history = model.fit(
    dataset_train,
    validation_data=dataset_valid,
    epochs=40
)

# Plotting the training progress

import pandas as pd

history_frames = pd.DataFrame(history.history)
history_frames.loc[:, ['loss', 'val_loss']].plot()