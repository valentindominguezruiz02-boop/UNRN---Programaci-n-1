lista = ["lapiz", "lapicera", "goma", "tijeras", "cuter", "sacapuntas", "regla", "compas"]
elemento_e = input("escribe un útil escolar ")
i = 0
if elemento_e in lista:
    print()
    print("el elemento elegido se encuentra en la lista")
    print()
    print("el elemento elegido es el numero", lista.index(elemento_e), "de la lista")
else:
    print()
    print("el elemento elegido no se encuentra en la lista")