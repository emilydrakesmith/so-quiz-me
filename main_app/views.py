from django.shortcuts import render

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def quizzes_index(request):
    return render(request, 'quizzes/index.html')