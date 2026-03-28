from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Base de datos expandida de marcas y precios base
PRECIOS_BASE = {
    # Populares
    "Toyota": 18000, "BMW": 28000, "Mercedes": 30000, "Audi": 27000,
    "Volkswagen": 19500, "Ford": 16500, "Seat": 14000, "Renault": 13500,
    "Peugeot": 13800, "Citroën": 12500, "Opel": 14200, "Fiat": 11500,
    "Nissan": 16000, "Hyundai": 15500, "Kia": 15000, "Dacia": 9500,
    # Premium / Lujo
    "Tesla": 36000, "Volvo": 26000, "Lexus": 31000, "Jaguar": 33000,
    "Land Rover": 38000, "Porsche": 85000, "Maserati": 70000, "Ferrari": 160000,
    # Otras
    "Mazda": 17000, "Skoda": 14500, "Honda": 17500, "Suzuki": 12000,
    "Mini": 19000, "Alfa Romeo": 21000, "Jeep": 23000, "Subaru": 18500
}

@app.route('/marcas', methods=['GET'])
def obtener_marcas():
    # Devuelve la lista ordenada alfabéticamente
    lista_marcas = sorted(list(PRECIOS_BASE.keys()))
    return jsonify(lista_marcas)

@app.route('/tasar', methods=['POST'])
def tasar():
    marca = request.form.get('marca', 'Toyota')
    anio = int(request.form.get('anio', 2020))
    km = int(request.form.get('kilometros', 0))
    combustible = request.form.get('combustible', 'Gasolina')

    # Lógica de Tasación Pro
    precio = PRECIOS_BASE.get(marca, 15000)
    
    # Depreciación por año (Año actual simulado: 2026)
    antiguedad = 2026 - anio
    precio -= (antiguedad * 1200)
    
    # Depreciación por Kilometraje
    precio -= (km * 0.04)
    
    # Bonus por combustible eficiente
    if combustible in ["Eléctrico", "Híbrido"]:
        precio += 4500
    
    precio_final = max(1000, int(precio))
    return jsonify({"precio": precio_final})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
