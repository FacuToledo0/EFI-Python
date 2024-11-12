from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.accesorio_service import AccesorioService
from repositories.accesorio_repositories import AccesorioRepositories
from schemas import AccesorioSchema, EquipoSchema
from models import Accesorio
from forms import AccesorioForm

accesorio_bp = Blueprint('accesorio', __name__)

@accesorio_bp.route('/accesorio', methods=['POST', 'GET'])
@jwt_required()
def accesorios():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear accesorios"}), 403

    accesorio_service = AccesorioService(AccesorioRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        tipo_accesorio = data.get('tipo_accesorio')  

        if not tipo_accesorio:
            return jsonify({"Mensaje": "El nombre del accesorio es obligatorio"}), 400

        nuevo_accesorio = accesorio_service.create(tipo_accesorio)
        accesorio_schema = AccesorioSchema()

        return jsonify({
            "Mensaje": "Accesorio creado exitosamente",
            "accesorio": accesorio_schema.dump(nuevo_accesorio)
        }), 201
    
@accesorio_bp.route("/accesorio_list", methods=['GET'])
@jwt_required()
def accesorios_list():
    accesorio_service = AccesorioService(AccesorioRepositories())
    accesorios = accesorio_service.get_all()

    accesorio_schema = AccesorioSchema(many=True)
    accesorios_serializadas = accesorio_schema.dump(accesorios)

    return jsonify({'accesorios': accesorios_serializadas})

@accesorio_bp.route("/accesorio/<id>/editar", methods=['PUT'])
@jwt_required()
def accesorio_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar accesorio"}), 403

    accesorio = Accesorio.query.get_or_404(id)

    if request.method == 'PUT':

        tipo_accesorio = request.json.get('tipo_accesorio')
        
        if not tipo_accesorio:
            return jsonify({"Mensaje": "El campo 'tipo_accesorio' es obligatorio"}), 400
        accesorio.tipo_accesorio = tipo_accesorio
        
        db.session.commit()

        accesorio_schema = AccesorioSchema()
        accesorio_serializada = accesorio_schema.dump(accesorio)

        return jsonify({
            "Mensaje": "Accesorio editado con éxito",
            'accesorio': accesorio_serializada
        }), 200

    accesorio_schema = AccesorioSchema()
    accesorio_serializada = accesorio_schema.dump(accesorio)

    return jsonify({'accesorio': accesorio_serializada})

@accesorio_bp.route('/accesorio/<int:id>/borrar', methods=['DELETE'])
@jwt_required()
def borrar_accesorio(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el administrador puede eliminar accesorios"}), 403

    accesorio = Accesorio.query.get(id)
    if not accesorio:
        return jsonify({"Mensaje": "Accesorio no encontrado"}), 404

    try:
        db.session.delete(accesorio)
        db.session.commit()
        return jsonify({"Mensaje": "Accesorio eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar el accesorio", "Error": str(e)}), 500
    