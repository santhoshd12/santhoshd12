from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class newtable(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='a.png', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name
