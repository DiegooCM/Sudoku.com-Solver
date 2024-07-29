from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image

class board():
    def open_browser(self):
        self.browser = webdriver.Chrome()
        url = "https://sudoku.com/"
        self.browser.maximize_window()
        self.browser.get(url)
        
        self.browser.implicitly_wait(10)
        html = self.browser.page_source.encode('utf-8').strip()

    def reject_cookies(self):   
        self.browser.find_element(By.ID, 'onetrust-pc-btn-handler').click()
        self.browser.find_element(By.CLASS_NAME, 'ot-pc-refuse-all-handler').click()

    def screenshot(self):
        sleep(10)
        game =  self.browser.find_element(By.ID, 'game')
        sleep(2)
        game.screenshot('board.png')

    def get_boxes(self):
        filename = 'board.png'

        board = Image.open(filename)

        size = board.size

        square_size = int(size[0] // 9)

        n = 0
        for y in range(0, size[0] - 10, square_size):
            for x in range(0, size[0] - 10, square_size):
                square_bbox =  x , y, square_size + x , square_size + y #im.crop((left - x0, top - y0, right - x0, bottom - y0))
                square = board.crop(square_bbox)
                square = square.crop((12, 12, 45, 45))

                square.save(f'squares/square{n}.png')
                
                n+=1



#board = board()

#board.open_browser()
#board.reject_cookies()
#board.screenshot()

#board.get_boxes()


    

