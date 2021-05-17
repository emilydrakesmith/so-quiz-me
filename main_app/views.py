## IMPORT STATEMENTS  ##

# import render function
from django.shortcuts import render, redirect

# import class-based functionalities for data models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import data models for class-based views
from .models import Quiz, Question, Answer

# import input form models
from .forms import QuestionForm, AnswerForm

# import forms for auth purposes
from django.contrib.auth import login                       # needed to log in a new user automatically
from django.contrib.auth.forms import UserCreationForm      # form to create a new app user account
from django.contrib.auth.decorators import login_required   # detector to require login on view functions
from django.contrib.auth.mixins import LoginRequiredMixin   # detector to require login on class-based views

##  RENDER VIEW FUNCTIONS  ##

# view function for route '/'
def home(request):
    return render(request, 'home.html')

# view funciton for route '/about'
def about(request):
    return render(request, 'about.html')

# view function for route '/quizzes'
@login_required
def quizzes_index(request):
    quizzes = Quiz.objects.filter(user=request.user)
    return render(request, 'quizzes/index.html', {'quizzes': quizzes})

# TODO: {  add separate views that a user can see all public
# TODO: {  quizzes vs just quizzes available to them, this 
# TODO: {  will also require adding a public/private option
# TODO: {  to the Quiz database model

# view function for route '/quiz/<quiz.id>
@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    question_form = QuestionForm()
    return render(request, 'quizzes/detail.html', {'quiz': quiz, 'question_form': question_form})

# view function for route '/quiz/<question.id>
@login_required
def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answer_form = AnswerForm()
    return render(request, 'questions/detail.html', {'question': question, 'answer_form': answer_form})




##  CLASS-BASED VIEW FUNCTIONS  ##

# class-based view for creating quizzes
class QuizCreate(LoginRequiredMixin, CreateView):
    model = Quiz                                            # data model to use
    fields = ['title', 'description', 'question_count']     # fields in the model to take input for

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuizUpdate(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['description']    # exclude fields to protect from being updated

class QuizDelete(LoginRequiredMixin, DeleteView):
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

# form to add a new answer
@login_required
def add_answer(request, question_id):
    form = AnswerForm(request.POST)                                 # serve the add question for to the user
    if form.is_valid():                                             # perform form validation
        new_answer = form.save(commit=False)                        # get data submitted without sending it to the database 
        new_answer.question_id = question_id                        # add the quiz_id value as a foreign key
        new_answer.save()                                           # send the completed form to the database
    return redirect('question_detail', question_id=question_id)     # redirect user to  quiz detail page

# renger a user-interactable quiz
@login_required
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quizzes/take_quiz.html', {'quiz': quiz})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   # take data from request object to create a new user
        if form.is_valid():
            user = form.save()                  # add new user to the database
            login(request, user)                # automatically log in the new user
            return redirect('/')                # terminate the function and redirect to index
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()                                       # if new user creation fails, reinitiate signup process
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)