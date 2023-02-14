# Import keras from tensorflow
from tensorflow import keras
# Import layers from keras
from tensorflow.keras import layers

# Creating a network with 1 linear unit

## Units define how many outputs we want
## input_shape tells the dimensions of inputs. Here we have 3 inputs.

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])

