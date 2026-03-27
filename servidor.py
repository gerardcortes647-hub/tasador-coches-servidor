from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/tasar', methods=['POST'])
def tasar():
    km = request.form.get('kilometros', '0')
    estado = request.form.get('estado', 'Bueno')
    
    precio_base = 12000 
    descuento_km = int(km) * 0.02
    
    if "Averiado" in estado:
        precio_final = 500
    else:
        precio_final = max(800, precio_base - descuento_km)

    return jsonify({"precio": int(precio_final)})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
