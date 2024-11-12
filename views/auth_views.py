from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password

    usuario = User.query.filter_by(username=username).first()
    
    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ): 
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=10000),
            additional_claims=dict(
                administrador=usuario.is_admin
            )
        )

        return jsonify({'Token': access_token})
    
    return jsonify(Mensaje="El usuario y la contraseña no coinciden")

@auth_bp.route('/users', methods=['GET', 'POST'])
@jwt_required()
def users ():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')
    if request.method == 'POST':
        if administrador is True:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            is_admin = data.get('is_admin', False)

            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=generate_password_hash(password),
                    is_admin=is_admin,
                )
                db.session.add(nuevo_usuario)
                db.session.commit()

                return jsonify(
                    {
                    "Mensaje":"Usuario creado correctamente",
                    "Usuario": nuevo_usuario.to_dict()
                    }
                )
            except:
                return jsonify(
                    {
                    "Mensaje": "Fallo la creación del nuevo usuario"
                    }
                )
        else:
            return jsonify(Mensaje="Solo el usuario admin puede crear nuevos usuarios")    
    usuarios = User.query.all()
    usuarios_dict = []
    for usuario in usuarios:
        usuarios_dict.append(usuario.to_dict())

    return jsonify(usuarios_dict)


@auth_bp.route('/users/<int:id>/borrar', methods=['DELETE'])
@jwt_required()
def borrar_user(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "Solo el admin puede eliminar usuarios"}), 403

    usuario = User.query.get(id)
    if not usuario:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404

    try:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"Mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Fallo al eliminar el usuario", "Error": str(e)}), 500





@auth_bp.route('/users/<int:id>/editar', methods=['PUT'])
@jwt_required()
def editar_user(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if administrador is not True:
        return jsonify({"Mensaje": "No tienes permiso para actualizar usuarios"}), 403

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    is_admin = data.get('is_admin')

    try:
        usuario = User.query.get(id)
        if not usuario:
            return jsonify({"Mensaje": "Usuario no encontrado"}), 404

        usuario.username = username if username else usuario.username
        usuario.password_hash = generate_password_hash(password) if password else usuario.password_hash
        usuario.is_admin = is_admin if is_admin is not None else usuario.is_admin

        db.session.commit()
        return jsonify({"Mensaje": "Usuario actualizado correctamente", "Usuario": usuario.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Mensaje": "Error al actualizar el usuario: " + str(e)}), 500