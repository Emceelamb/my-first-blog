from django.contrib import admin

from .models import Question
from .models import Project

admin.site.register(Question)
admin.site.register(Project)