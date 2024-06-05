from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    image = models.ImageField(upload_to='team' , default= 'default.jpg') 
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username
    
class Service(models.Model):
    image = models.ImageField(upload_to='service' , default= 'default.jpg') 
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    price = models.IntegerField()
    counted_view = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username
    