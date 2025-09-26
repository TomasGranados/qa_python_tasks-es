import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

    print("=== DESPUÉS DE 2 SEGUNDOS ===")
    time.sleep(2)
    elements_2s = driver.find_elements(By.XPATH, ".//img")
    print(f"🔍 XPath con 2s: {len(elements_2s)} imágenes")

    print("\n=== DESPUÉS DE 5 SEGUNDOS ===")
    time.sleep(3)  # 3 segundos más = 5 total
    elements_5s = driver.find_elements(By.XPATH, ".//img")
    print(f"🔍 XPath con 5s: {len(elements_5s)} imágenes")

    print("\n=== DESPUÉS DE 10 SEGUNDOS ===")
    time.sleep(5)  # 5 segundos más = 10 total
    elements_10s = driver.find_elements(By.XPATH, ".//img")
    print(f"🔍 XPath con 10s: {len(elements_10s)} imágenes")

    print("\n=== COMPARANDO DIFERENTES MÉTODOS ===")
    xpath_imgs = driver.find_elements(By.XPATH, ".//img")
    css_imgs = driver.find_elements(By.CSS_SELECTOR, "img")
    tag_imgs = driver.find_elements(By.TAG_NAME, "img")

    print(f"XPath './/img': {len(xpath_imgs)}")
    print(f"CSS 'img': {len(css_imgs)}")
    print(f"TAG_NAME 'img': {len(tag_imgs)}")

    print("\n=== DETALLES DE LAS IMÁGENES ENCONTRADAS ===")
    for i, img in enumerate(xpath_imgs, 1):
        src = img.get_attribute('src')
        style = img.get_attribute('style')
        visible = img.is_displayed()
        print(f"Imagen {i}: visible={visible}, src='{src}', style='{style}'")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()