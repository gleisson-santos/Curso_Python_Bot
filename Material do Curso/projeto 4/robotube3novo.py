from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RoboYoutube():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def busca(self, busca):
        url = "https://www.youtube.com/results?search_query=%s" %busca
        self.driver.get(url)
        titulos = self.driver.find_elements(By.XPATH, "//*[@id='video-title']")
        for titulo in titulos:
            print("Video encontrado: %s" % titulo.text)

bot = RoboYoutube()
bot.busca("teste")