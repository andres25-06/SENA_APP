from django.urls import path  
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("aprendices/", views.aprendices_list, name="aprendices"),
    path("aprendices/detalle/<str:document>", views.aprendiz_detail, name="aprendiz_detail"),
    ]
