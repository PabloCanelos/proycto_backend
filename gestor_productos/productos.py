def duplicar(x):
    x = x * 2
    return x

numero = 5
resultado = duplicar(numero)

print("Original:", numero)      # ¿Qué esperás?
print("Resultado:", resultado)  # ¿Qué devuelve?

#¿Qué implica usar bien return?
#🔹 1. Saber qué tipo de dato estás manejando#
# - Si es inmutable (int, str, float), tenés que usar return para que el cambio exista.
#- Si es mutable (list, dict), podés modificar directamente o devolver una copia.

def agregar_producto(lista):
    lista.append("Teclado")

    

