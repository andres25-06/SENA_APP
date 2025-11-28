from django.db import models

# Create your models here.
class aprendices(models.Model):
    document = models.CharField(max_length=20, primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    birthdate = models.DateField(null=True)
    city = models.CharField(max_length=50, null=True)
    program = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.document} {self.firstname} {self.lastname}'