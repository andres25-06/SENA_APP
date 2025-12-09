from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    # Listado y detalle
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='curso_detail'),
    
    # CRUD Curso
    path('cursos/crear/', views.CursoCreateView.as_view(), name='curso_create'),
    path('cursos/<int:curso_id>/editar/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('cursos/<int:curso_id>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),
    
    # Asignar/Remover Instructores
    path('cursos/instructor/asignar/', views.InstructorCursoCreateView.as_view(), name='instructor_curso_create'),
    path('cursos/instructor/<int:pk>/remover/', views.InstructorCursoDeleteView.as_view(), name='instructor_curso_delete'),
    
    # Inscribir/Gestionar Aprendices
    path('cursos/aprendiz/inscribir/', views.AprendizCursoCreateView.as_view(), name='aprendiz_curso_create'),
    path('cursos/aprendiz/<int:pk>/editar/', views.AprendizCursoUpdateView.as_view(), name='aprendiz_curso_update'),
    path('cursos/aprendiz/<int:pk>/remover/', views.AprendizCursoDeleteView.as_view(), name='aprendiz_curso_delete'),
]
