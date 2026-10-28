import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

url = "http://127.0.0.1:8000/tareas/"


def enviar_peticion(metodo, datos=None):
    contenido = None

    if datos is not None:
        contenido = json.dumps(datos).encode("utf-8")

    peticion = Request(
        url,
        data=contenido,
        method=metodo,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urlopen(peticion) as respuesta:
            print("\nMétodo:", metodo)
            print("Código:", respuesta.status)
            print(respuesta.read().decode("utf-8"))

    except HTTPError as error:
        print("\nMétodo:", metodo)
        print("Código:", error.code)
        print(error.read().decode("utf-8"))


enviar_peticion("GET")

enviar_peticion("POST", {
    "titulo": "Aprender POST"
})

enviar_peticion("PUT", {
    "id": 1,
    "titulo": "Estudiar Django avanzado"
})

enviar_peticion("DELETE", {
    "id": 2
})

enviar_peticion("GET")
