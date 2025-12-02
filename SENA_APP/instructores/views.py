from django.shortcuts import render
from .models import Instructores

# Create your views here.
def instructores_list(request):
    data = Instructores.objects.all().values()
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
