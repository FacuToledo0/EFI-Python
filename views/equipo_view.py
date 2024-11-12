from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from app import db
from services.equipo_service import EquipoService
from repositories.equipo_repositories import EquipoRepositories
from schemas import (EquipoSchema, MarcaSchema, ModeloSchema, ProveedorSchema, FabricanteSchema, AccesorioSchema)
from models import Equipo, Marca, Modelo, Proveedor, Fabricante, Accesorio
from forms import EquipoForm

equipo_bp = Blueprint('equipo', __name__)

@equipo_bp.route("/equipo", methods=['POST'])
@jwt_required()
def equipos():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear celulares"}), 403

    data = request.get_json()

    required_fields = ['anio_fabricacion', 'precio', 'marca_id', 'modelo_id', 'proveedor_id', 'fabricante_id', 'accesorio_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo {field}"}), 400

    equipo_service = EquipoService(EquipoRepositories())

    try:
        equipo = equipo_service.create(
            data['anio_fabricacion'],
            data['precio'],
            data['marca_id'],
            data['modelo_id'],
            data['proveedor_id'],
            data['fabricante_id'],
            data['accesorio_id']
        )
        return jsonify({"message": "Celular creado exitosamente"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error al crear el celular: {str(e)}"}), 500
    
@equipo_bp.route("/equipo_list", methods=['GET'])
@jwt_required()
def equipos_list():
    equipo_service = EquipoService(EquipoRepositories())
    equipos = equipo_service.get_all()

    equipo_schema = EquipoSchema(many=True)
    equipos_serializadas = equipo_schema.dump(equipos)

    return jsonify({'equipos': equipos_serializadas})

