from repositories.equipo_repositories import EquipoRepositories

class EquipoService:
    def __init__(self, equipo_repository: EquipoRepositories):
        self._equipo_repository = equipo_repository

    def get_all(self):
        return self._equipo_repository.get_all()

    def create(self, anio_fabricacion, precio, marca, modelo, proveedor, fabricante, accesorio):
        return self._equipo_repository.create(anio_fabricacion, precio, marca, modelo, proveedor, fabricante, accesorio)

    def get_by_id(self, id):
        return self._equipo_repository.get_by_id(id)

    def update(self, id, anio_fabricacion, precio, marca, modelo, proveedor, fabricante, accesorio):
        equipo = self._equipo_repository.get_by_id(id)
        if not equipo:
            raise Exception("Equipo no encontrado")
        equipo.anio_fabricacion = anio_fabricacion
        equipo.precio = precio
        equipo.marca = marca
        equipo.modelo = modelo
        equipo.proveedor = proveedor
        equipo.fabricante = fabricante
        equipo.accesorio = accesorio 
        self._equipo_repository.update(equipo)
        return equipo
    
    def get_equipos_por_equipo(self, equipo_id):
        return self._equipo_repository.get_equipos_por_equipo(equipo_id)
