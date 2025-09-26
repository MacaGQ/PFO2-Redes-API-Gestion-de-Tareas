from flask import Flask, request, jsonify, render_template
import bcrypt
from database import create_user, get_user, create_db

app = Flask(__name__)

@app.post('/registro')
def registro():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Se requiere usuario y contraseña"}), 400
    
    user = get_user(username)
    if user:
        return jsonify({"error": "El nombre de usuario ya esta siendo utilizado"}), 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    result = create_user(username, hashed_password)
    if "error" in result:
        return jsonify(result), 500
    
    return jsonify({"mensaje": "Usuario creado correctamente"}), 201

@app.post('/login')
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Se requiere usuario y contraseña"}), 400
    
    user = get_user(username)

    if user:
        hashed_password = user[2]

        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return jsonify({"mensaje": "Se inicio sesión correctamente"}), 200
        else:
            return jsonify({"error": "Credenciales invalidas"}), 401
    
    else:
        return jsonify({"error": "Usuario no encontrado"}), 401

@app.get("/tareas")
def tareas():
    return render_template("tareas.html")

create_db()

