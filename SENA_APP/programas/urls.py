from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    # Listado y detalle
    path('programas/', views.ProgramaListView.as_view(), name='programa_list'),
    path('programas/<int:pk>/', views.programa_detail, name='programa_detail'),
    
    # CRUD Programa
    path('programas/crear/', views.ProgramaCreateView.as_view(), name='programa_create'),
    path('programas/<int:pk>/editar/', views.ProgramaUpdateView.as_view(), name='programa_update'),
    path('programas/<int:pk>/eliminar/', views.ProgramaDeleteView.as_view(), name='programa_delete'),
]
