from google import genai

GEMINI_API_KEY = ""
client = genai.Client(api_key=GEMINI_API_KEY)

"""
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explicame de una manera sencilla como trabajan los modelos de IA"
)
"""

animal = input("Ingresa un animal:")
lugar = input("Ingresa un lugar:")
accion = input("Ingresa una accion:")


response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"crea un poema de 3 estrofas sobre un {animal}, que vive en {lugar} y que esta haciendo {accion}"
)

print(response.text)
