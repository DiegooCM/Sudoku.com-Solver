import tensorflow as tf
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

model = tf.keras.models.load_model('model3.keras')

img = cv2.imread(f'squares/square5.png')[:,:,0]

img = np.invert(np.array([img]))
prediction = model.predict(img)

number_s = np.argmax(prediction)

print(prediction)
print(number_s)