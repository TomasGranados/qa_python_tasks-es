import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

# Pausa la ejecución durante 5 segundos para permitir que la página se cargue correctamente
time.sleep(5)

# Para buscar un elemento
element = driver.find_element(By.XPATH, ".//img")
print(element)

# Para buscar un grupo de elementos
elements = driver.find_elements(By.XPATH, ".//input")
print(elements)