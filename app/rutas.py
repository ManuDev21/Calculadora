from flask import Blueprint, render_template, request
from .utilidades import procesar_funcion

principal = Blueprint('principal', __name__)

@principal.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        funcion = request.form.get('funcion')
        url_grafica, derivada = procesar_funcion(funcion)
        return render_template('resultado.html', funcion=funcion, url_grafica=url_grafica, derivada=derivada)
    return render_template('inicio.html')
