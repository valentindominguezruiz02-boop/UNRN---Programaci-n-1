lista = []
while True:
    a_comida = input("escriba la comida que desea agregar o escriba (terminar) para salir: ")
    if a_comida == "pizza" or a_comida == "hamburgueza" or a_comida == "empanadas":
        lista.append(a_comida)
        print()
    elif a_comida == "terminar":
        print()
        print("lista terminada")
        break
    else:
        print()
        print("ERROR, ese tipo de comida es invalido")
print()
print(lista)
print("elementos de la lista:", len(lista))