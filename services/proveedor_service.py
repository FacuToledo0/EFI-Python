from repositories.proveedor_repositories import ProveedorRepositories

class ProveedorService:
    def __init__(self, proveedor_repository: ProveedorRepositories):
        self._proveedor_repository = proveedor_repository

    def get_all(self):
        return self._proveedor_repository.get_all()

    def create(self, nombre_proveedor, contacto):
        return self._proveedor_repository.create(nombre_proveedor, contacto)

    def get_by_id(self, id):
        return self._proveedor_repository.get_by_id(id)

    def update(self, id, nombre_proveedor, contacto):
        proveedor = self._proveedor_repository.get_by_id(id)
        if not proveedor:
            raise Exception("Proveedor no encontrado")
        proveedor.nombre_proveedor = nombre_proveedor, 
        proveedor.contacto = contacto
        self._proveedor_repository.update(proveedor)
        return proveedor
    
    def get_equipos_por_proveedor(self, proveedor_id):
        return self._proveedor_repository.get_equipos_por_proveedor(proveedor_id)