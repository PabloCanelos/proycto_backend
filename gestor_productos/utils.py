#utils.py
#este modulo contine funciones auxiliares


productos = {
    "monitor": 1200,
    "teclado": 450,
    "mouse": 300,
    "activo": True
}
"""ejemplo de funcion reutilizable"""
def calcular_total(productos):
    total = 0
    for precio in productos.values():
        if isinstance(precio, (int, float)):
            total += precio
    return total

"""llamado a la funcion"""
total_final = calcular_total(productos)
print("Total calculado:", total_final)