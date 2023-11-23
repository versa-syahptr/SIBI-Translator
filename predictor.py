import tensorflow as tf
import numpy as np
import pandas as pd
import string

# Load the model
model = tf.keras.models.load_model('models/model-ann-flip.keras')

def predict(df : pd.DataFrame) -> str:
    res = model(np.array([df.values]))
    predicted = np.argmax(res)
    return string.ascii_uppercase[predicted]
    

def predict_with_conf(df : pd.DataFrame) -> str:
    res = model(np.array([df.values]))
    predicted = np.argmax(res)
    return string.ascii_uppercase[predicted], res[0][predicted]