from app import db
from models import Proveedor, Equipo

class ProveedorRepositories:
    def get_all(self):
        return Proveedor.query.all()

    def create(self, nombre_proveedor, contacto):
        nuevo_proveedor = Proveedor(nombre_proveedor=nombre_proveedor, contacto=contacto)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return nuevo_proveedor

    def get_by_id(self, id):
        return Proveedor.query.get_or_404(id)

    def update(self, proveedor):
        proveedor.nombre = "Nuevo proveedor"
        db.session.commit()

    def get_equipos_por_proveedor(self, proveedor_id):
        proveedor = self.get_by_id(proveedor_id)
        return proveedor.equipos 