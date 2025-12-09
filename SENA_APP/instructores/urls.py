from django.urls import path  
from . import views

app_name = 'instructores'

urlpatterns = [
    # Listado y detalle
    path("instructores/", views.instructores_list, name="instructores_list"),
    path("instructores/detalle/<str:document>", views.instructor_detail, name="instructor_detail"),
    
    # CRUD Instructor
    path("instructores/crear/", views.InstructorCreateView.as_view(), name="instructor_create"),
    path("instructores/<int:instructor_id>/editar/", views.InstructorUpdateView.as_view(), name="instructor_update"),
    path("instructores/<int:instructor_id>/eliminar/", views.InstructorDeleteView.as_view(), name="instructor_delete"),
]
