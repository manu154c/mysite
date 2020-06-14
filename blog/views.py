from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.all()