from django.contrib import admin

from .models import Question, Answers, Upload

admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Upload)
