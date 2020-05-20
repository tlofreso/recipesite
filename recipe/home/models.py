from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class RecipeRequests(models.Model):
    recipe_site_tld = models.CharField(max_length=150)
    recipe_title = models.CharField(max_length=80)
    recipe_parsed = models.BooleanField()
