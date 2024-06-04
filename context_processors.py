from root.models import Category
def general_context(request):
    context = {
        'category' : Category.objects.all(),
        
    }
    return context