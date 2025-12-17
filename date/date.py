# app.py - VERSIÓN COMPLETAMENTE CORREGIDA
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Frases casuales y amigables
MENSAJES = [
    "Pues, me gustaría conocerte mejor para serte sincero...",
    "ya que me pareces una persona muy interesante y linda",
    "Y creo que podríamos pasar un buen rato, asi que...",
    "¿Te gustaría salir esta semana conmigo?"

]

RESPUESTAS_POSITIVAS = [
    "¿Te parece bien el miércoles después del trabajo?"
]

@app.route('/')
def home():
    return render_template('cafe.html')

@app.route('/siguiente_paso', methods=['POST'])
def siguiente_paso():
    data = request.get_json()
    paso = data.get('paso', 0) if data else 0
    
    if paso < len(MENSAJES):
        return jsonify({
            'mensaje': MENSAJES[paso],
            'siguiente': True,
            'paso_actual': paso
        })
    
    return jsonify({'final': True})

@app.route('/responder', methods=['POST'])
def responder():
    data = request.get_json()
    respuesta = data.get('respuesta') if data else None
    
    if respuesta == 'si':
        return jsonify({
            'mensaje': random.choice(RESPUESTAS_POSITIVAS),
            'mostrar_calendario': True
        })
    elif respuesta == 'talvez':
        return jsonify({
            'mensaje': 'Entiendo, ¿y si empezamos con una videollamada corta primero?',
            'mostrar_opciones': True
        })
    else:
        return jsonify({
            'mensaje': 'No hay problema, seguimos charlando por aquí cuando quieras 😊',
            'final': True
        })

if __name__ == '__main__':
    app.run(debug=True, port=5080)