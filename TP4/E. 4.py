def calcular_descuento(precio):
    if precio >= 10000:
        print("tu precio tiene un 10% de descuento")
        print("total a pagar: ")
        descuento = precio * 0.10
        return precio - descuento
    else:
        print("tu precio no tiene descuento")
        print("total a pagar: ")    
        return precio
    

print(calcular_descuento(9000))
print(calcular_descuento(15000))