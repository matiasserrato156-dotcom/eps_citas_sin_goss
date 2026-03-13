from database import get_connection


def registrar_cita(documento, medico, tipo_cita, fecha, hora, direccion):
    conn   = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO citas (documento, medico, tipo_cita, fecha, hora, direccion)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (documento, medico, tipo_cita, fecha, hora, direccion))
    conn.commit()
    cita_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return cita_id


def obtener_citas_paciente(documento):
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """
        SELECT c.*, p.nombre, p.apellido
        FROM   citas c
        JOIN   pacientes p ON c.documento = p.documento
        WHERE  c.documento = %s
        ORDER  BY c.fecha DESC, c.hora DESC
    """
    cursor.execute(sql, (documento,))
    citas = cursor.fetchall()
    cursor.close()
    conn.close()
    return citas


def obtener_cita(cita_id):
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """
        SELECT c.*, p.nombre, p.apellido
        FROM   citas c
        JOIN   pacientes p ON c.documento = p.documento
        WHERE  c.id = %s
    """
    cursor.execute(sql, (cita_id,))
    cita = cursor.fetchone()
    cursor.close()
    conn.close()
    return cita


def actualizar_cita(cita_id, medico, tipo_cita, fecha, hora):
    conn   = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE citas
             SET medico=%s, tipo_cita=%s, fecha=%s, hora=%s
             WHERE id=%s"""
    cursor.execute(sql, (medico, tipo_cita, fecha, hora, cita_id))
    conn.commit()
    cursor.close()
    conn.close()


def eliminar_cita(cita_id):
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE id = %s", (cita_id,))
    conn.commit()
    cursor.close()
    conn.close()
