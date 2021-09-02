from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    s = (
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Completed','Completed'),
    )
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(max_length=1500,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True,null=True,blank=True)
    status = models.CharField(max_length=25,null=True,blank=True,choices=s,default='Pending')

    def __str__(self):
        return self.title
