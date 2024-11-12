from app import ma

from marshmallow import validates, ValidationError

from models import User, Marca, Equipo, Fabricante, Accesorio, Proveedor, Modelo

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca

    id = ma.auto_field()
    nombre= ma.auto_field()

class FabricanteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Fabricante

    id = ma.auto_field()
    nombre_fabricante = ma.auto_field()
    pais_origen = ma.auto_field()

class AccesorioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Accesorio

    id = ma.auto_field()
    tipo_accesorio = ma.auto_field()

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    id = ma.auto_field()
    nombre=ma.auto_field()

class ProveedorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Proveedor

    id = ma.auto_field()
    nombre_proveedor = ma.auto_field()
    contacto = ma.auto_field()

class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo

    id = ma.auto_field()
    anio_fabricacion = ma.auto_field()
    precio = ma.auto_field()
    modelo_id = ma.auto_field()
    marca_id = ma.auto_field()
    proveedor_id = ma.auto_field()
    fabricante_id = ma.auto_field()
    accesorio_id = ma.auto_field()
    modelo = ma.Nested(ModeloSchema)
    marca = ma.Nested(MarcaSchema)
    proveedor = ma.Nested(ProveedorSchema)
    fabricante = ma.Nested(FabricanteSchema)
    accesorio = ma.Nested(AccesorioSchema)

