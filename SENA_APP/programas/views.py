from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Programa
from .forms import ProgramaForm

class ProgramaListView(ListView):
    model = Programa
    template_name = 'program_list.html'
    context_object_name = 'programas'
    
    def get_queryset(self):
        # Mostrar todos los programas ordenados por nombre
        return Programa.objects.all()

def programa_detail(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request, 'program_detail.html', {'programa': programa})


# ==================== CRUD PROGRAMA ====================

class ProgramaCreateView(CreateView):
    """Vista para crear un nuevo programa de formación"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:programa_list')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido creado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class ProgramaUpdateView(UpdateView):
    """Vista para actualizar un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:programa_list')
    pk_url_kwarg = 'pk'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


class ProgramaDeleteView(DeleteView):
    """Vista para eliminar un programa"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:programa_list')
    pk_url_kwarg = 'pk'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        programa = self.get_object()
        messages.success(
            request,
            f'El programa {programa.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)
