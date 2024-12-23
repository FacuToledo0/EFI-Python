from .auth_views import auth_bp
from .marca_view import marca_bp
from .modelo_view import modelo_bp
from .accesorio_view import accesorio_bp
from .proveedor_view import proveedor_bp
from .fabricante_view import fabricante_bp
from .equipo_view import equipo_bp

def register_bp(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(modelo_bp)
    app.register_blueprint(accesorio_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(fabricante_bp)
    app.register_blueprint(equipo_bp)
