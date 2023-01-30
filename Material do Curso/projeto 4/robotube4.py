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

    def busca(self, busca, paginas):
        videos= []

        pagina = 1
        url = "https://www.youtube.com/results?search_query=%s" %busca
        self.webdriver.get(url)
        while pagina <= paginas:
            titulos = self.webdriver.find_elements_by_xpath("//*[@id='video-title']")
            for titulo in titulos:
                print("Video encontrado: %s" % titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print('Mudando para a proxima página %s' % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)

bot = RoboYoutube()
bot.busca("teste", 5)