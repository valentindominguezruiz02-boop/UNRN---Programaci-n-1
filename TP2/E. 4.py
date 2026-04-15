contraseña_registrada = "hola mundo"
codigo_token = "vdr"
usa_clave_token = (input("¿usa codigo token? si/no "))
acceso = False
if usa_clave_token == "si":
    while True:
        print()
        inserte_token = input("inserte su codigo token o escriba salir para usar la contraseña ")
        if inserte_token == codigo_token:
            print()
            print("acceso permitido")
            print("gracias por usar el sistema de seguridad de nuestro banco")
            acceso = True
            break
        elif inserte_token == "salir":
            break
        else:
            print()
            print("codigo token incorrecto, inserte nuevamente")
if not acceso:
    print()
    print("okey")
    while True:
        print()
        contraseña = input("ingrese la contraseña ")
        if contraseña == contraseña_registrada:
           print()
           print("acceso permitido")
           print("gracias por usar el sistema de seguridad de nuestro banco")
           break
        else:
          print()
          print("contraseña incorrecta, intentelo nuevamente")