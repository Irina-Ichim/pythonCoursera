# Saludando a Irina y mostrando su número favorito
name = "Irina"
number = len(name) + 3
print("Hola {}, tu numero favorito es {}".format(name, number))

# Mostrando el número favorito de Irina de otra manera utilizando .format()
print("Tu numero favorito es {number}, {name}.".format(name=name, number=len(name) + 3))

# Calculando el precio con impuestos y mostrándolo con formato
price = 97.8 
with_tax = price * 0.21 
print(price, with_tax)
print("Base price: $:{:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# Definiendo una función para convertir Fahrenheit a Celsius
def to_celsius(x):
    return (x - 32) * 5 / 9

# Mostrando una tabla de conversiones de Fahrenheit a Celsius
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

