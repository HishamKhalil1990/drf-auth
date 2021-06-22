from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    grade = models.CharField(max_length=256)
    feedback = models.TextField(default='',null=True)
    teacher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name