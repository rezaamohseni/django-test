from django.db import models
from django.contrib.auth.models import User
class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Team(models.Model):
    image = models.ImageField(upload_to='services' , default='default.jpg')
    skill = models.ManyToManyField(Skill)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title