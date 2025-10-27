from flask import(         
    redirect, 
    render_template, 
    request, url_for,
    Blueprint,
    flash
)
from models import Note, db

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/')
# @app.route('/home')
def home():
    role = "admin"
    
    notes = Note.query.all()
    return render_template('home.html', role=role, notes=notes)

@notes_bp.route('/confirmacion', methods=['GET', 'POST'])
def confirmation():
    print(request)
    # return "Prueba de confirmación"
    title = request.args.get('title')
    content = request.args.get('content')
    return render_template('confirmation.html', title=title, content=content)

@notes_bp.route('/crear-nota', methods=['GET', 'POST'])
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
        flash("Nota creada exitosamente.", "success")        
        print(f"Nota creada: {title} - {content}")
        return redirect(
            url_for('notes.home')
            # url_for('notes.confirmation', title=title, content=content)
        )
    return render_template('note_form.html')

@notes_bp.route('/editar-nota/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':        
        title = request.form.get('title-note', 'Sin título')
        content = request.form.get('content-note', 'Sin contenido')
        
        note.title = title
        note.content = content
        
        db.session.commit()
        
        return redirect(url_for('notes.home'))        
    return render_template('edit_note.html', note=note)

@notes_bp.route('/eliminar-nota/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('notes.home')) # esto genera un 302