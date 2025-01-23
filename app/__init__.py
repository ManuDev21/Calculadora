from flask import Flask

def crear_aplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config['CLAVE_SECRETA'] = 'clave_secreta'

    from .rutas import principal
    aplicacion.register_blueprint(principal)

    return aplicacion
