from django.shortcuts import render

# Create your views here.


def index(request):
    
    context = {
        'id' : 1
    }
    
    return render(request, 'context_client_0/index.html', context)