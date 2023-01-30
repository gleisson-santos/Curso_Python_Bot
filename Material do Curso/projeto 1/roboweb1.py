from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

driver = webdriver.Chrome('C:/Users/Leonardo/Desktop/Robos/chromedriver', options=options)
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear()
pesquisa.send_keys("roboscompython.com.br")
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()