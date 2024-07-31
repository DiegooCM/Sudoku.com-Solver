from findtable import board
from ia_numbers import numbers_ia
from sudoku_solver import solver

def main():
    # Open the browser and the webpage, and get an array of the squares
    find_board = board()
    
    find_board.open_browser()
    find_board.reject_cookies()
    find_board.screenshot()
    squares = find_board.get_boxes()

    # Create de KNN model, makes the predictions and creates de matrix of the sudoku
    numbers = numbers_ia(squares)
    numbers.create_model()
    empty_index = numbers.get_number_boxes()
    numbers.predict_numbers()
    matrix = numbers.create_matrix()

    # Solves the sudoku
    solve = solver(matrix)
    matrix_solved = solve.solve_matrix()

    # Click the solutions on the webpage
    find_board.click_solution(matrix_solved, empty_index)



if __name__ == "__main__":
    main()