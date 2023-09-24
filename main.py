import math
import numpy as np
import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import classification_report

import tensorflow as tf

# from tensorflow.python.keras import optimizers
# from tensorflow.python.keras.models import Sequential
# from tensorflow.python.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D
# from tensorflow.python.keras.layers import Dropout, BatchNormalization, LeakyReLU, Activation
# from tensorflow.python.keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# from keras.utils import np_utils


df = pd.read_csv(
    './datasets/fer2013.csv')
print(df.shape)  # (35887, 3)

df.head()
