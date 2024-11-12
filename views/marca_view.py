from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.marca_service import MarcaService
from repositories.marca_repositories import MarcaRepositories
from schemas import MarcaSchema, EquipoSchema
from models import Marca
from forms import MarcaForm

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/marca', methods=['POST', 'GET'])
@jwt_required()
def marcas():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear marcas"}), 403

    marca_service = MarcaService(MarcaRepositories())

    if request.method == 'POST':
        data = request.get_json() 
        nombre = data.get('nombre')
        if not nombre:
            return jsonify({"Mensaje": "El nombre de la marca es obligatorio"}), 400

        nueva_marca = marca_service.create(nombre)
        marca_schema = MarcaSchema()

        return jsonify({
            "Mensaje": "Marca creada exitosamente",
            "marca": marca_schema.dump(nueva_marca)
        }), 201

@marca_bp.route("/marca_list", methods=['GET'])
@jwt_required()
def marcas_list():
    marca_service = MarcaService(MarcaRepositories())
    marcas = marca_service.get_all()

    marca_schema = MarcaSchema(many=True)
    marcas_serializadas = marca_schema.dump(marcas)

    return jsonify({'marcas': marcas_serializadas})


@marca_bp.route("/marca/<id>/editar", methods=['PUT'])
@jwt_required()
def marca_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar marca"}), 403

    marca = Marca.query.get_or_404(id)

    if request.method == 'PUT':
        nombre = request.json.get('nombre')
        
        if not nombre:
            return jsonify({"Mensaje": "El campo 'nombre' es obligatorio"}), 400
        marca.nombre = nombre
        
        db.session.commit()

        marca_schema = MarcaSchema()
        marca_serializada = marca_schema.dump(marca)

        return jsonify({
            "Mensaje": "Marca editada con éxito",
            'marca': marca_serializada
        }), 200

    marca_schema = MarcaSchema()
    marca_serializada = marca_schema.dump(marca)

    return jsonify({'marca': marca_serializada})


@marca_bp.route('/marca/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_marca(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar usuarios"}), 403

    marca = Marca.query.get(id)
    if not marca:
        return jsonify({"Mensaje": "Marca no encontrada"}), 404

    try:
        db.session.delete(marca)
        db.session.commit()
        return jsonify({"Mensaje": "Marca eliminada correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar la marca", "Error": str(e)}), 500
