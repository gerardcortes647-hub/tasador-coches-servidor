from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Base de datos de precios base por marca
PRECIOS_MARCAS = {
    "Tesla": 35000, "BMW": 28000, "Mercedes": 30000, "Audi": 27000,
    "Toyota": 18000, "Seat": 14000, "Ford": 16000, "Renault": 13000,
    "Hyundai": 15000, "Kia": 14500, "Volkswagen": 19000, "Ferrari": 150000,
    "Porsche": 85000, "Nissan": 15500, "Fiat": 12000, "Peugeot": 13500
}

@app.route('/tasar', methods=['POST'])
def tasar():
    marca = request.form.get('marca', 'Toyota')
    anio = int(request.form.get('anio', 2020))
    km = int(request.form.get('kilometros', 0))
    combustible = request.form.get('combustible', 'Gasolina')

    # Lógica de Tasación
    precio = PRECIOS_MARCAS.get(marca, 15000)
    
    # Depreciación por año (2026 es el año actual en este proyecto)
    antiguedad = 2026 - anio
    precio -= (antiguedad * 1150)
    
    # Depreciación por Kilometraje
    precio -= (km * 0.04)
    
    # Bonus por combustible eficiente
    if combustible in ["Eléctrico", "Híbrido"]:
        precio += 3500
    
    # Precio mínimo garantizado si no está averiado
    precio_final = max(1200, int(precio))
    
    return jsonify({"precio": precio_final})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
