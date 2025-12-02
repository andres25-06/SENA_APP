from django.db import models

# Create your models here.
class Instructores(models.Model):
    TIPO_DOCUMENT_CHOICES = [
        ('CC', 'Cedula de ciudadania'),
        ('CE', 'Cedula de extrangeria'),
        ('TI', 'Tarjeta de identidad'),
        ('PAS', 'Pasaporte'),
    ]
    LEVEL_EDUCATION_CHOICES = [
        ('BACH', 'Bachiller'),
        ('TECN', 'Tecnico'),
        ('ING', 'Ingeniero'),
        ('MAST', 'Maestro'),
        ('PREGRA', 'Pregrado'),
        ('POSTGR', 'Postgrado'),
        ('MAESTRIA', 'Maestria'),
        ('DOCTORADO', 'Doctorado'),
    ]
    document = models.CharField(max_length=20, unique=True)
    tipe_document = models.CharField(max_length=3, choices=TIPO_DOCUMENT_CHOICES)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    birth_date = models.DateField()
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    level_education = models.CharField(max_length=10, choices=LEVEL_EDUCATION_CHOICES)
    speciality = models.CharField(max_length=100)
    years_experience = models.IntegerField()
    state = models.BooleanField(default=True)
    date_boding = models.DateField()
    date_record = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.document} {self.name} {self.last_name}'

    
