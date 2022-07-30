import numpy as np
import pandas as pd
import tensorflow
import create_dataset
from tensorflow import keras
if __name__ == "__main__" :
    x_train, y_train, x_test, y_test =create_dataset.load_dataset() 
