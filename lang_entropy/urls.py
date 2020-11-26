from django.urls import path
from . import views

app_name = 'lang_entropy'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('create/', views.AddItem, name='add_items'),
        path('save/', views.SaveTransaction, name='save'),
        path('list_state/', views.ListState, name='list_state'),
]