from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/tasar', methods=['POST'])
def tasar():
    # Recibimos todos los datos nuevos
    km = int(request.form.get('kilometros', 0))
    estado = request.form.get('estado', 'Bueno')
    marca = request.form.get('marca', 'Genérico')
    combustible = request.form.get('combustible', 'Gasolina')
    anio = int(request.form.get('anio', 2015))

    # 1. Precio base según la Marca (Vanguardista)
    maras_premium = {"BMW": 25000, "Mercedes": 27000, "Audi": 24000, "Tesla": 35000}
    precio_base = maras_premium.get(marca, 15000)

    # 2. Ajuste por Año (un coche nuevo vale más)
    antiguedad = 2026 - anio
    precio_base -= (antiguedad * 1000)

    # 3. Ajuste por Kilometraje
    precio_base -= (km * 0.05)

    # 4. Bonus por combustible "Eco"
    if combustible in ["Eléctrico", "Híbrido"]:
        precio_base += 3000

    # 5. Ajuste por Estado
    if "Averiado" in estado:
        precio_final = 500
    else:
        precio_final = max(1000, precio_base)

    return jsonify({"precio": int(precio_final)})
