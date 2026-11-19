import db

while True:
    print("Bienvenido a GymOs")
    print("1.Registrar Usuario")
    print("2.Ingresar")
    print("3.Borrar datos")
    print("0. Salir")

    opcion = input("Ingrese el numero de una opcion: ")

    match (opcion):
        case "0":
            print("Hasta luego...")
            break

        case "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")

            resultado = db.registrar_usuario(nombre, correo, contraseña)

            if resultado:
                print("Registro terminado")

        case "2":
            print("Escriba su Correo y contraseña")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")

        case "3":
            print("Seguro que quieres borrar la BD?")
            opcion = input("SI/NO: ")

            if opcion == "si":
                resultado = db.limpiarBD()
                if resultado:
                    print("BD Limpia")
                else:
                    print("Error eliminando la BD")

            else:
                break
