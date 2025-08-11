nombres_personas ={
    "nombre": "juan",
    "edad": 22,
    "profesion": "analista",
    "nacionalidad": "chileno"
}
"""funcion es mutable no lleva return porque ha cambiado el contenido
de el dict"""

def actualizar(actualizar_personas):
    actualizar_personas["comida_favorita"] = "cazuela"

actualizar(nombres_personas)
print(nombres_personas)


