## IMPORT STATEMENTS  ##

# import render function
from django.shortcuts import render

# import class-based functionalities for data models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import data models for class-based views
from .models import Quiz

##  RENDER VIEW FUNCTIONS  ##

# view function for route '/'
def home(request):
    return render(request, 'home.html')

# view funciton for route '/about'
def about(request):
    return render(request, 'about.html')

# view function for route '/quizzes'
def quizzes_index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/index.html', {'quizzes': quizzes})

# view function for route '/quiz/<quiz.id>
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quizzes/detail.html', {'quiz': quiz})

##  CLASS-BASED VIEW FUNCTIONS  ##

# class-based view for creating quizzes
class QuizCreate(CreateView):
    model = Quiz
    fields = ['title', 'description']

    # # TODO: figure out what this does
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class QuizUpdate(UpdateView):
    model = Quiz
    fields = ['description']    # exclude fields to protect from being updated

class QuizDelete(DeleteView):
    model = Quiz
    success_url = '/quizzes/'