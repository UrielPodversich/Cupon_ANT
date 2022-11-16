from django.db import models

# Create your models here.

class Cupon(models.Model):
    name = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=50, unique=True)
    valid = models.DateTimeField()
    expired = models.DateTimeField()
    DISCOUNT = [
        ('10', '10%'),
        ('15', '15%'),
        ('25', '25%'),
        ('30', '30%'),
        ('50', '50%'),
    ]
    discount = models.CharField(max_length=3, choices=DISCOUNT)
    available = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.name}'