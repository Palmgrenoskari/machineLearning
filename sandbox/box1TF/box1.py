"""
Just making some own notes while learning in kaggle

Course: Intro to Deep Learning
"""

# Import keras from tensorflow
from tensorflow import keras
# Import layers from keras
from tensorflow.keras import layers

# Creating a network with 1 linear unit

## Units define how many outputs we want
## input_shape tells the dimensions of inputs. Here we have 3 inputs.

modelbasic = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])

# Network with:
# 2 inputs
# 2 hidden layers | 1st: 4 neurons, 2nd: 3 neurons | activation function = ReLU
# 1 output

model1 = keras.Sequential([
    # The hidden ReLU layers
    layers.Dense(units=4, activation="relu", input_shape=[2]),
    layers.Dense(units=3, activation="relu"),
    # The linear output layer
    layers.Dense(units=1)
])

# Action - Red Wine Quality
import pandas as pd

# Read csv
red_wine = pd.read_csv('C:/Users/Palmg/Desktop/machineLearning/sandbox/box1/red-wine.csv')

# Creating training and validation splits
df_train = red_wine.sample(frac=0.7, random_state=0)
df_valid = red_wine.drop(df_train.index)

# Scale to [0, 1] - Neat little trick
max = df_train.max(axis=0)
min = df_train.min(axis=0)
df_train = (df_train - min) / (max - min)
df_valid = (df_valid - min) / (max - min)

# Split features and target
X_train = df_train.drop('quality', axis=1)
X_valid = df_valid.drop('quality', axis=1)
y_train = df_train['quality']
y_valid = df_valid['quality']

# How many inputs should this network have?
print(X_train.shape) # (1119, 11) -> 11 inputs

# Let's go with roughly 1500 neurons and 3 layers

modelWines = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)
])

# Compile in adam-optimizer and loss function for the training

modelWines.compile(
    optimizer='adam',
    loss='mae'
)

# 256 rows of training data at a time and 12 epochs (12 times through the dataset)

training = modelWines.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size = 256,
    epochs = 12
)

# We could plot the loss with each iteration
import matplotlib
training_df = pd.DataFrame(training.history) # Training history into dataframe
training_df['loss'].plot()



