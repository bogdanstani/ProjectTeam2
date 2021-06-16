from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    #id = models.AutoField()

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)  # Audi
    type = models.CharField(max_length=200)   # A6
    year = models.DateField()
    km = models.IntegerField()
    registry_number = models.CharField(max_length=9)
    #id = models.AutoField()

class Documents(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=200)
    doc_issue_date = models.DateField()
    doc_expiry_date = models.DateField()
    #id = models.AutoField()
