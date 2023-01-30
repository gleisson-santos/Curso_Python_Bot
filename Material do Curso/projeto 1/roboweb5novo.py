from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import xlrd

print("Iniciando nosso robô...\n")

arq = open("resultado.txt", "w")
workbook = xlrd.open_workbook(r'C:\Users\Leonardo\Desktop\Robos\excel.xls')
sheet = workbook.sheet_by_name('Plan1')
rows = sheet.nrows
columns = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://registro.br/")


for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    texto ="Domínio %s %s\n" % (x, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    arq.write(texto)

arq.close()
driver.close()