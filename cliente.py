import requests

# Informacion
URL = 'http://localhost:5000'

def registro():
    url = f"{URL}/registro"
    print("-- REGISTRO --")
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    data = {"username": username, "password": password}
    print(f"Registrando Usuario...")
    respuesta = requests.post(url, json=data)

    if respuesta.status_code == 201:
        print("Registro Exitoso! Volviendo al inicio...")
    else:
        error_info = respuesta.json()
        print(f"Error en el registro: {error_info['error']}", )


    main()

def login():
    url = f"{URL}/login"
    print("-- LOGIN --")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    data = {"username": username, "password": password}
    print(f"Iniciando Sesion...")
    respuesta = requests.post(url, json=data)

    if respuesta.status_code == 200:
        print("Bienvenido!")
        tareas()
    else:
        error_info = respuesta.json()
        print(f"Error al iniciar sesion: {error_info['error']}")
        print("Ingrese cualquier tecla para volver a intentarlo")
        print("Para volver al menu principal ingrese 0")
        respuesta = input()
        if respuesta == "0":
            main()

def tareas():
    url = f"{URL}/tareas"
    respuesta = requests.get(url)
    print("Cargando tareas...")
    if respuesta.status_code == 200:
        print(respuesta.text)
    else:
        print("Ocurrio un error")
    main()


def main():
    print("Bienvenido a la App. Ingrese una opcion para continuar")
    print("[1] Registrarse")
    print("[2] Iniciar Sesion")
    print("[3] Salir")
    while True:
        seleccion = input("Ingrese solo el número de la opcion deseada: ")
        match seleccion:
            case "1":
                registro()
                break
            case "2":
                login()
                break
            case "3":
                print("Saliendo...")
                exit()
            case _:
                print("Error. Ingrese solo el número de la opcion deseada")
                
main()
