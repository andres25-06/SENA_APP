from django import forms
from .models import Instructores

class InstructoresForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar instructores"""
    
    class Meta:
        model = Instructores
        fields = [
            'document',
            'tipe_document',
            'name',
            'last_name',
            'phone',
            'email',
            'birth_date',
            'city',
            'address',
            'level_education',
            'speciality',
            'years_experience',
            'state',
            'date_boding'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'document': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el número de documento'
            }),
            'tipe_document': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa'
            }),
            'level_education': forms.Select(attrs={
                'class': 'form-control'
            }),
            'speciality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Desarrollo de Software, Electrónica'
            }),
            'years_experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Años de experiencia',
                'min': '0'
            }),
            'state': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'date_boding': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        # Etiquetas personalizadas
        labels = {
            'document': 'Número de Documento',
            'tipe_document': 'Tipo de Documento',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Teléfono',
            'email': 'Correo Electrónico',
            'birth_date': 'Fecha de Nacimiento',
            'city': 'Ciudad',
            'address': 'Dirección',
            'level_education': 'Nivel de Educación',
            'speciality': 'Especialidad',
            'years_experience': 'Años de Experiencia',
            'state': 'Activo',
            'date_boding': 'Fecha de Vinculación'
        }

    # Validaciones personalizadas
    
    def clean_document(self):
        """Validar que el documento contenga solo números"""
        documento = self.cleaned_data.get('document')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_phone(self):
        """Validar que el teléfono contenga solo números"""
        telefono = self.cleaned_data.get('phone')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono

    def clean_years_experience(self):
        """Validar que los años de experiencia sean un valor razonable"""
        years = self.cleaned_data.get('years_experience')
        if years is not None:
            if years < 0:
                raise forms.ValidationError("Los años de experiencia no pueden ser negativos.")
            if years > 50:
                raise forms.ValidationError("Los años de experiencia parecen excesivos. Verifique el valor.")
        return years

    def clean(self):
        """Validaciones adicionales del formulario"""
        cleaned_data = super().clean()
        birth_date = cleaned_data.get('birth_date')
        date_boding = cleaned_data.get('date_boding')
        
        # Validar que la fecha de vinculación sea posterior a la fecha de nacimiento
        if birth_date and date_boding:
            if date_boding <= birth_date:
                raise forms.ValidationError("La fecha de vinculación debe ser posterior a la fecha de nacimiento.")
        
        return cleaned_data
