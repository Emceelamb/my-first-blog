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
'''
    
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
'''    
class Project(models.Model):
    projecttitle = models.CharField(max_length=200, null=True)
    projectdate = models.CharField(max_length=200, null=True)
    projectmedium = models.CharField(max_length=200, null=True)
    projecttext = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)

    
    projectimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='https://pmcdeadline2.files.wordpress.com/2010/08/nicolas_cage.jpg')
    '''
    def publish(self):
        
        self.save()

    def __str__(self):
        return self.projecttitle
'''
    
    def __str__(self):
        return self.projecttitle
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    
    