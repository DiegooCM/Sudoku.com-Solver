import tensorflow as tf
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Probar en algun momento a entrenar la ia con casillas del sudoku

# Poner los cuadrados en greyscale, si sigue sin funcionar hacer algo para los cuadrados blancos y que el modelo solo analice los numeros
class numbers_ia:

    def __init__(self):
        self.model_name = 'model2.keras'

    def create_model(self):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))# Se puede poner lo que sea en el str, Relu = rectify linear unit
        model.add(tf.keras.layers.Dense(128, activation= 'relu'))
        model.add(tf.keras.layers.Dense(10, activation='softmax')) #10 por los 10 números(0-9), esto es el 'output'. Hay que poner esto debido a los 10 numeros con los que entrenamos a la ia(mnist). Investigar acerca del activation

        model.compile(optimizer= 'adam', loss= 'sparse_categorical_crossentropy', metrics = ['accuracy'])#Lo compilamos

        model.fit(x_train, y_train, epochs= 10) # Lo entrenamos

        model.save(self.model_name) 

    def predict_numbers(self):
        model = tf.keras.models.load_model(self.model_name)
        self.matrix = []

        n = 0
        while os.path.isfile(f'squares/square{n}.png'):
            try:
                img = cv2.imread(f'squares/square{n}.png')[:,:,0]
                img = np.invert(np.array([img]))
                prediction = model.predict(img)

                number_s = np.where(prediction[0] == 1.)[0]
                
                # Si está vacío devuelve un 0 y si no el número
                if len(number_s) != 0:
                    self.matrix.append(int(number_s))
                else:
                    self.matrix.append(None)
                
            except:
                print('ERROR')
                break
            finally:
                n += 1

    def create_matrix(self):
        ar2 = []

        matrix = []
        n = 0

        for item in self.matrix:
            ar2.append(item)
            n+=1  
            if n== 9:
                n= 0
                matrix.append(ar2)
                ar2 = []
              
        
        self.matrix = matrix

        print(self.matrix)


nia = numbers_ia()

nia.create_model()
nia.predict_numbers()
nia.create_matrix()