import os
from time import sleep 
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
import pyautogui
from selenium.webdriver.chrome.options import Options


class board():
    def open_browser(self):
        '''Opens the browser and the sudoku.com webpage'''
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.browser = webdriver.Chrome(options=chrome_options)
        url = "https://sudoku.com/"
        self.browser.maximize_window()
        self.browser.get(url)
        
        self.browser.implicitly_wait(10)
        html = self.browser.page_source.encode('utf-8').strip()

    def reject_cookies(self):
        '''Rejects cookies'''   
        self.browser.find_element(By.ID, 'onetrust-pc-btn-handler').click()
        self.browser.find_element(By.CLASS_NAME, 'ot-pc-refuse-all-handler').click()

    def screenshot(self):
        '''Makes a screenshot of the sudoku board. The leftClicks are to delete a text that appears in the sudoku board when you open the webpage'''
        self.game =  self.browser.find_element(By.ID, 'game')

        location = self.game.location
        self.x_game = location['x'] 
        self.y_game = location['y'] + 150

        pyautogui.leftClick(self.x_game + 20, self.y_game)
        pyautogui.leftClick(self.x_game + 20, self.y_game)
        sleep(0.2)
        self.game.screenshot('board.png')

    def get_boxes(self):
        '''Makes the array with all squares from the board.png'''
        filename = 'board.png'

        board = Image.open(filename)

        size = board.size

        square_size = int(size[0] // 9)

        squares = []
        n = 0
        for y in range(0, size[0] - 10, square_size):
            for x in range(0, size[0] - 10, square_size):

                square_bbox =  x , y, square_size + x , square_size + y #im.crop((left - x0, top - y0, right - x0, bottom - y0))
                square = board.crop(square_bbox)
                self.square_size = square.size
                square = square.crop((12, 12, 45, 45))

                square = square.convert('L')
                
                new_squaredata = []
                square_data = list(square.getdata())

                for color in square_data:
                    if color < 155:
                        new_squaredata.append(0)
                    else:
                        new_squaredata.append(255)    

                square = Image.new(square.mode, square.size)
                square.putdata(new_squaredata)

                square_array = np.array(square).reshape(1, -1)

                squares.append(list(square_array))

                n+=1

        return squares

    def click_solution(self, matrix, empty):
        '''Clicks the solution on the board, and removes board.png'''
        os.remove('board.png')
        
        pos = 0
        for column in range(9):
            for row in range(9):
                
                if pos in empty:
                    pyautogui.press([str(matrix[column][row]), 'right']) 
                else:
                    pyautogui.press('right')
                
                pos += 1

            pyautogui.press('down')
            pyautogui.press('left', presses=8)
        sleep(10)
        self.browser.close()
        self.browser.quit()