producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}

for clave in producto:
    print(clave)

for clave in producto:
    print(producto[clave])

for clave in producto:
    print(f"{clave}: {producto[clave]}")