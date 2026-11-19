import sqlite3

with sqlite3.connect("gym_db") as conexion:
    cursor = conexion.cursor()

    # Parte provicional para el CRUD de la BD
    while True:
        print("Bienvenido a GymOs")
        print("1.Registrar Usuario")
        print("2.Ingresar")
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

                query = """
                INSERT INTO Users(nombre,correo,contraseña)
                VALUES (?,?,?);
                """

                user_data = (nombre, correo, contraseña)

                cursor.execute(query, user_data)

                conexion.commit()

                print("Usruario guardado Exitosamente")

            case "2":
                print("Escriba su Correo y contraseña")
                correo = input("Correo: ")
                contraseña = input("Contraseña: ")

                query = """
                SELECT * FROM Users
                WHERE correo = ?;
                """

                user_data = (correo,)

                cursor.execute(query, user_data)

                # Optenemos el valor (o no)
                resultado = cursor.fetchone()

                if resultado == None:
                    print("No se enocntraron coincidencias")
                    print("¿Desea Registrarse?")
                    print("1. SI")
                    print("0. NO")
                    opcion = input("Opcion: ")
                    if opcion == "0":
                        break
                else:
                    # Desempaquetamos la tupla
                    id_usuario, nombre_usuario, correo_usuario, contraseña_usuario = (
                        resultado
                    )

                    if correo_usuario == correo and contraseña_usuario == contraseña:
                        print("Exito")

                    ##

                    # TERMINAR LA VERIFI CACION CON CONTRASEÑA

                    ##
