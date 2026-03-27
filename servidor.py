from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/tasar', methods=['POST'])
def tasar():
    # Recibimos los nuevos datos
    km = int(request.form.get('kilometros', 0))
    estado = request.form.get('estado', 'Bueno')
    marca = request.form.get('marca', 'Toyota')
    combustible = request.form.get('combustible', 'Gasolina')
    anio = int(request.form.get('anio', 2020))

    # 1. Precio base por Marca
    precios_base = {
        "BMW": 25000, "Mercedes": 27000, "Audi": 24000, 
        "Tesla": 35000, "Toyota": 18000, "Seat": 15000
    }
    precio = precios_base.get(marca, 15000)

    # 2. Ajuste por antigüedad (2026 es el año actual)
    antiguedad = 2026 - anio
    precio -= (antiguedad * 1200)

    # 3. Ajuste por KM
    precio -= (km * 0.04)

    # 4. Bonus por combustible ECO
    if combustible in ["Híbrido", "Eléctrico"]:
        precio += 3500

    # 5. Ajuste por estado
    if "Averiado" in estado:
        precio = 800
    else:
        # Aseguramos un precio mínimo de 1000€ si no está averiado
        precio = max(1000, precio)

    return jsonify({"precio": int(precio)})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
