# Fruit recognition using 3 different CNN architectures

## Work in progress...

* I'm using the fruits-360 dataset from kaggle. Currently considering deleting all different variations of the same fruit from the dataset. For example there are like 10 different apples. It makes the models perform better, it reduces the training time and makes it easier for the human eye to tell if the predictions are correct.
* I'm building 3 different CNN models to compare their performances
* I'm using using a base and freezing the base layers when training the models.
* Models are saved elsewhere because they are usually too big for github. >100MB
* Models I'm currently working on:
    * ResNet50V2
    * VGG16
    * MobileNetV2