import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

class numbers_ia:
    def __init__(self, squares):
        self.squares = squares

    
    def create_model(self):
        '''Creates a knn model based on the .csv that I created. This model was greatly inspired from https://github.com/santifiorino/sudoku.com-solver'''
        df = pd.read_csv("dataset.csv")
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(X, y)
            
    def get_number_boxes(self):
        '''Searchs for the squares that are empty and those who doesn't. This is helpfull for clicking them later and for the prediction'''
        self.numbers_index = []
        empty_index = []

        for n in range(81):

            dark = 0

            array = np.array(self.squares[n])

            if np.all(array == 255):
                empty_index.append(n)
            else:
                self.numbers_index.append(n)
                
        
        return empty_index
               

    def predict_numbers(self):
        '''Makes predictions of the numbers'''
        self.numbers_matrix = []

        for n in range(81):

            try:
                if n in self.numbers_index:
                    prediction = self.knn.predict(self.squares[n])
                    self.numbers_matrix.append(prediction[0])
                    
            except:
                print(f'ERROR')
                break

            finally:
                n += 1

    def create_matrix(self):
        '''Creates the matrix of the initial sudoku. This matrix is going to be sended to the solver'''
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