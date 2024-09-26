from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'