from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import TareaView

urlpatterns = [
    path('tareas/', csrf_exempt(TareaView.as_view()), name='tareas'),
]