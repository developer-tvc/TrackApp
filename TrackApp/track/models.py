from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

class Unit(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

class Visit(models.Model):
    visit_date = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
