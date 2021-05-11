from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('quizzes/', views.quizzes_index, name='quizzes')
]