#data.py
# este es un diccionario simple, no anidado, clave-valor
# recordar que los diccionarios van entre {}
productos = {
    "monitor": 1200,
    "teclado": 450,
    "mouse": 300,
    "activo": True
}

"""conceptos a aprender  "funcion impura"(modifica directamente modificando la original)"""
def desactivar_todos(productos):
    for p in productos:
        p["activo"] = False


"""ejemplo de funcion"pura"(devuelve una lista nueva sin modificar la original)"""
"""Datos sensibles, lógica predecible, test unitarios"""
"""Scripts rápidos, mutaciones intencionales, performance"""
def desactivar_todos_puro(productos):
    nueva = []
    for p in productos:
        copia = p.copy()
        copia["activo"] = False
        nueva.append(copia)
    return nueva
"""Preguntas clave para reflexionar
1. 	¿Cuál usarías si estás en un backend que maneja datos sensibles?
2. 	¿Qué pasa si después querés mostrar los productos originales?
3. 	¿Cómo documentarías cada función para que otro dev entienda su comportamiento?"""