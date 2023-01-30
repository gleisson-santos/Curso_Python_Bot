from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
import time

class RoboYoutube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        self.webdriver = webdriver.Chrome('C:/Users/Leonardo/Desktop/Robos/chromedriver', options=options)

bot = RoboYoutube()