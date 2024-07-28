from flask import Flask, render_template, request, redirect, url_for
import psycopg2.extras
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#_________________________________________________________________________________________


@app.route('/registro', methods=['POST', 'GET'])
def registro():
    if request.method == 'POST':
        if 'id' in request.form:
            # Se actualiza un entrenador existente
            id = request.form['id']
            nombre = request.form['nombre']
            medallas = request.form['medallas']
            actualizar_entrenador(id, nombre, medallas)
        else:
            # Se agrega un nuevo entrenador
            nombre = request.form['nombre']
            medallas = request.form['medallas']
            agregar_entrenadores(nombre, medallas)

    lista_entrenadores = mostrar_entrenadores()
    return render_template('registro.html', lista_entrenadores=lista_entrenadores)

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_entrenador_route(id):
    eliminar_entrenador(id)
    return redirect(url_for('registro'))
#__________________________________________________________________________________________



@app.route('/batalla', methods=['GET', 'POST'])
def batalla():
    if request.method == 'POST':
        entrenador1_id = request.form['entrenador1']
        pokemon1_1_id = request.form['pokemon1-1']
        pokemon1_2_id = request.form['pokemon1-2']
        crear_equipos(entrenador1_id, pokemon1_1_id, pokemon1_2_id)

        entrenador2_id = request.form['entrenador2']
        pokemon2_1_id = request.form['pokemon2-1']
        pokemon2_2_id = request.form['pokemon2-2']
        crear_equipos(entrenador2_id, pokemon2_1_id, pokemon2_2_id)

        agregar_resultados(entrenador1_id,entrenador2_id)
        return redirect(url_for('resultados'))

    lista_entrenadores = mostrar_entrenadores()
    lista_pokemones = mostrar_pokemones()
    return render_template('batalla.html', lista_entrenadores=lista_entrenadores, lista_pokemones=lista_pokemones)



#_________________________________________________________________________________________



@app.route('/resultados')
def resultados():
    lista_resultados = mostrar_resultados()
    return render_template('resultados.html', lista_resultados=lista_resultados)

if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/agregar_entrenador', methods=['POST'])
# def agregar_entrenador():
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         cursor.execute("INSERT INTO entrenadores (nombre) VALUES (%s)", (nombre,))
#         conn.commit()
#         flash('Entrenador agregado', 'success')
#         return redirect(url_for('entrenadores'))  


# @app.route('/editar/<id>', methods = ['POST', 'GET'])
# def editar_entrenador (id):
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cursor.execute('SELECT * FROM entrenadores WHERE id = %s', (id,))
#     entrenador = cursor.fetchall() #recupera todos los resultados de la consulta
#     cursor.close() #cierra el cursor
#     return render_template('editar.html', entrenador = entrenador[0])


# @app.route('/actualizar/<id>', methods = ['POST'])
# def actualizar_entrenador(id):
#     if request.method == 'POST':
#         nombre = request.form['nombre']
         
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         cursor.execute (""" 
#                     UPDATE entrenadores 
#                     SET nombre = %s
#                     WHERE id = %s """, (nombre, id))
#         flash('Entrenador actualizado', 'success')
#         conn.commit()
#         return redirect(url_for('entrenadores'))
    
 
# @app.route('/borrar/<string:id>', methods = ['POST','GET'])
# def borrar_entrenador(id):
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
#     cursor.execute('DELETE FROM entrenadores WHERE id = {0}'.format(id))
#     conn.commit()
#     flash('Entrenador borrado', 'success')
#     return redirect(url_for('entrenadores'))





