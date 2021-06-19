from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)  # Audi
    type = models.CharField(max_length=200)   # A6
    year = models.DateField()
    km = models.IntegerField()
    registry_number = models.CharField(max_length=9)


class Documents(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField()
