from django import forms

from newshuntapp.models import *

from django.db import models
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model=User
		fields=['first_name','last_name','password','email']
		widgets = {
        'password': forms.PasswordInput(),
        'email': forms.EmailInput(),
    }

CHOICES = (('1', 'First',), ('2', 'Second',))

class ArticleForm(forms.ModelForm):
	"""docstring for ArticleForm"ModelForm"""
	class Meta:
		model=Article
		fields = ['title','date','content','image_path','category_name']
		category_name=forms.ModelChoiceField(queryset=Category.objects.values('category_name'))
		# category_name=forms.ChoiceField(widget=forms.RadioSelect, choices= CHOICES)
		widgets = {
			'date': forms.DateInput(),
		}