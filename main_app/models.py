from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
    
    # TODO: add def get_absolute_url