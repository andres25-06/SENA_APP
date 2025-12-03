from django.urls import path
from .views import ProgramaListView, programa_detail

app_name = 'programas'

urlpatterns = [
    path('programas/', ProgramaListView.as_view(), name='programa_list'),
    path('programas/<int:pk>/', programa_detail, name='programa_detail'),
]
