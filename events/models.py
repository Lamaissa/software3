from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRIORITY = [
    ("H", "High"),
    ("M", "Medium"),
    ("L", "Low"),
]
status_choices = (
                ('Back Burner', 'Back Burner'),
                ('On Deck', 'On Deck'),
                ('In Process', 'In Process'),
                ('Complete', 'Complete'))

class Manager(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    def __str__(self):
       return self.first_name + ' ' + self.last_name

class Team(models.Model):
    first_name = models.CharField('First_Name', max_length=120)
    last_name = models.CharField('Last_Name', max_length=120,blank=True)
    email = models.EmailField('Email')
    evalutate = models.ForeignKey(Manager, null=True, on_delete=models.CASCADE)
    joined_us = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Task(models.Model):
    title = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=status_choices,default="")
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    member_team = models.ManyToManyField(Team, blank=False)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    descript= models.TextField(max_length=1500,default="")
    def __str__(self):
       return self.title