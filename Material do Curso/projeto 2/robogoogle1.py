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