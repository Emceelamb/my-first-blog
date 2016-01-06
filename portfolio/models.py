import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    
"""
from django.db import models

class Project_name(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
    class Meta:
        db_table = "name"
        ordering = ['name']
    class Admin:
        pass
        
    def __repr__(self):
        return self.name
    
class Medium(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        db_table = "media"
        verbose_name_plural = "media"
        ordering = ['name']

    class Admin:
        pass
    
    def __repr__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=250)
    project_url = models.URLField('Project URL')
    description = models.TextField(blank=True)
    
    media = models.ManyToManyField(Medium)
    disciplines = models.CharField(max_length=200)
    completion_date = models.DateField()
    in_development = models.BooleanField()
    is_public = models.BooleanField(default=True)
    overview_image = models.URLField()
    detail_image = models.URLField()
    
    class Meta:
        db_table = "projects"
        ordering = ['-completion_date']
     
    class Admin:
        pass
        
    def __repr__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/work/%s/" % self.slug
"""