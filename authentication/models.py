from django.db import models
from django.utils import timezone

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=20)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class City(models.Model):
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50)
    password = models.TextField()
    id_city = models.ForeignKey(City, on_delete=models.CASCADE) #error
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


