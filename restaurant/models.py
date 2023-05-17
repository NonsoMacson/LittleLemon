from django.db import models

# Create your models here.

class Menu(models.Model):
    title= models.CharField(max_length=255)
    price=models.DecimalField(max_digits=2, decimal_places=1)
    inventory=models.IntegerField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name =models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingDate=models.DateField(auto_now=True)

    def __str__(self):
        return self.name