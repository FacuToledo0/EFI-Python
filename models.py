from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_proveedor = db.Column(db.String(50), nullable=False)
    contacto = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return f"{self.nombre_proveedor}, {self.contacto}"
    
class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_fabricante = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return f"{self.nombre_fabricante}, {self.pais_origen}"
    
class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_accesorio = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.tipo_accesorio

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)

    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True))
    proveedor = db.relationship('Proveedor', backref=db.backref('equipos', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('equipos', lazy=True))
    accesorio = db.relationship('Accesorio', backref=db.backref('equipos', lazy=True))

    
    def __str__(self):
        return f"Telefono {self.modelo}"
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.username,
            'password': self.password_hash,
            'is_admin': 1 if self.is_admin else 0
        }