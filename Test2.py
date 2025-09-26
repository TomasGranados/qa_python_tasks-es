import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# Buscar el título
title_element = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

# Busc ar e imprimir la linea con el texto
print("Login form title:", title_element.text)

# Cerrar el navegador
driver.quit()