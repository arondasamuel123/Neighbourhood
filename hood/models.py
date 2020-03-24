from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    SUPER_ADMIN = 'SUPER ADMIN'
    ADMIN = 'ADMIN'
    USER = 'USER'
    ROLE_TYPE_CHOICES = [
        (SUPER_ADMIN, 'SUPER ADMIN'),
        (ADMIN, 'ADMIN'),
        (USER, 'USER')
    ]
    name = models.CharField(max_length=20)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    role_type = models.CharField(max_length=2, choices=ROLE_TYPE_CHOICES, default=USER)
    
    
    
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=20)
    neighbourhood_location = models.CharField(max_length=20)
    occupants = models.IntegerField()
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    