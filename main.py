import random
import time
from config import form_url, opciones_formulario
from voter import enviar_respuesta

for i in range(5):
    print(f"\n🌀 Envío #{i + 1}")

    seleccion = random.choice(opciones_formulario)
    print(f"✅ Opción elegida: {seleccion}")

    enviar_respuesta(form_url, seleccion)

    tiempo_espera = random.uniform(1.0, 4.0)
    print(f"⏳ Esperando {tiempo_espera:.2f} segundos...")
    time.sleep(tiempo_espera)

print("✔️ El formulario se envió correctamente...")
