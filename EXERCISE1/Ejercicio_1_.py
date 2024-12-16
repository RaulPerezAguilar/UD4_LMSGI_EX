import json
from datetime import datetime

# Función para validar si un string es un JSON válido
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print(f"JSON inválido: {error}")
        return False

# Función para validar el formato de una fecha
def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Leer el archivo JSON
try:
    with open("nombre.json", "r") as json_file:
        data = json.load(json_file)

    # Verificar si la clave 'fecha_nacimiento' existe
    if "fecha_nacimiento" in data:
        if validate_date_format(data["fecha_nacimiento"]):
            print("Fecha de nacimiento válida")
        else:
            print("Fecha de nacimiento inválida")
    else:
        print("No se encontró la clave 'fecha_nacimiento' en el JSON")
except FileNotFoundError:
    print("El archivo 'nombre.json' no se encontró.")
except json.JSONDecodeError as error:
    print(f"Error al decodificar JSON: {error}")
