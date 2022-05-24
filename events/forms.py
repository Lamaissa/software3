from django import forms
from django.forms import ModelForm
from .models import Manager
from .models import Task

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ('first_name', 'last_name', 'email', 'phone', 'address')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'address': '', }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Address'}), }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due', 'priority', 'manager', 'member_team', 'status','descript')
        labels = {
            'title': '',
            'due':'YYY-MM-DD HH:MM:SS',
            'priority': 'Proiority',
            'manager': 'Manager',
            'member_team': 'Member Team',
            'status': 'What is status?',
            'descript':'',
              }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Task..'}),
            'due': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Due..'}),
            'priority': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Task Priority'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': ' Manager For This Task'}),
            'member_team': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Member For This Task'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'descript': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your notice..'}),
            }


#class UpdateForm(ModelForm):
   # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task title..'}), label=False)
   # class Meta:
   #     model = Task
      #  fields = ('title', 'due', 'complete','priority')


