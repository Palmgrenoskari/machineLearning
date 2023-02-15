# Just some callbacks testing 

from tensorflow import keras
from tensorflow.keras import layers, callbacks
import pandas as pd

# Copypaste from box1.py

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

# Creating the callbacks
early_stopping = callbacks.EarlyStopping(
    min_delta=0.001, # minimum amount of change to count as improvement during the training
    patience=20, # how many epochs we wait before stopping
    restore_best_weights=True # when we stop, we go back to the best score (= lowest loss)
)

# Our model of choice
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)
])

# Compiling
model.compile(
    optimizer='adam',
    loss='mae'
)

# Training
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=500,
    callbacks=[early_stopping] 
)

# Plotting to visualize the moment of stop.
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot() # Choosing all rows from columns: 'loss' and 'val_loss' and then plotting.

