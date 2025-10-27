from flask import Flask, request
from config import Config
from models import db
from notes.routes import notes_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(notes_bp)

@app.route('/acerca-de')
def about():
    return "Esto es una app de notas."

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Formulario de contacto enviado.", 201
    return "Página de contacto"



# @app.route('/api/info') # Ruta creada para devolver información de la API en formato JSON
# def api_info():
#     data = {
#         "nombre": "App de Notas",
#         "version": "1.0.0",
#         "author": "Azfe",
#         "description": "API para la aplicación de notas"
#     }
#     return jsonify(data), 200

# if __name__ == '__main__':
#     app.run(debug=True) # Debug mode ON
