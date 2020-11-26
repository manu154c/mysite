from django.urls import path

from . import views

app_name = 'data_structures'

urlpatterns = [
    
    path('', views.index, name='data_structures_index'),
]