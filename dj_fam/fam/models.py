from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Human(models.Model):
    # id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])  # years
    height = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)])  # cm
    weight = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])  # kg
    occupation = models.CharField(max_length=50)
