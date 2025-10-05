from fastapi import FastAPI
import requests

app = FastAPI(title="API Pokémon y Goku")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de Pokémon y Goku"}

# --- Pokémon API ---
@app.get("/pokemon/{nombre}")
def obtener_pokemon(nombre: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        return {
            "nombre": data["name"],
            "altura": data["height"],
            "peso": data["weight"],
            "habilidades": [h["ability"]["name"] for h in data["abilities"]]
        }
    else:
        return {"error": "Pokémon no encontrado"}

# --- Goku API (Dragon Ball) ---
@app.get("/goku")
def obtener_goku():
    url = "https://dragonball-api.com/api/characters"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()

        # Buscar cualquier personaje que contenga 'goku' en su nombre
        for personaje in data.get("items", []):
            if "goku" in personaje["name"].lower():
                return {
                    "nombre": personaje["name"],
                    "raza": personaje.get("race", "Desconocida"),
                    "ki": personaje.get("ki", "Desconocido"),
                    "max_ki": personaje.get("maxKi", "Desconocido"),
                    "imagen": personaje.get("image", "Sin imagen")
                }

        return {"error": "No se encontró información de Goku"}
    else:
        return {"error": "Error al consultar la API de Goku"}

