from flask import Flask



def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_class)

    from rootfile.main.routes import main
    from rootfile.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
