from django.urls import path  
from . import views

urlpatterns = [
    path("instructores/", views.instructores_list, name="instructores"),
    path("instructores/detalle/<str:document>", views.instructor_detail, name="instructor_detail"),
]
