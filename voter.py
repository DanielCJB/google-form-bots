from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import modo_headless
import time


def enviar_respuesta(form_url: str, seleccion: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    if modo_headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(form_url)
    wait = WebDriverWait(driver, 10)

    opcion = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        f"//label[.//span[text()='{seleccion}']]"
    )))
    opcion.click()

    boton_enviar = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//span[text()='Enviar']/ancestor::div[@role='button']"
    )))
    boton_enviar.click()

    time.sleep(1)
    driver.quit()
