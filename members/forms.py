from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):

        class Meta:
          model=User
          fields = ('username','first_name', 'last_name', 'email', 'password1','password2',)
          labels = {
              'username': 'UserName',
              'first_name': 'First-Name',
              'last_name': 'Last-Name',
              'email': 'Email',
              'password1': '',
              'password2': '', }
          widgets = {
              'first_name': forms.TextInput(attrs={'class': 'form-control'}),
              'last_name': forms.TextInput(attrs={'class': 'form-control'}),
              'email': forms.EmailInput(attrs={'class': 'form-control'}), }
        def __init__(self,*args,**kwargs):
           super(RegisterUserForm,self).__init__(*args, **kwargs)
           self.fields['username'].widget.attrs['class'] = 'form-control'
           self.fields['password1'].widget.attrs['class'] = 'form-control'
           self.fields['password2'].widget.attrs['class'] = 'form-control'