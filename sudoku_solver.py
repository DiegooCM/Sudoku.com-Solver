import numpy as np

# Tengo que hacer listas de los posibles numeros que quedan en una fila columna o cuadrado, e ir probando con esos numeros y ver si en algun momento se repite

class solver():

    def __init__(self):
        self.matrix = [[None,None,None,7,6,2,None,9,None],
               [None,None,None,3,8,None,None,2,7],
               [2,8,None, None,5,9,1,6,3],
               [None, None, None, None, None, None, 6, None, 1],
               [None, 1, 5, None, None, 3, 2, None, None],
               [6, None, None, None, 4, 5, 7, None , 8],
               [None, 2, None, 9, None, None, 4, None, 5],
               [None, 7, None, 8,2,4, None, None, None],
               [9, None, None, 5, None, 7, None, 8, None]]
        
    def check_axis(self):
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
                            x_axis, y_axis = check_x(a, b)
                            square_list = check_square(a, b)

                            #print(a, b)
                            missing = find_missing_item(x_axis, y_axis, square_list)

                            if missing != None: self.matrix[a][b] = missing
                print(self.matrix)

solve = solver()

solve.check_axis()


