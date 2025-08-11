from data import productos
from productos import mostrar_productos
from gestor_productos.por_valor_o_referencia import nuevos_productos
from productos import desactivar_producto


print(desactivar_producto(nuevos_productos, "active"))
print(nuevos_productos)