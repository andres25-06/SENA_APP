from django.shortcuts import render, get_object_or_404
from .models import Curso

# Create your views here.
def lista_cursos(request):
    cursos = Curso.objects.all()
    
    context = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    
    return render(request, 'cursos_list.html', context)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    
    return render(request, 'curso_detail.html', context)