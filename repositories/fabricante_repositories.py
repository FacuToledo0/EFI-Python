from app import db
from models import Fabricante, Equipo

class FabricanteRepositories:
    def get_all(self):
        return Fabricante.query.all()

    def create(self, nombre_fabricante, pais_origen):
        nuevo_fabricante = Fabricante(nombre_fabricante=nombre_fabricante, pais_origen=pais_origen)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return nuevo_fabricante

    def get_by_id(self, id):
        return Fabricante.query.get_or_404(id)

    def update(self, fabricante):
        fabricante.nombre = "Nuevo fabricante"
        db.session.commit()

    def get_equipos_por_fabricante(self, fabricante_id):
        fabricante = self.get_by_id(fabricante_id)
        return fabricante.equipos 