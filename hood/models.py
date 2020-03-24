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
    

class Profile(models.Model):
    bio = models.TextField()
    neighbourhood_name = models.CharField(max_length=20)
    general_location = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=20)
    neighbourhood_location = models.CharField(max_length=20)
    occupants = models.IntegerField()
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    