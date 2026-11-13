import sqlite3

with sqlite3.connect("gym_db") as conexion:
    cursor = conexion.cursor()
    while True:
        print("1.Agregar un usuario")
        print("0. SAlir")
        opcion = input("Ingresa el numero de opcion: ")

        match (opcion):
            case "1":
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contraseña = input("Contraseña: ")

                query = """
                   INSERT INTO Users(nombre,correo,contraseña)
                   VALUES(?,?,?);
                        """

                user_data = (nombre, correo, contraseña)

                cursor.execute(query, user_data)

                conexion.commit()

                print("Usuario agregado de manera Correcta")

            case "0":
                break
