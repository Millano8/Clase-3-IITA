"""
Crear un programa que me permita leer, escribir y actualizar el archivo jugadores_boca.json
"""
import json

cavani = {
    "10": {
        "nombre": "Edinson Cavani",
        "edad": "36"
    }
}

with open("jugadores_boca.json", "r", encoding='UTF-8') as f:
    data = json.load(f)

print(data)

data.update(cavani)


with open("jugadores_modificado.json", "w", encoding='UTF-8') as modificado:
    json.dump(data, modificado, indent=4)


with open("jugadores_modificado.json", "r") as modificado:
    modific = json.load(modificado)

print(modific)
