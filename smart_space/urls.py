from django.urls import path
from . import views

app_name = 'smart_space'

urlpatterns = [
    path('', views.index, name='smart_space_index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]