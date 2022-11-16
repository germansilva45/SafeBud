# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
	nombre=models.CharField(max_length=30)
	correo=models.CharField(max_length=30)
	mensaje=models.CharField(max_length=1000)
	def __str__(self):
		return self.nombre