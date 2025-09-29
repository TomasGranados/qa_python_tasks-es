from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Este objeto se usará para todas las esperas explícitas
wait = WebDriverWait(driver, 10)

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Usar el objeto de espera hasta que el campo de correo electrónico esté presente, luego ingresarlo
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("some_email")

# Usar el objeto de espera hasta que el campo de contraseña esté presente, luego ingresarla
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("some_password")

# Usar el objeto de espera hasta que el botón de inicio de sesión sea clickeable, luego hacer clic en él
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

# Usar el objeto de espera hasta que la sección de usuario sea visible después de iniciar sesión
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__user")))

# Usar el objeto de espera para obtener el botón de cierre de sesión y verificar que su texto sea 'Log out'
logout_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text
assert logout_text.strip() == 'Cerrar sesión', f"Se esperaba 'Cerrar sesión', pero se obtuvo '{logout_text}'"

driver.quit()

