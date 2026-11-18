from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.medicamento_routes import medicamento_bp
    from .routes.categoria_routes import categoria_bp

    app.register_blueprint(medicamento_bp)
    app.register_blueprint(categoria_bp)

    return app