from django.db import models

# Create your models here.

class ExampleDotCom(models.Model):
	"""docstring for ExampleDotCom"""
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.title
		