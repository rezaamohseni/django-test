from django.db import models
from django.contrib.auth.models import User
class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class Team(models.Model):
    image = models.ImageField(upload_to='services' , default='default.jpg')
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    description = models.TextField()
    skill = models.ManyToManyField(Skill)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Option(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Service(models.Model):
    image = models.ImageField(upload_to='services' , default='default.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    Category = models.ManyToManyField(Category)
    generals = models.ManyToManyField(Option)
    status = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    counted_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    
    
    
    