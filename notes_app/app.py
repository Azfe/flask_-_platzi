from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_FILE_PATH = os.path.join(os.path.dirname(__file__), 'notes.sqlite')

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"

@app.route('/')
# @app.route('/home')
def home():
    role = "admin"
    
    notes = Note.query.all()
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

@app.route('/confirmacion', methods=['GET', 'POST'])
def confirmation():
    print(request)
    # return "Prueba de confirmación"
    title = request.args.get('title')
    content = request.args.get('content')
    return render_template('confirmation.html', title=title, content=content)

@app.route('/crear-nota', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form.get('title-note')
        content = request.form.get('content-note')
        
        note_db = Note(
            title=title,
            content=content
        )
        
        db.session.add(note_db)
        db.session.commit()
        
        print(f"Nota creada: {title} - {content}")
        return redirect(
            url_for('confirmation', title=title, content=content)
        )
    return render_template('note_form.html')

@app.route('/editar-nota/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':        
        title = request.form.get('title-note', 'Sin título')
        content = request.form.get('content-note', 'Sin contenido')
        
        note.title = title
        note.content = content
        
        db.session.commit()
        
        return redirect(url_for('home'))        
    return render_template('edit_note.html', note=note)

@app.route('/eliminar-nota/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('home')) # esto genera un 302

# if __name__ == '__main__':
#     app.run(debug=True) # Debug mode ON
