lista = []
while True:
    print()
    des_lista = input("desea agregar algo a la lista ")
    if des_lista == "si":
        print()
        lista.append(input("escriba lo que quiera agregar a la lista "))
    else:
        print()
        print("lista terminada")
        break
        
print()
print(lista)
print(len(lista)) 