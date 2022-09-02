from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import user

class UserForm(forms.ModelForm):
    class Meta: 
        model = user
        field ='__all__'
        #field=['Full_name',' User_namme','Email','Phone','Password','Confrim_password',]
