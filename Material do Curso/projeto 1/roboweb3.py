from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


print("Iniciando nosso robô...\n")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

driver = webdriver.Chrome('C:/Users/Leonardo/Desktop/Robos/chromedriver', options=options)
driver.get("https://registro.br/")


dominios = ["roboscompython.com.br", "hotmart.com.br", "uol.com.br", "pythoncurso.com.br"]
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    print("Donínio %s %s" % (dominio, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))


driver.close()