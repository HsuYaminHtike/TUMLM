from django.db import models

# Create your models here.
class IT(models.Model):
	dept = models.CharField(max_length=255)
	people = models.CharField(max_length=255)

	def __str__(self):
		return self.dept