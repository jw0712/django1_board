from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    #/polls/3/detail
    path('<int:question_id>/', views.detail, name='detail'),
    #/polls/3/results
    path('<int:question_id>/', views.results, name='results'),
    #/polls/3/vote
    path('<int:question_id>/', views.vote, name='vote'),
]
