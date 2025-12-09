from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Curso, InstructorCurso, AprendizCurso
from .forms import CursoForm, InstructorCursoForm, AprendizCursoForm

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


# ==================== CRUD CURSO ====================

class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""
    model = Curso
    form_class = CursoForm
    template_name = 'agregar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el curso"""
        messages.success(
            self.request,
            f'El curso {form.instance.name} ha sido creado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El curso {form.instance.name} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        curso = self.get_object()
        messages.success(
            request,
            f'El curso {curso.name} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


# ==================== CRUD INSTRUCTOR-CURSO ====================

class InstructorCursoCreateView(generic.CreateView):
    """Vista para asignar un instructor a un curso"""
    model = InstructorCurso
    form_class = InstructorCursoForm
    template_name = 'instructor_curso_form.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'Instructor asignado al curso exitosamente.'
        )
        return super().form_valid(form)


class InstructorCursoDeleteView(generic.DeleteView):
    """Vista para remover un instructor de un curso"""
    model = InstructorCurso
    template_name = 'instructor_curso_confirm_delete.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'pk'
    
    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            'Instructor removido del curso exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


# ==================== CRUD APRENDIZ-CURSO ====================

class AprendizCursoCreateView(generic.CreateView):
    """Vista para inscribir un aprendiz en un curso"""
    model = AprendizCurso
    form_class = AprendizCursoForm
    template_name = 'aprendiz_curso_form.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'Aprendiz inscrito en el curso exitosamente.'
        )
        return super().form_valid(form)


class AprendizCursoUpdateView(generic.UpdateView):
    """Vista para actualizar la información de un aprendiz en un curso"""
    model = AprendizCurso
    form_class = AprendizCursoForm
    template_name = 'aprendiz_curso_form.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'pk'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Información del aprendiz actualizada exitosamente.'
        )
        return super().form_valid(form)


class AprendizCursoDeleteView(generic.DeleteView):
    """Vista para remover un aprendiz de un curso"""
    model = AprendizCurso
    template_name = 'aprendiz_curso_confirm_delete.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'pk'
    
    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            'Aprendiz removido del curso exitosamente.'
        )
        return super().delete(request, *args, **kwargs)