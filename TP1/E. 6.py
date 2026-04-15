edad = input("escribe tu edad")
if (int(edad)) >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")


edad_en_meses = (int(edad)) * 12 
edad_futura = (int(edad)) + 10


opcion1 = input("¿quieres saber cuanto sería eso en meses?")
if opcion1 == "si":
    print('vale, si has vivido durante ', edad, 'anios, eso es igual a haber vivido durante', edad_en_meses, 'meses')
else:
    print("okey")


opcion2 = input("¿Quieres saber cuantos anios tendras en 10 anios?")
if opcion2 == "si":
    print("en 10 anios vas a tener ", edad_futura, "anios.")
else:
    print("vale")


altura = input("Escriba su altura en metros")
altura2 = (float(altura)) * 2


opcion3 = input("¿quieres saber cual es el doble de tu altura?")
if opcion3 == "si":
    print(" el doble de tu altura es ", altura2, "metros")
else:
    print("entendido")

print("Segun la informacion dada puedo decir que tienes ", edad, "anios, y en meses eso sería ", edad_en_meses, "meses, tu edad en 10 anios va a ser ", edad_futura, "anios, mides ", altura, "metros y el doble de tu altura es ", altura2, "metros.")