from findtable import board
from ia_numbers import numbers_ia
from sudoku_solver import solver

def main():
    find_board = board()
    
    
    find_board.open_browser()
    find_board.reject_cookies()
    find_board.screenshot()
    squares = find_board.get_boxes()

    numbers = numbers_ia(squares)
    numbers.create_model()
    empty_index = numbers.get_number_boxes()
    numbers.predict_numbers()
    matrix = numbers.create_matrix()

    solve = solver(matrix)
    matrix_solved = solve.solve_matrix()

    find_board.click_solution(matrix_solved, empty_index)



if __name__ == "__main__":
    main()


'''
Que tarde menos en escribir los numeros
Ultimo. Subirlo a github con el readme y toda la pesca
'''