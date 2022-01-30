"""
Definition of models.
"""

from django.db import models

# Create your models here.

#Each model is a Python class
#   suclass django.db.models.Model
#Each attribute of the model represents a data field


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

#https://docs.djangoproject.com/en/4.0/topics/db/models/

