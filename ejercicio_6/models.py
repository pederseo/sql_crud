# HERRAMIENTAS

import psycopg2
import psycopg2.extras
from config import Conect
import random

#________________________________________QUERYS______________________________________________________

conn = Conect.conexion # traemos nuestra coneccion

def agregar_entrenadores(nombre, medallas):
    '''funcion para agregar entrenadores y medallas a la base de datos entrenadores'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('INSERT INTO entrenadores (nombre, medallas) VALUES (%s, %s)', (nombre, medallas))
    conn.commit()
    cursor.close()

def mostrar_entrenadores():
    '''funcion extraer los datos en una lista para llevar al front'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM entrenadores")
    lista_entrenadores = cursor.fetchall()
    cursor.close()
    return lista_entrenadores

def actualizar_entrenador(id, nombre, medallas):
    '''funcion actualizar los datos de la tabla entrenadores con datos nuevos'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("UPDATE entrenadores SET nombre = %s, medallas = %s WHERE id = %s",(nombre, medallas, id))
    conn.commit()
    cursor.close()

def eliminar_entrenador(id):
    '''funcion eliminar los datos de la tabla entrenadores'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("DELETE FROM entrenadores WHERE id = %s", (id,))
    conn.commit()
    cursor.close()

#_______________________________________________________________________________________________________________________________
def mostrar_pokemones():
    '''funcion extraer los datos de la tabla pokemon para cargar en una lista y mandar al front'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM pokemones")
    lista_pokemones = cursor.fetchall()
    cursor.close()
    return lista_pokemones

def crear_equipos(entrenador, pokemon1, pokemon2):
    '''funcion cargar datos a la tabla intermedio "equipos" donde relacionamos entrenadores con sus pokemones'''

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('INSERT INTO equipos (id_entrenador, id_pokemon1, id_pokemon2) VALUES (%s, %s, %s)', (entrenador, pokemon1, pokemon2))
    conn.commit()
    cursor.close()


def agregar_resultados(id_entrenador1,id_entrenador2):
    '''funcion agregar los resultados de las batallas a la tabla "batallas" '''


    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(f'SELECT nombre FROM entrenadores WHERE id = {id_entrenador1};')
    entrenador1 = cursor.fetchone()['nombre']

    cursor.execute(f'SELECT nombre FROM entrenadores WHERE id = {id_entrenador2};')
    entrenador2 = cursor.fetchone()['nombre']

    ganador = random.choice([entrenador1, entrenador2])
    cursor.execute('INSERT INTO resultados (equipo1, equipo2, ganador) VALUES (%s, %s, %s)', (entrenador1, entrenador2, ganador))
    conn.commit()
    cursor.close()

#__________________________________________________________________________________________________________________________________
def mostrar_resultados():
    '''funcion extraer los datos de la tabla batallas para cargar en una lista y mandar al front'''
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM resultados")
    lista_resultados = cursor.fetchall()
    cursor.close()
    return lista_resultados
