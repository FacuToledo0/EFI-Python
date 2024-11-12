from repositories.accesorio_repositories import AccesorioRepositories

class AccesorioService:
    def __init__(self, accesorio_repository: AccesorioRepositories):
        self._accesorio_repository = accesorio_repository

    def get_all(self):
        return self._accesorio_repository.get_all()

    def create(self, tipo_accesorio):
        return self._accesorio_repository.create(tipo_accesorio)

    def get_by_id(self, id):
        return self._accesorio_repository.get_by_id(id)

    def update(self, id, tipo_accesorio):
        accesorio = self._accesorio_repository.get_by_id(id)
        if not accesorio:
            raise Exception("Accesorio no encontrado")
        accesorio.nombre = tipo_accesorio
        self._accesorio_repository.update(accesorio)
        return accesorio
    
    def get_telefonos_por_accesorio(self, accesorio_id):
        return self._accesorio_repository.get_telefonos_por_accesorio(accesorio_id)