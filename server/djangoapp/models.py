from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [(SEDAN, 'Sedan'), (SUV, 'SUV'), (WAGON, 'Wagon')]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default=SUV)
    year = models.IntegerField(default=2023, validators=[MaxValueValidator(2023), MinValueValidator(2015)])
    dealer_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
