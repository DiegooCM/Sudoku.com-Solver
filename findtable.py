from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
import pyautogui
from selenium.webdriver.chrome.options import Options

class board():
    def open_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.browser = webdriver.Chrome(options=chrome_options)
        url = "https://sudoku.com/"
        self.browser.maximize_window()
        self.browser.get(url)
        
        self.browser.implicitly_wait(10)
        html = self.browser.page_source.encode('utf-8').strip()

    def reject_cookies(self):   
        self.browser.find_element(By.ID, 'onetrust-pc-btn-handler').click()
        self.browser.find_element(By.CLASS_NAME, 'ot-pc-refuse-all-handler').click()

    def screenshot(self):
        self.game =  self.browser.find_element(By.ID, 'game')

        location = self.game.location
        self.x_game = location['x'] 
        self.y_game = location['y'] + 150

        pyautogui.doubleClick(self.x_game + 20, self.y_game)
        self.game.screenshot('board.png')

    def get_boxes(self):
        filename = 'board.png'

        board = Image.open(filename)

        size = board.size

        square_size = int(size[0] // 9)

        n = 0
        for y in range(0, size[0] - 10, square_size):
            for x in range(0, size[0] - 10, square_size):
                square_bbox =  x , y, square_size + x , square_size + y #im.crop((left - x0, top - y0, right - x0, bottom - y0))
                self.square = board.crop(square_bbox)
                self.square_size = self.square.size
                self.square = self.square.crop((12, 12, 45, 45))

                self.square.save(f'squares/square{n}.png')
                
                n+=1

    def click_solution(self, matrix, empty):
        
        pos = 0
        for column in range(len(matrix)):
            for row in range(len(matrix)):
                
                if pos in empty:
                    pos_click = (self.x_game + (row * self.square_size[0])) + 30, (self.y_game + (column * self.square_size[0])) + 25


                    pyautogui.click(pos_click[0], pos_click[1]) 

                    pyautogui.press(str(matrix[column][row])) 
                
                pos += 1
        
        sleep(10)
        self.browser.close()

