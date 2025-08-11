"""¿Qué significa “por valor” y “por referencia”?
| Tipo de paso   | ¿Qué se copia?                   | ¿Qué se comparte? | ¿Puede modificarse desde la función? |

| Por valor      | Se copia el contenido            | Nada |            | ❌ No (la original queda intacta) |
| Por referencia | Se copia la dirección en memoria | ✅ Sí             | ✅ Sí (la original puede cambiar) |
"""

# Tipos inmutables → por valor
#- int, float, str, bool, tuple
"""- int → 5, 100, -3
- float → 3.14, 0.5
- str → "100", "hola"
- bool → True, False
- tuple → (1, 2)
"""
"""ejemplo por valor"""
def duplicar(x):
    x = x * 2
a = 5
duplicar(a)
print(a)  # Sigue siendo 5
"""→ a no cambia, porque los enteros se pasan por valor.
inmutable debe llevar un return
"""
#"""""""""""""""""



"""ejemplo por referencia"""
"""Tipos mutables → por referencia, no lleva return"""
#list, dict, set, object
def agregar_item(lista):
    lista.append("nuevo")
""" mi_lista cambia, porque las listas se pasan por referencia.
"""
mi_lista = ["a", "b"]
agregar_item(mi_lista)
print(mi_lista)  # ["a", "b", "nuevo"]




nuevos_productos = {
    "lampara": 800,
    "alfombra": 1500,
    "cortina": 950,
    "active": True
}