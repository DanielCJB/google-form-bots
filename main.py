import random
import time
from config import form_url, opciones_pregunta1, opciones_pregunta2, opciones_pregunta3
from voter import enviar_respuesta

for i in range(5):
    print(f"\n🌀 Envío #{i + 1}")

    seleccion1 = random.choice(opciones_pregunta1)
    seleccion2 = random.choice(opciones_pregunta2)
    seleccion3 = random.choice(opciones_pregunta3)

    print(f"✅ Pregunta 1: {seleccion1}")
    print(f"✅ Pregunta 2: {seleccion2}")
    print(f"✅ Pregunta 3: {seleccion3}")

    enviar_respuesta(form_url, seleccion1, seleccion2, seleccion3)

    tiempo_espera = random.uniform(2.0, 6.0)
    print(f"⏳ Esperando {tiempo_espera:.2f} segundos...")
    time.sleep(tiempo_espera)

print("✔️ El formulario se envió correctamente...")
