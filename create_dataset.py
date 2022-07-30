import pandas as pd
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist

def load_dataset():
    (x_train, y_train),(x_test,y_test)=mnist.load_data()
    print(x_train.shape)
    return x_train, y_train, x_test, y_test
