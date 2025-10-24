from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    role = "admin"
    notes = [
        {"id": 1, "title": "Nota 1", "content": "Contenido de la nota 1"},
        {"id": 2, "title": "Nota 2", "content": "Contenido de la nota 2"},
        {"id": 3, "title": "Nota 3", "content": "Contenido de la nota 3"},
    ]
    return render_template('home.html', role=role, notes=notes)

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

