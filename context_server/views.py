from django.shortcuts import render
from context_server.helper_functions import *

# Create your views here.

def index(request):
    
    context = {
        'id' : 1,
    }
    
    return render(request, 'context_server/index.html', context)


def preprocess_amr(request):
    
    file_location = '/home/manu154c/amr_parser/amr_anotation/amr_annotation.txt'
    line_list = upload_the_file(file_location)
    extract_concepts_from_sentences()
    
    context = {
        'line_list' : line_list,
    }
    
    return render(request, 'context_server/display_file.html', context)