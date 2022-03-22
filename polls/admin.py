from random import choices
from django.contrib import admin
from .models import Question,Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']

class ChoicesAdmin(admin.ModelAdmin):
    fields = ['question','choice_text','votes']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoicesAdmin)



