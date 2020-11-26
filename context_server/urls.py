from django.urls import path
from . import views

app_name = 'context_server'

urlpatterns = [
    path('', views.index, name='context_server_index'),
    path('/amr_preprocessing/', views.preprocess_amr, name='amr_file_process'),
]