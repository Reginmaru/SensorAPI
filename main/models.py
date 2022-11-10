from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    unit = models.CharField(max_length = 20)

class Record(models.Model):
    date = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()

