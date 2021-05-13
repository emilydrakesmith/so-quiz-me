##  IMPORT STATEMENTS  ##
from django.db import models        # allows model creation
from django.urls import reverse     # allows reverse-redirect on form submissions

##  DATA MODELS  ##

# quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title    # return title instead of id when model is called
    
    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'quiz_id': self.id})   # set redirect on form submit