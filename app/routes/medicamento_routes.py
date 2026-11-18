from flask import Blueprint, render_template, request, redirect, url_for
from app.models.medicamento import MedicamentoModel
from app.models.categoria import CategoriaModel

medicamento_bp = Blueprint('medicamento_bp', __name__)

@medicamento_bp.route('/')
def index():
    medicamentos = MedicamentoModel.get_all()
    return render_template('inicio/index.html', medicamentos=medicamentos)

@medicamento_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        MedicamentoModel.insertar(
            request.form['nombre'],
            request.form['precio'],
            request.form['stock'],
            request.form['id_categoria']
        )
        return redirect(url_for('medicamento_bp.index'))
    categorias = CategoriaModel.get_all()
    return render_template('inicio/crear.html', categorias=categorias)

@medicamento_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        MedicamentoModel.actualizar(
            id,
            request.form['nombre'],
            request.form['precio'],
            request.form['stock'],
            request.form['id_categoria']
        )
        return redirect(url_for('medicamento_bp.index'))
    medicamento = MedicamentoModel.get_by_id(id)
    categorias = CategoriaModel.get_all()
    return render_template('inicio/editar.html', medicamento=medicamento, categorias=categorias)

@medicamento_bp.route('/eliminar/<int:id>')
def eliminar(id):
    MedicamentoModel.eliminar(id)
    return redirect(url_for('medicamento_bp.index'))