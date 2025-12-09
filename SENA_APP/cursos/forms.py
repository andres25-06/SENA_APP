from django import forms
from .models import Curso, InstructorCurso, AprendizCurso

class CursoForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar cursos"""
    
    class Meta:
        model = Curso
        fields = [
            'code',
            'name',
            'program',
            'instructor_coordinator',
            'start_date',
            'end_date',
            'schedule',
            'classroom',
            'max_capacity',
            'state',
            'observations'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el código del curso'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del curso'
            }),
            'program': forms.Select(attrs={
                'class': 'form-control'
            }),
            'instructor_coordinator': forms.Select(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'schedule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lunes a Viernes 8:00 AM - 12:00 PM'
            }),
            'classroom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el aula o ambiente'
            }),
            'max_capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cupos máximos',
                'min': '1'
            }),
            'state': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observations': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones adicionales',
                'rows': 3
            })
        }
        # Etiquetas personalizadas
        labels = {
            'code': 'Código del Curso',
            'name': 'Nombre del Curso',
            'program': 'Programa de Formación',
            'instructor_coordinator': 'Instructor Coordinador',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Finalización',
            'schedule': 'Horario',
            'classroom': 'Aula/Ambiente',
            'max_capacity': 'Cupos Máximos',
            'state': 'Estado del Curso',
            'observations': 'Observaciones'
        }

    # Validaciones personalizadas
    
    def clean_code(self):
        """Validar que el código no esté vacío y tenga formato válido"""
        codigo = self.cleaned_data.get('code')
        if not codigo:
            raise forms.ValidationError("El código del curso es obligatorio.")
        return codigo.upper()

    def clean(self):
        """Validar que la fecha de finalización sea posterior a la fecha de inicio"""
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError("La fecha de finalización debe ser posterior a la fecha de inicio.")
        
        return cleaned_data


class InstructorCursoForm(forms.ModelForm):
    """Formulario para asignar instructores a cursos"""
    
    class Meta:
        model = InstructorCurso
        fields = ['teacher', 'course', 'role']
        widgets = {
            'teacher': forms.Select(attrs={
                'class': 'form-control'
            }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Instructor Técnico, Instructor de Apoyo'
            })
        }
        labels = {
            'teacher': 'Instructor',
            'course': 'Curso',
            'role': 'Rol en el Curso'
        }


class AprendizCursoForm(forms.ModelForm):
    """Formulario para inscribir aprendices en cursos"""
    
    class Meta:
        model = AprendizCurso
        fields = ['student', 'course', 'state', 'final_grade', 'observations']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control'
            }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            }),
            'state': forms.Select(attrs={
                'class': 'form-control'
            }),
            'final_grade': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nota de 0.0 a 5.0',
                'step': '0.1',
                'min': '0',
                'max': '5'
            }),
            'observations': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones sobre el aprendiz en el curso',
                'rows': 3
            })
        }
        labels = {
            'student': 'Aprendiz',
            'course': 'Curso',
            'state': 'Estado en el Curso',
            'final_grade': 'Nota Final',
            'observations': 'Observaciones'
        }

    def clean_final_grade(self):
        """Validar que la nota final esté en el rango válido"""
        nota = self.cleaned_data.get('final_grade')
        if nota is not None:
            if nota < 0 or nota > 5:
                raise forms.ValidationError("La nota debe estar entre 0.0 y 5.0")
        return nota
