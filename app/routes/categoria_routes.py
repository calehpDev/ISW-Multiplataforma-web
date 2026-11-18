from flask import Blueprint, render_template, request, redirect, url_for
from app.models.categoria import CategoriaModel

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        estado = 1 if 'estado' in request.form else 0
        CategoriaModel.insertar(request.form['nombre'], request.form['descripcion'], estado)
        return redirect(url_for('categoria_bp.index'))
    categorias = CategoriaModel.get_all()
    return render_template('categorias/index.html', categorias=categorias)

@categoria_bp.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        estado = 1 if 'estado' in request.form else 0
        CategoriaModel.actualizar(id, request.form['nombre'], request.form['descripcion'], estado)
        return redirect(url_for('categoria_bp.index'))
    categoria = CategoriaModel.get_by_id(id)
    return render_template('categorias/editar.html', categoria=categoria)

@categoria_bp.route('/categorias/eliminar/<int:id>')
def eliminar(id):
    CategoriaModel.eliminar(id)
    return redirect(url_for('categoria_bp.index'))