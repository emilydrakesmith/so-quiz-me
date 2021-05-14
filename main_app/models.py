##  IMPORT STATEMENTS  ##
from django.db import models        # allows model creation
from django.urls import reverse     # allows reverse-redirect on form submissions

##  DATA MODELS  ##

# quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    question_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: add a slug for URL path generation (icebox)

    class Meta:
        verbose_name = 'Quiz'               # singular name in admin portal
        verbose_name_plural = 'Quizzes'     # plural name in admin portal
        # TODO: add 'ordering' for sequencing on page when rendered

    def __str__(self):
        return self.title    # return title instead of id when model is called
    
    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'quiz_id': self.id})   # set redirect on form submit