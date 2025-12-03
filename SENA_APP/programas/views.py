from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Programa

class ProgramaListView(ListView):
    model = Programa
    template_name = 'program_list.html'
    context_object_name = 'programas'
    
    def get_queryset(self):
        # Filtra solo programas activos por defecto
        return Programa.objects.filter(estado='ACT')

def programa_detail(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request, 'program_detail.html', {'programa': programa})
