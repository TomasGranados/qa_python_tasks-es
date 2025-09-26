import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")
time.sleep(10)
# Encontrar todos los elementos
elements = driver.find_elements(By.XPATH, ".//img")
print(f"DEBUG: Encontré {len(elements)} imágenes")  # ← ESTA LÍNEA
# Comprobar que el número de elementos encontrados es mayor que 1 usando len()
assert len(elements) > 1, f"Expected more than 1 <img> element, but found {len(elements)}"

# Cerrar el navegador
driver.quit()

