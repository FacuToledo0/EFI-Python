from app import db
from models import Accesorio, Equipo

class AccesorioRepositories:
    def get_all(self):
        return Accesorio.query.all()

    def create(self, tipo_accesorio):
        nuevo_accesorio = Accesorio(tipo_accesorio=tipo_accesorio)
        db.session.add(nuevo_accesorio)
        db.session.commit()
        return nuevo_accesorio

    def get_by_id(self, id):
        return Accesorio.query.get_or_404(id)

    def update(self, accesorio):
        accesorio.nombre = "Nuevo accesorio"
        db.session.commit()

    def get_equipos_por_accesorio(self, accesorio_id):
        accesorio = self.get_by_id(accesorio_id)
        return accesorio.equipos 