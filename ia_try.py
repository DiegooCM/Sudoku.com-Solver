import tensorflow as tf
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
print('\n\n\n')

model = tf.keras.models.load_model('model1.keras')

img = cv2.imread(f'squares\square0.png')[:,:,0]
img = np.invert(np.array([img]))
prediction = model.predict(img)
print(f'Number is {np.argmax(prediction)}')
plt.imshow(img[0], cmap= plt.cm.binary)
plt.show()
