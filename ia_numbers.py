import tensorflow as tf
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

#Probar en algun momento a entrenar la ia con casillas del sudoku

# Poner los cuadrados en greyscale, si sigue sin funcionar hacer algo para los cuadrados blancos y que el modelo solo analice los numeros
class numbers_ia:

    def __init__(self):
        self.model_name = 'model4.keras'


    def create_model(self):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))# Se puede poner lo que sea en el str, Relu = rectify linear unit
        model.add(tf.keras.layers.Dense(128, activation= tf.nn.relu))
        model.add(tf.keras.layers.Dense(units=10,activation='softmax')) #10 por los 10 números(0-9), esto es el 'output'. Hay que poner esto debido a los 10 numeros con los que entrenamos a la ia(mnist). Investigar acerca del activation

        model.compile(optimizer= 'adam', loss= 'sparse_categorical_crossentropy', metrics = ['accuracy'])#Lo compilamos

        model.fit(x_train, y_train, epochs= 3) # Lo entrenamos

        model.save(self.model_name) 
    
    def get_number_boxes(self):
        self.numbers_index = []

        for n in range(81):
            img = Image.open(f'squares/square{n}.png').convert('L')

            dark = 0
            new_imgdata = []

            for color in img.getdata():
                if color < 200:
                    new_imgdata.append(0)
                    dark +=1
                else:
                    new_imgdata.append(255)    

            new_img = Image.new(img.mode, img.size)
            new_img.putdata(new_imgdata)

            new_img.save(f'squares/square{n}.png')

            if dark>=1:
                self.numbers_index.append(n)

    def predict_numbers(self):
        model = tf.keras.models.load_model(self.model_name)
        self.numbers_matrix = []

        for n in self.numbers_index:

            try:
                img = cv2.imread(f'squares/square{n}.png')[:,:,0]
                img = np.invert(np.array([img]))
                prediction = model.predict(img)

                number_s = np.argmax(prediction)
                    
                self.numbers_matrix.append(int(number_s))
                    
            except:
                print(f'ERROR')
                break

            finally:
                n += 1

    def create_matrix(self):
        self.matrix_temp = []
        self.matrix = []
        ar2 = []
        n = 0

        for a in range(81):
            if a in self.numbers_index:
                self.matrix_temp.append(self.numbers_matrix[n])
                n += 1
            else:
                self.matrix_temp.append(None)

        n = 0

        for item in self.matrix_temp:
            ar2.append(item)
            n+=1  
            if n== 9:
                n= 0
                self.matrix.append(ar2)
                ar2 = []
              

        print(self.matrix)

    def accuracy_prediction_matrix(self):
        real_matrix = [[None,None,None,7,6,2,None,9,None],
               [None,None,None,3,8,None,None,2,7],
               [2,8,None, None,5,9,1,6,3],
               [None, None, None, None, None, None, 6, None, 1],
               [None, 1, 5, None, None, 3, 2, None, None],
               [6, None, None, None, 4, 5, 7, None , 8],
               [None, 2, None, 9, None, None, 4, None, 5],
               [None, 7, None, 8,2,4, None, None, None],
               [9, None, None, 5, None, 7, None, 8, None]]

        success = 0
        wrong = 0

        for a in range(len(real_matrix)):
            for b in range(len(real_matrix[0])):
                rm_item = real_matrix[a][b]
                pm_item = self.matrix[a][b]

                if rm_item == pm_item:
                    success +=1
                else:
                    wrong +=1


        print(f'Success = {success}\nWrong = {wrong}')



nia = numbers_ia()

nia.create_model()
nia.get_number_boxes()
nia.predict_numbers()
nia.create_matrix()

nia.accuracy_prediction_matrix()


'''
Model 3:(Blanco y negro): 60
Model 4:(changes in layers): 57 

'''