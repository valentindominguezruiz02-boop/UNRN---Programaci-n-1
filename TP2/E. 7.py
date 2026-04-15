dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
for i in range(len(dias)):
    print( 1 + i, dias[i])

print()

for numero, dia in enumerate(dias, start = 1):
    print(numero, dia)