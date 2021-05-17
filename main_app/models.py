##  IMPORT STATEMENTS  ##
from django.db import models                    # allows model creation
from django.urls import reverse                 # allows reverse-redirect on form submissions
from django.contrib.auth.models import User     # allows data for user model for auth

##  DATA MODELS  ##

# quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    question_count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: add a slug for URL path generation (icebox)

    class Meta:
        verbose_name = 'Quiz'               # singular name in admin portal
        verbose_name_plural = 'Quizzes'     # plural name in admin portal
        # TODO: add 'ordering' for sequencing on page when rendered

    def __str__(self):
        return self.title    # return title instead of id when model is called
    
    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'quiz_id': self.id})   # set redirect on form submit

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer_count = models.PositiveIntegerField(default=1)
    question_text = models.TextField(max_length=800)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=800)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text