def actualizar_persona(persona):
    # El diccionario 'persona' se pasa por referencia (mutable)

    # El valor 'nombre' es un str (inmutable), así que se reemplaza
    persona["nombre"] = persona["nombre"] + " López"

    # La lista 'hobbies' es mutable, se modifica directamente
    persona["hobbies"].append("programar")

# Diccionario original
persona = {
    "nombre": "Pablo",
    "edad": 30,
    "hobbies": ["leer", "caminar"]
}

# Aplicamos la función
actualizar_persona(persona)

# Mostramos el resultado
print(persona)

# Resultado esperado:
# {
#   'nombre': 'Pablo López',
#   'edad': 30,
#   'hobbies': ['leer', 'caminar', 'programar']
# }