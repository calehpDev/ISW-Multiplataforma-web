from app.database import get_connection

class MedicamentoModel:
    @classmethod
    def get_all(cls):
        conexion = get_connection()
        medicamentos = []
        try:
            with conexion.cursor() as cursor:
                sql = """
                    SELECT m.*, c.nombre AS categoria_nombre 
                    FROM Medicamento m 
                    LEFT JOIN Categoria c ON m.id_categoria = c.id_categoria
                """
                cursor.execute(sql)
                medicamentos = cursor.fetchall()
        finally:
            conexion.close()
        return medicamentos

    @classmethod
    def get_by_id(cls, id_medicamento):
        conexion = get_connection()
        medicamento = None
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM Medicamento WHERE id_medicamento = %s", (id_medicamento,))
                medicamento = cursor.fetchone()
        finally:
            conexion.close()
        return medicamento

    @classmethod
    def insertar(cls, nombre, precio, stock, id_categoria):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO Medicamento (nombre, precio, stock, id_categoria) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nombre, precio, stock, id_categoria))
            conexion.commit()
        finally:
            conexion.close()

    @classmethod
    def actualizar(cls, id_medicamento, nombre, precio, stock, id_categoria):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                sql = """UPDATE Medicamento 
                         SET nombre = %s, precio = %s, stock = %s, id_categoria = %s 
                         WHERE id_medicamento = %s"""
                cursor.execute(sql, (nombre, precio, stock, id_categoria, id_medicamento))
            conexion.commit()
        finally:
            conexion.close()

    @classmethod
    def eliminar(cls, id_medicamento):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM Medicamento WHERE id_medicamento = %s", (id_medicamento,))
            conexion.commit()
        finally:
            conexion.close()