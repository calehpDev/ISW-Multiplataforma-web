from app.database import get_connection

class CategoriaModel:
    @classmethod
    def get_all(cls):
        conexion = get_connection()
        categorias = []
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Categoria")
                categorias = cursor.fetchall()
        finally:
            conexion.close()
        return categorias

    @classmethod
    def get_by_id(cls, id_categoria):
        conexion = get_connection()
        categoria = None
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Categoria WHERE id_categoria = %s", (id_categoria,))
                categoria = cursor.fetchone()
        finally:
            conexion.close()
        return categoria

    @classmethod
    def insertar(cls, nombre, descripcion, estado=1):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO Categoria (nombre, descripcion, estado) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, descripcion, estado))
            conexion.commit()
        finally:
            conexion.close()

    @classmethod
    def actualizar(cls, id_categoria, nombre, descripcion, estado):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                sql = "UPDATE Categoria SET nombre = %s, descripcion = %s, estado = %s WHERE id_categoria = %s"
                cursor.execute(sql, (nombre, descripcion, estado, id_categoria))
            conexion.commit()
        finally:
            conexion.close()

    @classmethod
    def eliminar(cls, id_categoria):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM Categoria WHERE id_categoria = %s", (id_categoria,))
            conexion.commit()
        except Exception as ex:
            print(f"No se puede eliminar la categoría (puede estar en uso): {ex}")
        finally:
            conexion.close()