from time import sleep 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

class board():
    def __init__(self):
        self.browser = webdriver.Chrome()
        url = "https://sudoku.com/"
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        html = self.browser.page_source.encode('utf-8').strip()

    def reject_cookies(self):
        self.browser.find_element(By.ID, 'onetrust-pc-btn-handler').click()
        self.browser.find_element(By.CLASS_NAME, 'ot-pc-refuse-all-handler').click()

    def screenshot(self):
        sleep(4)
        game =  self.browser.find_element(By.ID, 'game')
        game.screenshot('board.png')



board = board()

board.reject_cookies()
board.screenshot()


    

