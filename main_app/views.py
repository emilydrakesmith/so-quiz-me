## IMPORT STATEMENTS  ##

# import render function
from django.shortcuts import render, redirect

# import class-based functionalities for data models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import data models for class-based views
from .models import Quiz, Question, Answer

# import input form models
from .forms import QuestionForm

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
    # TODO: Use foreign key on Questions model to get questions for a quiz
    #questions = Quiz.questions.get()
    question_form = QuestionForm()
    return render(request, 'quizzes/detail.html', {'quiz': quiz, 'question_form': question_form})

##  CLASS-BASED VIEW FUNCTIONS  ##

# class-based view for creating quizzes
class QuizCreate(CreateView):
    model = Quiz                                            # data model to use
    fields = ['title', 'description', 'question_count']     # fields in the model to take input for

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

# form to add a new question
def add_question(request, quiz_id):
    form = QuestionForm(request.POST)                   # serve the add question for to the user
    if form.is_valid():                                 # perform form validation
        new_question = form.save(commit=False)          # get data submitted without sending it to the database 
        new_question.quiz_id = quiz_id                  # add the quiz_id value as a foreign key
        new_question.save()                             # send the completed form to the database
    return redirect('quiz_detail', quiz_id=quiz_id)     # redirect user to  quiz detail page