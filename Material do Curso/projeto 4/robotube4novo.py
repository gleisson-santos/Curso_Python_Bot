from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class RoboYoutube():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def busca(self, busca, paginas):
        videos= []

        pagina = 1
        url = "https://www.youtube.com/results?search_query=%s" %busca
        self.driver.get(url)
        while pagina <= paginas:
            titulos = self.driver.find_elements(By.XPATH, "//*[@id='video-title']")
            for titulo in titulos:
                print("Video encontrado: %s" % titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print('Mudando para a proxima página %s' % (pagina + 1))
        bottom = pagina * 10000
        self.driver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)

bot = RoboYoutube()
bot.busca("teste", 5)