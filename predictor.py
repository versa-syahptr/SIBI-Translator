import tensorflow as tf
import numpy as np
import pandas as pd
import string

# Load the model
model = tf.keras.models.load_model('model.keras')

def predict(df : pd.DataFrame) -> str:
    res = model(np.array([df.values]))
    predicted = np.argmax(res)
    return string.ascii_uppercase[predicted]
    

    