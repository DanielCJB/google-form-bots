from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import modo_headless
import time


def enviar_respuesta(form_url: str, pregunta1: str, pregunta2: str, pregunta3: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    if modo_headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(form_url)
    wait = WebDriverWait(driver, 10)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    })

    respuestas = [pregunta1, pregunta2, pregunta3]

    for respuesta in respuestas:
        try:
            opcion = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//label[.//span[normalize-space()='{respuesta}']]"
            )))
            driver.execute_script("arguments[0].scrollIntoView(true);", opcion)
            opcion.click()
            print(f"✅ Clic en: {respuesta}")
        except Exception as e:
            print(f"❌ No se encontró la opción: {respuesta}")
            driver.quit()
            return

    try:
        boton_enviar = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[text()='Enviar']/ancestor::div[@role='button']"
        )))
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", boton_enviar)
        time.sleep(1)  # Dar tiempo a que aparezca
        boton_enviar.click()
        print("📤 Formulario enviado correctamente")
    except Exception as e:
        print("❌ No se pudo hacer clic en el botón Enviar")
        print(f"Error: {e}")

    time.sleep(2.0)
    driver.quit()
