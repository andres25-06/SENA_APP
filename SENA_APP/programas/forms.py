from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar programas de formación"""
    
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el código del programa'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del programa'
            }),
            'nivel_formacion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modalidad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'duracion_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en meses',
                'min': '1'
            }),
            'duracion_horas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en horas',
                'min': '1'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción general del programa',
                'rows': 4
            }),
            'competencias': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Competencias que desarrollará el aprendiz',
                'rows': 4
            }),
            'perfil_egreso': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Perfil del egresado',
                'rows': 4
            }),
            'requisitos_ingreso': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Requisitos para ingresar al programa',
                'rows': 3
            }),
            'centro_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del centro de formación'
            }),
            'regional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Regional SENA'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_creacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        # Etiquetas personalizadas
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre del Programa',
            'nivel_formacion': 'Nivel de Formación',
            'modalidad': 'Modalidad',
            'duracion_meses': 'Duración en Meses',
            'duracion_horas': 'Duración en Horas',
            'descripcion': 'Descripción del Programa',
            'competencias': 'Competencias a Desarrollar',
            'perfil_egreso': 'Perfil de Egreso',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'regional': 'Regional',
            'estado': 'Estado',
            'fecha_creacion': 'Fecha de Creación del Programa'
        }

    # Validaciones personalizadas
    
    def clean_codigo(self):
        """Validar que el código no esté vacío y convertirlo a mayúsculas"""
        codigo = self.cleaned_data.get('codigo')
        if not codigo:
            raise forms.ValidationError("El código del programa es obligatorio.")
        return codigo.upper()

    def clean_duracion_meses(self):
        """Validar que la duración en meses sea positiva"""
        duracion = self.cleaned_data.get('duracion_meses')
        if duracion and duracion <= 0:
            raise forms.ValidationError("La duración en meses debe ser mayor a 0.")
        return duracion

    def clean_duracion_horas(self):
        """Validar que la duración en horas sea positiva"""
        duracion = self.cleaned_data.get('duracion_horas')
        if duracion and duracion <= 0:
            raise forms.ValidationError("La duración en horas debe ser mayor a 0.")
        return duracion

    def clean(self):
        """Validaciones adicionales del formulario"""
        cleaned_data = super().clean()
        duracion_meses = cleaned_data.get('duracion_meses')
        duracion_horas = cleaned_data.get('duracion_horas')
        
        # Validar coherencia entre duración en meses y horas
        if duracion_meses and duracion_horas:
            # Aproximadamente 160 horas por mes (4 semanas * 40 horas)
            horas_estimadas = duracion_meses * 160
            if duracion_horas > horas_estimadas * 2:
                self.add_warning = "La duración en horas parece muy alta en relación a los meses."
        
        return cleaned_data
