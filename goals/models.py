from django.db import models
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User


class MyGoal(models.Model):
    goal_name = models.CharField(max_length=254)
    goal_description = models.TextField()
    goal_timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
  
    def __str__(self):
        return self.content

    
