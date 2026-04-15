def obtener_estado(nota):
    if nota >= 8:
        print("Promociona")
    elif nota >= 6:
        print("regulariza")
    else:
        print("desaprueba")

obtener_estado(10)
obtener_estado(8)
obtener_estado(6)
obtener_estado(4)
obtener_estado(2)