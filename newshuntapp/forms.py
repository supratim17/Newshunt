from django import forms

from newshuntapp.models import *

from django.db import models
from django.forms import ModelForm

class UserForm(ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model=User
		#fields = '__all__'
		fields=['first_name','last_name','password','email']

class ArticleForm(ModelForm):
	"""docstring for ArticleForm"ModelForm"""
	class Meta:
		model=Article
		fields = ['title','date','content','image_path','category_name']
		
		