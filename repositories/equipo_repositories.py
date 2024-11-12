# from app import db
# from models import Equipo, Marca, Modelo, Proveedor, Fabricante, Accesorio

# class EquipoRepositories:
#     def get_all(self):
#         return Equipo.query.all()
    
#     def create(self, anio_fabricacion, precio, marca_id, modelo_id, proveedor_id, fabricante_id, accesorio_id):
#         marca = Marca.query.get(marca_id)
#         modelo = Modelo.query.get(modelo_id)
#         proveedor = Proveedor.query.get(proveedor_id)
#         fabricante = Fabricante.query.get(fabricante_id)
#         accesorio = Accesorio.query.get(accesorio_id)

#         if not marca or not modelo or not proveedor or not fabricante or not accesorio:
#             raise ValueError("Una o más relaciones son inválidas.")
    
#         nuevo_equipo = Equipo(
#             anio_fabricacion=anio_fabricacion,
#             precio=precio,
#             marca_id=marca_id,  # Usando solo los IDs de las relaciones
#             modelo_id=modelo_id,
#             proveedor_id=proveedor_id,
#             fabricante_id=fabricante_id,
#             accesorio_id=accesorio_id
#         )
    
#         db.session.add(nuevo_equipo)
#         db.session.commit()
#         return nuevo_equipo


#     # def create(self, anio_fabricacion, precio, marca, modelo, proveedor, fabricante, accesorio):
#     #     nuevo_equipo = Equipo(anio_fabricacion=anio_fabricacion, precio=precio, marca_id=marca, modelo_id=modelo, proveedor_id=proveedor, fabricante_id=fabricante, accesorio_id=accesorio)
#     #     db.session.add(nuevo_equipo)
#     #     db.session.commit()
#     #     return nuevo_equipo

#     def get_by_id(self, id):
#         return Equipo.query.get_or_404(id)

#     def update(self, equipo):
#         equipo.nombre = "Nuevo equipo"
#         db.session.commit()

#     def get_equipos_por_fabricante(self, equipo_id):
#         equipo = self.get_by_id(equipo_id)
#         return equipo.equipos 

from app import db
from models import Equipo, Marca, Modelo, Proveedor, Fabricante, Accesorio

class EquipoRepositories:
    
    def get_all(self):
        return Equipo.query.all()
    
    def create(self, anio_fabricacion, precio, marca_id, modelo_id, proveedor_id, fabricante_id, accesorio_id):
        # Verificar si las relaciones existen
        marca = Marca.query.get(marca_id)
        modelo = Modelo.query.get(modelo_id)
        proveedor = Proveedor.query.get(proveedor_id)
        fabricante = Fabricante.query.get(fabricante_id)
        accesorio = Accesorio.query.get(accesorio_id)

        # Si alguna de las relaciones no existe, lanzar un error
        if not marca or not modelo or not proveedor or not fabricante or not accesorio:
            raise ValueError("Una o más relaciones son inválidas.")
        
        # Crear el nuevo equipo con las relaciones verificadas
        nuevo_equipo = Equipo(
            anio_fabricacion=anio_fabricacion,
            precio=precio,
            marca_id=marca_id,  # Usando solo los IDs de las relaciones
            modelo_id=modelo_id,
            proveedor_id=proveedor_id,
            fabricante_id=fabricante_id,
            accesorio_id=accesorio_id
        )
        
        db.session.add(nuevo_equipo)
        db.session.commit()
        return nuevo_equipo

    def get_by_id(self, id):
        return Equipo.query.get_or_404(id)

    def update(self, id, anio_fabricacion, precio, marca_id, modelo_id, proveedor_id, fabricante_id, accesorio_id):
        equipo = self.get_by_id(id)
        if not equipo:
            raise Exception("Equipo no encontrado")
        
        # Actualiza los campos del equipo
        equipo.anio_fabricacion = anio_fabricacion
        equipo.precio = precio
        equipo.marca_id = marca_id
        equipo.modelo_id = modelo_id
        equipo.proveedor_id = proveedor_id
        equipo.fabricante_id = fabricante_id
        equipo.accesorio_id = accesorio_id
        
        db.session.commit()
        return equipo

    def get_equipos_por_fabricante(self, fabricante_id):
        # Buscar equipos del fabricante especificado
        fabricante = Fabricante.query.get(fabricante_id)
        if not fabricante:
            raise Exception(f"Fabricante con id {fabricante_id} no encontrado.")
        
        # Obtener todos los equipos asociados a ese fabricante
        return fabricante.equipos  # Asegúrate de que la relación esté bien definida en tu modelo
