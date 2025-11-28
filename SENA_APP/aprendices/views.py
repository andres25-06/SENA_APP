from django.http import HttpResponse  
from django.template import loader  
from .models import aprendices
from django.db.models import Q  

from django.shortcuts import render



# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def aprendices_list(request):
    data = aprendices.objects.all().values()
    context = {
        "aprendices": data,
    }

    return render(request, 'aprendices_list.html', context)

def aprendiz_detail(request, document):
    aprendiz = aprendices.objects.get(document=document)
    context = {
        "aprendiz": aprendiz,
    }
    return render(request, 'aprendiz_detail.html', context)
