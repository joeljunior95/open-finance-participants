from flask import Flask

def create_app():
    app = Flask('open-finance-participants', 
                template_folder='src/application/templates',
                static_folder='src/application/static')

    app.config.from_object('config.Config')

    with app.app_context():
        from src.application.participants import parts_routes

        app.register_blueprint(parts_routes.parts_bp)

    return app