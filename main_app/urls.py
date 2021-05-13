##  IMPORT STATEMENTS  ##
from django.urls import path    # import path function for path-based rendering
from . import views             # import view functions

##  URL PATTERNS  ##

#  All URL patterns use the function path()
#  List all functions in a sequence that makes sense and separate with commas
#
#  Each path() function takes three arguments:
#      1st arg: url path from index
#               no leading slash, must use trailing slash
#      2nd arg: call the function imported from views.py file
#               use .as_view() if the function is a class-based view
#      3rd arg: assign a name to the pathway for reverse() in form submits

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('quizzes/', views.quizzes_index, name='quizzes'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quizzes/create/', views.QuizCreate.as_view(), name='quiz_create')
]