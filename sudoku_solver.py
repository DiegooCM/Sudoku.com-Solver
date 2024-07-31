import numpy as np
from time import sleep
# Tengo que hacer listas de los posibles numeros que quedan en una fila columna o cuadrado, e ir probando con esos numeros y ver si en algun momento se repite

class solver():

    def __init__(self, matrix):
        self.matrix = matrix
        
    def solve_matrix(self):
        '''Mira en la fila, columna y cuadrado del item, y hace una lista de todos los números que aparecen'''

        def check_x(x, y):
            x_axis = []
            y_axis = []

            for a in range(len(self.matrix)):
                for b in range(len(self.matrix)):
                    item = self.matrix[a][b]
                    
                    if b == y:
                        if item != None:y_axis.append(item)
                
                    if a == x:
                        if item != None:x_axis.append(item)

            return x_axis, y_axis

        def check_square(x, y):
            square_list = []
            square_row = (x // 3) * 3
            square_column = (y // 3) * 3

            for a in range(3):
                for b in range(3):
                    item = self.matrix[square_row + a][square_column + b]

                    if item != None: square_list.append(item)

            return square_list
        
        def find_missing_item(list1, list2, list3):
            posible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            f_array = np.concatenate((list1, list2, list3), axis= None)

            f_array = np.unique(f_array)

            results = np.setdiff1d(posible_numbers, f_array)
            #print(results)
 
            if len(results) == 1:
                missing = results[0]

                return missing


        '''Mira si en la matriz hay algun None, y si lo hay pues intenta resolverlo'''
        for xs in range(len(self.matrix)):
            while None in self.matrix[xs]:
                '''Resuelve como antes mencionado'''
            
                for a in range(len(self.matrix)):
                    for b in range(len(self.matrix)):

                        item = self.matrix[a][b]
                        if item == None:
                            #print(f'{a, b}:')
                            x_axis, y_axis = check_x(a, b)
                            #print(f'X axis: {x_axis} Y axis: {y_axis}')
                            square_list = check_square(a, b)
                            #print(f'Square: {square_list}')

                            
                            missing_item = find_missing_item(x_axis, y_axis, square_list)

                            if missing_item != None: self.matrix[a][b] = missing_item
        
        return self.matrix