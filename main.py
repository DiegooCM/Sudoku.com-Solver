from findtable import board
from ia_numbers import numbers_ia
from sudoku_solver import solver

def main():
    find_board = board()
    numbers = numbers_ia()
    solve_sudoku = solver()
    
    #find_board.open_browser()
    #find_board.reject_cookies()
    #find_board.screenshot()

    #find_board.get_boxes()

    #numbers.create_model()
    #numbers.get_number_boxes()
    #numbers.predict_numbers()
    #numbers.create_matrix()

    numbers.accuracy_prediction_matrix()
    
    #pass


if __name__ == "__main__":
    main()