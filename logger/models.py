from django.db import models

# Create your models here.
class plane(models.Model):
    registration = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    onair = models.BooleanField(default=True)
    takeofftime = models.TimeField()
    beforenext_takeoff = models.IntegerField()
    created = models.DateField(auto_now_add=True)
