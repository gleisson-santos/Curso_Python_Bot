from selenium import webdriver # fazer upgrade do selenium pelo pip install --upgrade
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Iniciando nosso robô...\n")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://registro.br/")

pesquisa = driver.find_element(By.ID, "is-avail-field")
pesquisa.clear()
dominio = "roboscompython.com.br"
pesquisa.send_keys(dominio)
pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')# de PATH virou XPATH
print("Donínio %s %s" % (dominio, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))# de PATH virou XPATH

time.sleep(8)
driver.close()