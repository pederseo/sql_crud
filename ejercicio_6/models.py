import psycopg2
import psycopg2.extras
from config import Conect
import random

conn = Conect.conexion

def agregar_entrenadores(nombre, medallas):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('INSERT INTO entrenadores (nombre, medallas) VALUES (%s, %s)', (nombre, medallas))
    conn.commit()
    cursor.close()

def mostrar_entrenadores():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM entrenadores")
    lista_entrenadores = cursor.fetchall()
    cursor.close()
    return lista_entrenadores

def actualizar_entrenador(id, nombre, medallas):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("UPDATE entrenadores SET nombre = %s, medallas = %s WHERE id = %s",(nombre, medallas, id))
    conn.commit()
    cursor.close()

def eliminar_entrenador(id):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("DELETE FROM entrenadores WHERE id = %s", (id,))
    conn.commit()
    cursor.close()

#_______________________________________________________________________________________________________________________________
def mostrar_pokemones():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM pokemones")
    lista_pokemones = cursor.fetchall()
    cursor.close()
    return lista_pokemones

def crear_equipos(entrenador, pokemon1, pokemon2):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('INSERT INTO equipos (id_entrenador, id_pokemon1, id_pokemon2) VALUES (%s, %s, %s)', (entrenador, pokemon1, pokemon2))
    conn.commit()
    cursor.close()


def agregar_resultados(id_entrenador1,id_entrenador2):
    # Crear un cursor con DictCursor para obtener resultados como diccionarios
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Ejecutar las consultas para obtener los nombres de los entrenadores
    cursor.execute(f'SELECT nombre FROM entrenadores WHERE id = {id_entrenador1};')
    entrenador1 = cursor.fetchone()['nombre']

    cursor.execute(f'SELECT nombre FROM entrenadores WHERE id = {id_entrenador2};')
    entrenador2 = cursor.fetchone()['nombre']

    # Elegir un ganador aleatoriamente entre los dos entrenadores
    ganador = random.choice([entrenador1, entrenador2])

    # Insertar los resultados en la tabla resultados
    cursor.execute('INSERT INTO resultados (equipo1, equipo2, ganador) VALUES (%s, %s, %s)', (entrenador1, entrenador2, ganador))

    # Confirmar los cambios
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

#__________________________________________________________________________________________________________________________________
def mostrar_resultados():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM resultados")
    lista_resultados = cursor.fetchall()
    cursor.close()
    return lista_resultados