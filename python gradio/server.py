# server.py

from flask import Flask, request, jsonify
import asyncio
from init import mainGPT, mainAws  # Importamos las funciones desde init.py
from waitress import serve  # Importamos Waitress

app = Flask(__name__)

# Endpoint para recibir la task y el modelo
@app.route('/execute', methods=['POST'])
def execute_task():
    data = request.get_json()
    task = data.get('task')
    model = data.get('model')

    if not task or not model:
        return jsonify({"error": "Faltan parámetros 'task' o 'model'"}), 400

    try:
        # Ejecutar la función correspondiente según el modelo
        if model == "GPT":
            result = asyncio.run(mainGPT(task))
            print("Se ejecuto el modelo GPT")
        elif model == "AWS":
            result = asyncio.run(mainAws(task))
            print("Se ejecuto el modelo GPT")
        else:
            return jsonify({"error": "Modelo no válido. Use 'GPT' o 'AWS'"}), 400

        # Devolver el resultado como JSON
        print(jsonify({"result": result}))
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    serve(app, host='localhost', port=5001)