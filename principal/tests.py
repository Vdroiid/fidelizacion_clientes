from django.test import TestCase

# Create your tests here.

"""
# Cadenas cortas de Base64
encoded_str = "poner_cadena"

# Decodificar la cadena
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')

print(decoded_str)  # Salida: "Hello world!"


# Esto sire para cadenas más largas


encoded_str = 'BRKhUSj5UtC_AyUtq8eqbiCnXy42kQaszGnHOWyML8Y'

# Verificar si la longitud es un múltiplo de 4 y añadir padding si es necesario
if len(encoded_str) % 4 != 0:
    encoded_str += '=' * (4 - len(encoded_str) % 4)

# Eliminar espacios o saltos de línea
encoded_str = encoded_str.replace(' ', '').replace('\n', '')

try:
    decoded_bytes = base64.b64decode(encoded_str)
    print(decoded_bytes)
except Exception as e:
    print(f"Error: {e}")




Para otros casos

import base64
import re

def is_base64(s):
    pattern = re.compile(r'^[A-Za-z0-9+/=]*$')
    if not pattern.fullmatch(s):
        return False
    return True

encoded_str = 'V92jOk6FeC0f47wIk5ZoMx7S-p7h3AQvtdlRGq-E5z8'

# Eliminar espacios y saltos de línea
encoded_str = encoded_str.replace(' ', '').replace('\n', '')

if is_base64(encoded_str):
    # Añadir padding si es necesario
    padding = len(encoded_str) % 4
    if padding:
        encoded_str += '=' * (4 - padding)

    try:
        # Decodificar con el modo no estricto para manejar el padding incorrecto
        decoded_bytes = base64.b64decode(encoded_str, validate=False)
        print(decoded_bytes)
    except Exception as e:
        print(f"Error: {e}")
else:
    print("La cadena no es una cadena Base64 válida.")

"""
import base64
import json

# JWT Token
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxMjYwNjkzLCJpYXQiOjE3MjEyNjA1NzMsImp0aSI6IjU4YWRkZjIzZjYxMTQxMGZhMDE4NzhkNzJjZjU5MDUzIiwidXNlcl9pZCI6Mn0.BRKhUSj5UtC_AyUtq8eqbiCnXy42kQaszGnHOWyML8Y"

# Separar las partes del JWT
header, payload, signature = jwt_token.split('.')

# Decodificar el Header
decoded_header = base64.urlsafe_b64decode(header + '==').decode('utf-8')
print("Header:", decoded_header)

# Decodificar el Payload
decoded_payload = base64.urlsafe_b64decode(payload + '==').decode('utf-8')
print("Payload:", decoded_payload)

# La Signature no se decodifica en un formato legible, pero puedes obtenerla en formato base64
print("Signature:", signature)




