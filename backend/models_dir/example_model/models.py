from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import requests
# Create your models here.


# Extending User Model Using a One-To-One Link
class ExampleModel(models.Model):
    center_name = models.TextField(blank=True, null=True)
    center_html = models.TextField(blank=True, null=True)
