import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

#Probar cambiar los colores de los pixeles que quiera en ciertos numeros. ejemplo: if grey == 254: 0

class numbers_ia:

    def __init__(self):
        self.model_name = 'model1.keras'


    def create_model(self):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1), activation='relu'))
        # Add a Max pooling layer
        model.add(tf.keras.layers.MaxPool2D())
        # Add the flattened layer
        model.add(tf.keras.layers.Flatten())
        # Add the hidden layer
        model.add(tf.keras.layers.Dense(512, activation='relu'))
        # Adding a dropout layer
        model.add(tf.keras.layers.Dropout(0.2))
        # Add the output layer
        model.add(tf.keras.layers.Dense(10, activation='softmax'))
        # Compiling the model
        model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

        model.fit(x_train, y_train, epochs= 5) # Lo entrenamos

        model.save(self.model_name) 
    
    def get_number_boxes(self):
        self.numbers_index = []

        for n in range(81):
            img = Image.open(f'squares/square{n}.png').convert('L')

            dark = 0
            new_imgdata = []

            for color in img.getdata():
                if color < 155:
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
                img = cv2.imread(f'squares/square{n}.png', 0)

                img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_LINEAR)
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
        real_matrix = [[5, None, 1, 6, None, 2, 9, None, 4],
               [6, None, 9, 8, None, None, None, None, None],
               [8, 2, 7, None, None, 9, None, None, 3],
               [4, None, 6, 1, None, 7, None, None, 2],
               [2, 1, 8, 3, None, None, None, None, 5],
               [7, 5, None, None, None, 4, None, 9, None],
               [None, 7, 4, None, 2, None, None, None, 1],
               [None, 8, None, None, 6, 3, None, None, None],
               [None, None, None, None, None, 5, 3, 7, None]]
 
        success = 0
        wrong = 0
        wrong_items = []
        correct_wrong = []
        for a in range(len(real_matrix)):
            for b in range(len(real_matrix[0])):
                rm_item = real_matrix[a][b]
                pm_item = self.matrix[a][b]

                if rm_item == pm_item:
                    success +=1
                else:
                    wrong_items.append(rm_item)
                    correct_wrong.append(pm_item)
                    wrong +=1


        print(f'Success = {success}\nWrong = {wrong}\n Se ha equivocado en los siguientes números: {wrong_items}\n                             Debería de ser: {correct_wrong}')


'''
nia = numbers_ia()

#nia.create_model()
nia.get_number_boxes()
nia.predict_numbers()
nia.create_matrix()

nia.accuracy_prediction_matrix()



Model 1(Con cambios en los recortes)
Model1(CNN): 68
Model1(CNN)(cambiando el color): 65

Model 1(CNN copiado de github): 64

'''


