from django.urls import path  
from . import views

app_name = "aprendices"


urlpatterns = [
    path("", views.main, name="main"),
    path("aprendices/", views.aprendices_list, name="aprendices"),
    path("aprendices/detalle/<str:document>", views.aprendiz_detail, name="aprendiz_detail"),
    path("aprendices/crear", views.AprendizCreateView.as_view(), name="aprendiz_create"),
    path("aprendices/editar/<str:document>", views.AprendizUpdateView.as_view(), name="aprendiz_update"),
    path("aprendices/eliminar/<str:document>", views.AprendizDeleteView.as_view(), name="aprendiz_delete"),
    ]
