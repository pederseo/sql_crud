import psycopg2

class Conect:
    conexion = psycopg2.connect(
        dbname='POKEMON',
        user='postgres',
        password='admin',
        host='localhost'
    )