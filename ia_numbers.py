import numpy as np
from PIL import Image
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


#Probar cambiar los colores de los pixeles que quiera en ciertos numeros. ejemplo: if grey == 254: 0

class numbers_ia:

    def create_model(self):
        df = pd.read_csv("dataset.csv")
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(X, y)
            
    def get_number_boxes(self):
        self.numbers_index = []
        empty_index = []

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

            if dark>=10:
                self.numbers_index.append(n)
            else:
                empty_index.append(n)
        
        return empty_index
            
            

    def predict_numbers(self):
        self.numbers_matrix = []

        for n in self.numbers_index:

            try:
                image = Image.open(f'squares/square{n}.png').convert('L')

                image_array = np.array(image).reshape(1, -1)

                prediction = self.knn.predict(image_array)
                
                self.numbers_matrix.append(prediction[0])
                    
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
    
        return self.matrix