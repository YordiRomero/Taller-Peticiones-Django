import json

from django.http import JsonResponse
from django.views import View


tareas = [
    {"id": 1, "titulo": "Estudiar Django"},
    {"id": 2, "titulo": "Practicar los verbos HTTP"}
]


class TareaView(View):

    def get(self, request):
        return JsonResponse({"tareas": tareas})

    def post(self, request):
        datos = json.loads(request.body)

        nueva_tarea = {
            "id": max([tarea["id"] for tarea in tareas], default=0) + 1,
            "titulo": datos["titulo"]
        }

        tareas.append(nueva_tarea)

        return JsonResponse(nueva_tarea, status=201)

    def put(self, request):
        datos = json.loads(request.body)
        id_tarea = int(datos["id"])

        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tarea["titulo"] = datos["titulo"]
                return JsonResponse(tarea)

        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404
        )

    def delete(self, request):
        datos = json.loads(request.body)
        id_tarea = int(datos["id"])

        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tareas.remove(tarea)
                return JsonResponse(
                    {"mensaje": "Tarea eliminada correctamente"}
                )

        return JsonResponse(
            {"error": "Tarea no encontrada"},
            status=404
        )
