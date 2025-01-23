import io
import base64
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

def procesar_funcion(funcion_str):
    x = symbols('x')
    funcion = eval(funcion_str)
    derivada = diff(funcion, x)

    # Crear la gráfica
    valores_x = np.linspace(-10, 10, 400)
    valores_funcion = lambdify(x, funcion, 'numpy')(valores_x)
    valores_derivada = lambdify(x, derivada, 'numpy')(valores_x)

    plt.figure(figsize=(8, 6))
    plt.plot(valores_x, valores_funcion, label='Función', color='blue')
    plt.plot(valores_x, valores_derivada, label='Derivada', color='orange', linestyle='--')
    plt.title('Función y su Derivada')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica como cadena en base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    url_grafica = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return f"data:image/png;base64,{url_grafica}", str(derivada)
