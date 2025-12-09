from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Instructores
from .forms import InstructoresForm

# Create your views here.
def instructores_list(request):
    data = Instructores.objects.all()
    context = {
        "instructores": data,
    }
    return render(request, 'instructores_list.html', context)

def instructor_detail(request, document):
    instructor = Instructores.objects.get(document=document)
    context = {
        "instructor": instructor,
    }
    return render(request, 'instructores_detail.html', context)


# ==================== CRUD INSTRUCTOR ====================

class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructores
    form_class = InstructoresForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el instructor"""
        messages.success(
            self.request,
            f'El instructor {form.instance.name} {form.instance.last_name} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = Instructores
    form_class = InstructoresForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El instructor {form.instance.name} {form.instance.last_name} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructores
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.name} {instructor.last_name} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)
