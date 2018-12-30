from django import forms
from drsch.models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    
    class Meta:
      model = User
      fields = ("username", "first_name", "last_name", "email", "password1", "password2")

      def save(self, commit=True):
          user = super(UserCreateForm, self).save(commit=False)
          user.first_name = self.cleaned_data["first_name"]
          user.last_name = self.cleaned_data["last_name"]
          user.email = self.cleaned_data["email"] 
          if commit:
            user.save()
          return user
    

class AddUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'is_teacher', 'is_admin']


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.HiddenInput(),
        }
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_teacher', 'is_admin']

    def __init__(self, *args, **kwargs):
        super(EditUser, self).__init__(*args, **kwargs)



class Contact(forms.Form):
    sender = forms.CharField(label='Name', max_length=30)
    subject = forms.CharField(label='Subject', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)
    message = forms.CharField(widget=forms.Textarea())

