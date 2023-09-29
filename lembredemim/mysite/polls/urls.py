from django.urls import path

from . import views

urlpatterns = [
    #ex: /polls/
    path('', views.index, name='index'),
    #ex: /polls/5/
    path('<int:question_id>/', views.home, name='home'),
    #ex: /polls/5/results
    path('<int:question_id>/cartilhas/', views.cartilhas, name='cartilhas'),
   
    path('<int:question_id>/prontuario/', views.prontuario, name='prontuario'),
    
    path('<int:question_id>/quemsomos/', views.quemsomos, name='quemsomos'),

    path('<int:question_id>/minhaconta/', views.minhaconta, name='minhaconta'),
   
]