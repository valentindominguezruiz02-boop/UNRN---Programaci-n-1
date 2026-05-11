materias = {"Matemática", "Programación"}
materias.add("Física")
esta = False
for materia in materias:
    if materia == "Quimica":
        esta = True
    
if esta == True:
    print("Quimica esta en el set")
else:
    print("Quimica no esta en el set")

print("set:", materias)