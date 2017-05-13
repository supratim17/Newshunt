from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

import datetime

# from django.forms import ModelForm

# Create your models here.

class Category(models.Model):
	"""docstring for Category"""
	category_name=models.CharField(max_length=20)


class Role(models.Model):
	"""docstring for Role"""
	role_name=models.CharField(max_length=10)

class User(models.Model):
	"""docstring for User"""
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	role=models.CharField(max_length=10, default='Reader')

class Article(models.Model):
	"""docstring for Article"""
	title=models.CharField(max_length=200)
	date=models.DateField(default= timezone.now)
	content=models.CharField(max_length=4000)
	image_path=models.CharField(max_length=100)
	category_name=models.ForeignKey(Category, on_delete=models.CASCADE)
	# category_name=models.CharField(max_length=10)
	likes=models.IntegerField(null= True)
	dislikes=models.IntegerField(null= True)