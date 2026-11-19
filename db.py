import sqlite3

with sqlite3.connect("gym_db") as conexion:
    cursor = conexion.cursor()

    def registrar_usuario(nombre, correo, contraseña):
        query = """
        INSERT INTO Users(nombre,correo,password)
        VALUES(?,?,?);
        """

        user_data = (nombre, correo, contraseña)

        cursor.execute(query, user_data)

        conexion.commit()

        return True

    def limpiarBD():
        query = """
        ALTER TABLE Users
        ADD UNIQUE (correo;
        """
        cursor.execute(query)

        conexion.commit()

        return True
