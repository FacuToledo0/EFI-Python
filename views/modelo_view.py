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
        data = request.get_json()  # Obtener los datos en formato JSON
        nombre = data.get('nombre')  # Obtener el nombre de la marca desde el cuerpo de la solicitud

        if not nombre:
            return jsonify({"Mensaje": "El nombre de la marca es obligatorio"}), 400

        print(f"Creando nueva marca con nombre: {nombre}")  # Log de creación

        nuevo_modelo = modelo_service.create(nombre)
        modelo_schema = ModeloSchema()

        # Devolver directamente una respuesta JSON en lugar de hacer una redirección
        return jsonify({
            "Mensaje": "Marca creada exitosamente",
            "modelo": modelo_schema.dump(nuevo_modelo)
        }), 201

@modelo_bp.route("/modelo_list", methods=['GET'])
@jwt_required()
def modelos_list():
    # Obtener todas las marcas de la base de datos
    modelo_service = ModeloService(ModeloRepositories())
    modelos = modelo_service.get_all()

    # Serializar las marcas obtenidas
    modelo_schema = ModeloSchema(many=True)
    modelos_serializadas = modelo_schema.dump(modelos)

    # Retornar la lista de marcas como respuesta JSON
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