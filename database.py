import sqlite3

def get_db():
    connection = sqlite3.connect('database.sqlite')
    return connection

def create_db():
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   task TEXT NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users(id))''')
    connection.commit()
    connection.close()

def create_user(username, password):
    try:
        connection = get_db()
        cursor = connection.cursor()
        
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        connection.commit()
        connection.close()

    except Exception as e:
        print(f"Error de la base de datos: {e}")
        return {'error' : 'Ocurrio un error en la base de datos' }
    
    return {'mensaje' : 'Usuario creado con exito'}


def get_user(username):
    try:
        connection = get_db()
        cursor = connection.cursor()

        cursor.execute('''SELECT id, username, password FROM users WHERE username = ?''', (username, ))
        user = cursor.fetchone()

        connection.close()

        if user:
            return user
        else: 
            return None

    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return {'mensaje': 'Ocurrio un error'}
