## IMPORT STATEMENTS  ##

# import render function
from django.shortcuts import render

# import list functionality for data models
from django.views.generic import ListView

# import data models for class-based views
from .models import Quiz

##  RENDER VIEW FUNCTIONS  ##

# view function for route '/'
def home(request):
    return render(request, 'home.html')

# view funciton for route '/about'
def about(request):
    return render(request, 'about.html')

#view function for route '/quizzes'
def quizzes_index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/index.html', {'quizzes': quizzes})

##  CLASS-BASED VIEW FUNCTIONS  ##

# class-based view for quizzes
class QuizList(ListView):
    model = Quiz