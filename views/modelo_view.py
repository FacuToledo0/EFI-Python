from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.modelo_service import ModeloService
from repositories.modelo_repositories import ModeloRepositories
from schemas import ModeloSchema, EquipoSchema
from models import Modelo
from forms import ModeloForm

modelo_bp = Blueprint('modelo', __name__)

@modelo_bp.route('/modelo', methods=['POST', 'GET'])
@jwt_required()
def modelos():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear marcas"}), 403

    modelo_service = ModeloService(ModeloRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        nombre = data.get('nombre')  

        if not nombre:
            return jsonify({"Mensaje": "El nombre del modelo es obligatorio"}), 400

        nuevo_modelo = modelo_service.create(nombre)
        modelo_schema = ModeloSchema()

        return jsonify({
            "Mensaje": "Modelo creado exitosamente",
            "modelo": modelo_schema.dump(nuevo_modelo)
        }), 201

@modelo_bp.route("/modelo_list", methods=['GET'])
@jwt_required()
def modelos_list():
    modelo_service = ModeloService(ModeloRepositories())
    modelos = modelo_service.get_all()

    modelo_schema = ModeloSchema(many=True)
    modelos_serializadas = modelo_schema.dump(modelos)

    return jsonify({'modelos': modelos_serializadas})


@modelo_bp.route("/modelo/<id>/editar", methods=['PUT'])
@jwt_required()
def proveedor_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar el modelo"}), 403

    modelo = Modelo.query.get_or_404(id)

    if request.method == 'PUT':
        nombre = request.json.get('nombre')
        
        if not nombre:
            return jsonify({"Mensaje": "El campo 'nombre' es obligatorio"}), 400
        modelo.nombre = nombre

        db.session.commit()

        modelo_schema = ModeloSchema()
        modelo_serializada = modelo_schema.dump(modelo)

        return jsonify({
            "Mensaje": "El modelo esta editado con éxito",
            'modelo': modelo_serializada
        }), 200

    modelo_schema = ModeloSchema()
    modelo_serializada = modelo_schema.dump(modelo)

    return jsonify({'modelo': modelo_serializada})


@modelo_bp.route('/modelo/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_modelo(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar modelos"}), 403

    modelo = Modelo.query.get(id)
    if not modelo:
        return jsonify({"Mensaje": "Modelo no encontrado"}), 404

    try:
        db.session.delete(modelo)
        db.session.commit()
        return jsonify({"Mensaje": "Modelo eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar el modelo", "Error": str(e)}), 500