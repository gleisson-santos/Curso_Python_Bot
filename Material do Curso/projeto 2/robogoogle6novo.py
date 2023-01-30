from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pesquisa = input("Digite a pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.google.com")

campo = driver.find_element(By.XPATH, "//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element(By.XPATH, "//*[@id='result-stats']").text
print(resultados)

numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
maximo_paginas = numero_resultados/10

print("Número de páginas: %s"% (maximo_paginas))

url_pagina = driver.find_element(By.XPATH, "//a[@aria-label='Page 2']").get_attribute("href")

pagina_atual = 0
start = 10
lista_resultados = []
while pagina_atual <= 8:
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace("start=%s" % start, "start=%s" % (start+10))
        start = start + 10
        driver.get(url_pagina)
    
    

    divs = driver.find_elements_by_xpath("//div[@class='g']")
    divs = divs + driver.find_elements(By.XPATH, "//div[contains(@class, 'g ')]")
    for div in divs:
        try:
            nome = div.find_element(By.TAG_NAME, "h3")
            link = div.find_element(By.TAG_NAME, "a")
            resultado = "%s;%s" % (nome.text,link.get_attribute("href"))
            print(resultado)
        except:
            print('Informações não encontradas')
        lista_resultados.append(resultado)
    pagina_atual = pagina_atual + 1    

with open("resultadosrobo.txt", "w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write("%s\n" %resultado)
    arquivo.close

print("%s resultados encontrados do Google e salvos no arquivo resultados.txt" % len(lista_resultados))