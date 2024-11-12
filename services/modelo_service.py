from repositories.modelo_repositories import ModeloRepositories

class ModeloService:
    def __init__(self, modelo_repository: ModeloRepositories):
        self._modelo_repository = modelo_repository

    def get_all(self):
        return self._modelo_repository.get_all()

    def create(self, nombre):
        return self._modelo_repository.create(nombre)

    def get_by_id(self, id):
        return self._modelo_repository.get_by_id(id)

    def update(self, id, nombre):
        modelo = self._modelo_repository.get_by_id(id)
        if not modelo:
            raise Exception("Modelo no encontrado")
        modelo.nombre = nombre
        self._modelo_repository.update(modelo)
        return modelo
    
    def get_telefonos_por_modelo(self, modelo_id):
        return self._modelo_repository.get_telefonos_por_modelo(modelo_id)