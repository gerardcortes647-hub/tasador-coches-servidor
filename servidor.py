from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Base de datos expandida
MARCAS_DATA = {
    "Tesla": 35000, "BMW": 28000, "Mercedes": 30000, "Audi": 27000,
    "Toyota": 18000, "Seat": 14000, "Ford": 16000, "Renault": 13000,
    "Hyundai": 15000, "Kia": 14500, "Volkswagen": 19000, "Ferrari": 150000
}

@app.route('/tasar', methods=['POST'])
def tasar():
    # Si el usuario sube foto, aquí iría el modelo de IA (TensorFlow/PyTorch)
    # Por ahora procesamos los datos enviados por la App
    marca = request.form.get('marca', 'Toyota')
    anio = int(request.form.get('anio', 2020))
    km = int(request.form.get('kilometros', 0))
    combustible = request.form.get('combustible', 'Gasolina')

    precio = MARCAS_DATA.get(marca, 15000)
    
    # Lógica inteligente de depreciación
    antiguedad = 2026 - anio
    precio -= (antiguedad * 1100)
    precio -= (km * 0.05)
    
    if combustible in ["Eléctrico", "Híbrido"]: precio += 4000
    
    return jsonify({
        "precio": max(1000, int(precio)),
        "detectado": f"{marca} (Detectado por IA)"
    })

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
