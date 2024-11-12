from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.proveedor_service import ProveedorService
from repositories.proveedor_repositories import ProveedorRepositories
from schemas import ProveedorSchema, EquipoSchema
from models import Proveedor
from forms import ProveedorForm

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/proveedor', methods=['POST'])
@jwt_required()
def proveedores():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear proveedores"}), 403

    proveedor_service = ProveedorService(ProveedorRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        nombre_proveedor = data.get('nombre_proveedor')
        contacto = data.get('contacto')

        if not nombre_proveedor:
            return jsonify({"Mensaje": "El nombre del proveedor es obligatorio"}), 400
        
        if not contacto:
            return jsonify({"Mensaje": "El contacto es obligatorio"}), 400

        nuevo_proveedor = proveedor_service.create(nombre_proveedor, contacto)
        proveedor_schema = ProveedorSchema()

        return jsonify({
            "Mensaje": "Proveedor creado exitosamente",
            "proveedor": proveedor_schema.dump(nuevo_proveedor)
        }), 201

@proveedor_bp.route("/proveedor_list", methods=['GET'])
@jwt_required()
def proveedores_list():
    proveedor_service = ProveedorService(ProveedorRepositories())
    proveedores = proveedor_service.get_all()

    proveedor_schema = ProveedorSchema(many=True)
    proveedores_serializadas = proveedor_schema.dump(proveedores)

    return jsonify({'proveedores': proveedores_serializadas})


@proveedor_bp.route("/proveedor/<id>/editar", methods=['PUT'])
@jwt_required()
def proveedor_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar el proveedor"}), 403

    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'PUT':
        nombre_proveedor = request.json.get('nombre_proveedor')
        contacto = request.json.get('contacto')
        
        if not nombre_proveedor:
            return jsonify({"Mensaje": "El campo 'nombre_proveedor' es obligatorio"}), 400
        proveedor.nombre_proveedor = nombre_proveedor

        if not contacto:
            return jsonify({"Mensaje": "El campo 'contacto' es obligatorio"}), 400
        proveedor.contacto = contacto
        
        db.session.commit()

        proveedor_schema = ProveedorSchema()
        proveedor_serializada = proveedor_schema.dump(proveedor)

        return jsonify({
            "Mensaje": "El proveedor esta editado con éxito",
            'proveedor': proveedor_serializada
        }), 200

    proveedor_schema = ProveedorSchema()
    proveedor_serializada = proveedor_schema.dump(proveedor)

    return jsonify({'proveedor': proveedor_serializada})

@proveedor_bp.route('/proveedor/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_proveedor(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar proveedores"}), 403

    proveedor = Proveedor.query.get(id)
    if not proveedor:
        return jsonify({"Mensaje": "Proveedor no encontrado"}), 404

    try:
        db.session.delete(proveedor)
        db.session.commit()
        return jsonify({"Mensaje": "Proveedor eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar el proveedor", "Error": str(e)}), 500
