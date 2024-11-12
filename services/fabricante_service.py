from repositories.fabricante_repositories import FabricanteRepositories

class FabricanteService:
    def __init__(self, fabricante_repository: FabricanteRepositories):
        self._fabricante_repository = fabricante_repository

    def get_all(self):
        return self._fabricante_repository.get_all()

    def create(self, nombre_fabricante, pais_origen):
        return self._fabricante_repository.create(nombre_fabricante, pais_origen=pais_origen)

    def get_by_id(self, id):
        return self._fabricante_repository.get_by_id(id)

    def update(self, id, nombre_fabricante, pais_origen):
        fabricante = self._fabricante_repository.get_by_id(id)
        if not fabricante:
            raise Exception("Fabricante no encontrado")
        fabricante.nombre_fabricante = nombre_fabricante, 
        fabricante.pais_origen = pais_origen
        self._fabricante_repository.update(fabricante)
        return fabricante
    
    def get_equipos_por_fabricante(self, fabricante_id):
        return self._fabricante_repository.get_equipos_por_fabricante(fabricante_id)