from django.shortcuts import render
from .models import Service , Skill , Team , Category

def home (request):
    context = {
        'service' : Service.objects.filter(status = True),
        'skill' : Skill.objects.filter(status = True),
        'team' : Team.objects.filter(status = True),
        'category' : Category.objects.filter(status = True)
    }
    return render(request , 'root/index.html' , context=context)