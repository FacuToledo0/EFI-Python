from app import db
from models import Modelo, Equipo

class ModeloRepositories:
    def get_all(self):
        return Modelo.query.all()

    def create(self, nombre):
        nuevo_modelo = Modelo(nombre=nombre)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return nuevo_modelo

    def get_by_id(self, id):
        return Modelo.query.get_or_404(id)

    def update(self, modelo):
        modelo.nombre = "Nuevo modelo"
        db.session.commit()

    def get_equipos_por_modelo(self, modelo_id):
        modelo = self.get_by_id(modelo_id)
        return modelo.equipos 