from conexion import conectar_bd
import pandas as pd

def crear_encuesta(connection, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                   bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
                   problemas_digestivos, tension_alta, dolor_cabeza):
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(idEncuesta) FROM ENCUESTA")
    max_id = cursor.fetchone()[0]
    id_encuesta = (max_id + 1) if max_id else 1
    query = """INSERT INTO ENCUESTA (idEncuesta, edad, sexo, BebidasSemana, CervezasSemana, BebidasFinSemana,
                                     BebidasDestiladasSemana, VinosSemana, PerdidasControl, 
                                     DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, 
              bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
              problemas_digestivos, tension_alta, dolor_cabeza)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    print("Encuesta creada exitosamente.")

def leer_encuestas(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ENCUESTA")
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def actualizar_encuesta(connection, id_encuesta, **kwargs):
    cursor = connection.cursor()
    campos = [f"{key} = %s" for key, value in kwargs.items() if value is not None]
    valores = [value for value in kwargs.values() if value is not None]
    if campos:
        query = f"UPDATE ENCUESTA SET {', '.join(campos)} WHERE idEncuesta = %s"
        cursor.execute(query, valores + [id_encuesta])
        connection.commit()
        print("Encuesta actualizada exitosamente.")
    cursor.close()

def eliminar_encuesta(connection, id_encuesta):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta = %s", (id_encuesta,))
    connection.commit()
    cursor.close()
    print("Encuesta eliminada exitosamente.")

def exportar_a_excel(connection, archivo="encuestas.xlsx"):
    df = pd.read_sql("SELECT * FROM ENCUESTA", connection)
    df.to_excel(archivo, index=False)
    print(f"Datos exportados a {archivo}")

