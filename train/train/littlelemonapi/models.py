from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=6,max_digits=10)
    inventory=models.SmallIntegerField()