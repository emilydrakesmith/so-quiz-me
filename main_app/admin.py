## IMPORT STATEMENTS  ##

# import admin function (boilerplate feature)
from django.contrib import admin

# import data models to access in admin portal
from .models import Quiz, Question, Answer

## REGISTER DATA MODELS  ##
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)