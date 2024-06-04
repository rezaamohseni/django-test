from django.shortcuts import render
from .models import Service , Skill , Team , Category

def home (request):
    if request.GET.get('category') is not None:
        all_services = Service.objects.filter(category__title = request.GET.get('category'))
        
    else:  
        all_services = Service.objects.filter(status= True)
    context = {
        'services': all_services,
            
        }
    return render(request , 'root/index.html' , context=context)
