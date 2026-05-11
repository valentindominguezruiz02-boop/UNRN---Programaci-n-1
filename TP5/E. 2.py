numeros = (4, 7, 2, 9, 7)
print(f"primer valor: {numeros[0]}\nultimo valor: {numeros[-1]}")
for num in numeros:
    repe_7 = 0
    if num == 7:
        repe_7 += 1

print(f"La cantidad de veces que se repite el numero 7 son: {repe_7}")
print(f"el largo de la tupla es de {len(numeros)} elemtos")
