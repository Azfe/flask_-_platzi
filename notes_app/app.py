from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/acerca-de')
def about():
    return "Esto es una app de notas."

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Formulario de contacto enviado.", 201
    return "Página de contacto"

@app.route('/api/info')
def api_info():
    data = {
        "nombre": "App de Notas",
        "version": "1.0.0",
        "author": "Azfe",
        "description": "API para la aplicación de notas"
    }
    return jsonify(data), 200

# if __name__ == '__main__':
#     app.run(debug=True) # Debug mode ON

