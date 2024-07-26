real_matrix = [[None,None,None,7,6,2,None,9,None],
               [None,None,None,3,8,None,None,2,7],
               [2,8,None, None,5,9,1,6,3],
               [None, None, None, None, None, None, 6, None, 1],
               [None, 1, 5, None, None, 3, 2, None, None],
               [6, None, None, None, 4, 5, 7, None , 8],
               [None, 2, None, 9, None, None, 4, None, 5],
               [None, 7, None, 8,2,4, None, None, None],
               [9, None, None, 5, None, 7, None, 8, None]]

predicted_matrix = [[None, 2, 2, 7, 8, 2, 2, 9, 2], [2, 2, 2, 3, 8, None, None, 2, 1], [2, 8, 2, None, 5, 9, 8, 3, 3], [2, None, None, None, None, None, 3, None, 5], [2, 1, 5, None, 
None, 3, 2, None, None], [0, None, None, None, 9, 3, 1, None, 1], [2, 2, None, 3, None, None, 1, None, 3], [2, 3, None, 3, 2, 1, None, None, None], [3, None, None, 3, None, 3, None, 3, None]]
success = 0
wrong = 0

for a in range(len(real_matrix)):
    for b in range(len(real_matrix[0])):
        rm_item = real_matrix[a][b]
        pm_item = predicted_matrix[a][b]

        if rm_item == pm_item:
            success +=1
        else:
            wrong +=1


print(f'Success = {success}\nWrong = {wrong}')


'''
Model 1: 46 Success
Model 2: 48 Sucess


'''