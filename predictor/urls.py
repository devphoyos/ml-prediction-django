from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_and_predict, name='cargar_archivo'),  # URL para mostrar los resultados
]