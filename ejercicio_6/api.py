import requests
import psycopg2

# conexion con a la base de datos
conn = psycopg2.connect(
    dbname= 'POKEMON', 
    user="postgres", 
    password= "admin",
    host="localhost")

cursor = conn.cursor()

# funcion para acceder a la api de pokemon
def cargar_pokemon(id):    
    api_url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        name = data.get('name')
        number = data.get('id')
        type = data['types'][0]['type']['name']
        moves = data['moves'][0]['move']['name']
        front = data['sprites']['front_default']
        back = data['sprites']['back_default']
        
        print(name)
        print(number)
        print(type)
        print(moves)
        print(front)
        print(back)

# consulta sql para agregar los datos a la base de datos
    cursor.execute("""
    INSERT INTO pokemones (nombre, tipo, habilidad, numero, front, back)
    VALUES (%s, %s, %s, %s, %s, %s)
    """,(name, type, moves, number, front, back))

    conn.commit()

# cargar los pokemones de a uno
for i in range (1,152):
    cargar_pokemon(i)

cursor.close()
conn.close()