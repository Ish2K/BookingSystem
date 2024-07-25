from django.db import models

# Create your models here.

class Menu(models.Model):
    # id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # inventory = models.IntegerField()

    #code
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):

    # ID = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100)
    # number_of_guests = models.IntegerField()
    # bookingDate = models.DateField()

    #code

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()
    bookingDate = models.DateField()

    def __str__(self):

        return self.name