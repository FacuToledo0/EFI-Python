from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.fabricante_service import FabricanteService
from repositories.fabricante_repositories import FabricanteRepositories
from schemas import FabricanteSchema, EquipoSchema
from models import Fabricante
from forms import FabricanteForm

fabricante_bp = Blueprint('fabricante', __name__)

@fabricante_bp.route('/fabricante', methods=['POST'])
@jwt_required()
def fabricantes():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear fabricantes"}), 403

    fabricante_service = FabricanteService(FabricanteRepositories())

    if request.method == 'POST':
        data = request.get_json()  
        nombre_fabricante = data.get('nombre_fabricante')
        pais_origen = data.get('pais_origen')

        if not nombre_fabricante:
            return jsonify({"Mensaje": "El nombre del fabricante es obligatorio"}), 400
        
        if not pais_origen:
            return jsonify({"Mensaje": "El país es obligatorio"}), 400

        nuevo_fabricante = fabricante_service.create(nombre_fabricante, pais_origen=pais_origen)
        fabricante_schema = FabricanteSchema()

        return jsonify({
            "Mensaje": "Fabricante creado exitosamente",
            "fabricante": fabricante_schema.dump(nuevo_fabricante)
        }), 201
    

@fabricante_bp.route("/fabricante_list", methods=['GET'])
@jwt_required()
def fabricantes_list():
    fabricante_service = FabricanteService(FabricanteRepositories())
    fabricantes = fabricante_service.get_all()

    fabricante_schema = FabricanteSchema(many=True)
    fabricantes_serializadas = fabricante_schema.dump(fabricantes)

    return jsonify({'fabricantes': fabricantes_serializadas})


@fabricante_bp.route("/fabricante/<id>/editar", methods=['PUT'])
@jwt_required()
def fabricante_editar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para editar el fabricante"}), 403

    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'PUT':
        nombre_fabricante = request.json.get('nombre_fabricante')
        pais_origen = request.json.get('pais_origen')
        
        if not nombre_fabricante:
            return jsonify({"Mensaje": "El campo 'nombre_fabricante' es obligatorio"}), 400
        fabricante.nombre_fabricante = nombre_fabricante

        if not pais_origen:
            return jsonify({"Mensaje": "El campo 'pais_origen' es obligatorio"}), 400
        fabricante.pais_origen = pais_origen
        
        db.session.commit()

        fabricante_schema = FabricanteSchema()
        fabricante_serializada = fabricante_schema.dump(fabricante)

        return jsonify({
            "Mensaje": "El fabricante esta editado con éxito",
            'fabricante': fabricante_serializada
        }), 200

    fabricante_schema = FabricanteSchema()
    fabricante_serializada = fabricante_schema.dump(fabricante)

    return jsonify({'fabricante': fabricante_serializada})

@fabricante_bp.route('/fabricante/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_fabricante(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el fabricante puede eliminar proveedores"}), 403

    fabricante = Fabricante.query.get(id)
    if not fabricante:
        return jsonify({"Mensaje": "Fabricante no encontrado"}), 404

    try:
        db.session.delete(fabricante)
        db.session.commit()
        return jsonify({"Mensaje": "Fabricante eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al eliminar el fabricante", "Error": str(e)}), 500

