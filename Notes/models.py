from django.db import models

# Create your models here.

class Project_Users(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    project_name=models.CharField(max_length=25)
    raas_version=models.IntegerField()


class User_Selection(models.Model):
    type_of_hc=models.CharField(max_length=25)
    type_of_activity=models.CharField(max_length=25)
    fetch_fresh_logs=models.IntegerField()
    name_of_project=models.CharField(max_length=25)

