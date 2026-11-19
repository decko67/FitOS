import sqlite3

with sqlite3.connect("gym_db") as conexion:
    cursor = conexion.cursor()

    def registrar_usuario(nombre, correo, contraseña):
        query = """
        INSERT INTO Users(nombre,correo,password)
        VALUES(?,?,?);
        """

        user_data = (nombre, correo, contraseña)

        try:
            cursor.execute(query, user_data)

            conexion.commit()

            return True

        except sqlite3.IntegrityError:
            return False

    def limpiarBD():
        query = """
        ALTER TABLE Users
        ADD UNIQUE (correo;
        """
        cursor.execute(query)

        conexion.commit()

        return True

    def buscar_usuraio(correo, contraseña):
        query = """
        SELECT correo,password
        FROM Users 
        WHERE correo = ?
        AND password = ?;
        """
        user_data = (correo, contraseña)

        cursor.execute(query, user_data)

        conexion.commit()

        resultado = cursor.fetchone()

        return resultado
