from django.db import models

# Create your models here.

class repo(models.Model):
	name=models.CharField(max_length=20)
	lang=models.CharField(max_length=20,blank=True,null=True)
