# Datos de ventas por producto (nombre del producto y monto de venta)
ventas = {
    'manzanas': 100,
    'bananas': 75,
    'naranjas': 50,
    'uvas': 120,
    'peras': 90
}

# Calcular el total de ventas
total_ventas = sum(ventas.values())

# Imprimir el resumen de ventas
print("Resumen de Ventas por Producto:")
for producto, monto in ventas.items():
    print(f"{producto}: ${monto}")

print(f"Total de Ventas: ${total_ventas}")
