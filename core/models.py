from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
class Professor(models.Model):
    Name = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100,defaul)
    def __str__(self):
        return self.Name
        
class Course(models.Model):
    Name = models.CharField(max_length=200) 
    Course_id = models.CharField(max_length=200,default="MTLXXX")
    def __str__(self):
        return self.Course_id

class PReview(models.Model):
    question=models.ForeignKey(Professor,on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    is_ano = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pub_date = models.DateTimeField(auto_now="True" 'date published')

class CReview(models.Model):
    question=models.ForeignKey(Course,on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200)
    is_ano = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pub_date = models.DateTimeField(auto_now="True" 'date published')  

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=300)