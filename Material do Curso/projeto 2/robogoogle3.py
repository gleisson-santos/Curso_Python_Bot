from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("Digite a pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

driver = webdriver.Chrome('C:/Users/Leonardo/Desktop/Robos/chromedriver', options=options)
driver.get("https://www.google.com")

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element_by_xpath("//*[@id='result-stats']").text
print(resultados)

numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
maximo_paginas = numero_resultados/10

print("Número de páginas: %s"% (maximo_paginas))