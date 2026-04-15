temperatura = input("escribe la temperatura actual")

if int(temperatura)>= 10 and int(temperatura) <= 20:
    print("se recomienda usar ropa medianamente abrigada")
elif int(temperatura) > 20:
    print("se recomienda usar ropa liviana")
else:
    print("se recomienda usar ropa abrigada")