from django.urls import path
from . import views

app_name = 'context_client_0'


urlpatterns = [
    path('', views.index, name='context_client_0_index'),
]