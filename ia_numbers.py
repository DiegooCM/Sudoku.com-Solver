import tensorflow as tf
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

#1296

#Hay que cambiar las capas del modelo para que den 1296
class numbers_ia:

    def __init__(self):
        self.model_name = 'model1.keras'

    def create_model(self):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))# Se puede poner lo que sea en el str, Relu = rectify linear unit
        model.add(tf.keras.layers.Dense(128, activation= 'relu'))
        model.add(tf.keras.layers.Dense(10, activation='softmax')) #9 por los 9 números, esto es el 'output'. Investigar acerca del activation

        model.compile(optimizer= 'adam', loss= 'sparse_categorical_crossentropy', metrics = ['accuracy'])#Lo compilamos

        model.fit(x_train, y_train, epochs= 3) # Lo entrenamos

        model.save(self.model_name) 

    def predict_numbers(self):
        model = tf.keras.models.load_model(self.model_name)

        n = 0
        while os.path.isfile(f'squares/square{n}.png'):
            try:
                img = cv2.imread(f'squares/square{n}.png')[:,:,0]
                img = np.invert(np.array([img]))
                prediction = model.predict(img)
                print(f'Number is {np.argmax(prediction)}')
                plt.imshow(img[0], cmap= plt.cm.binary)
                plt.show()
            except:
                print('ERRORRRR!')
            finally:
                n += 1
                break



nia = numbers_ia()

nia.predict_numbers()