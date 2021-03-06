from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


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
    role_type = models.CharField(max_length=20, choices=ROLE_TYPE_CHOICES, default=USER)
    
    def save_sadmin(self):
        self.save()
    def save_admin(self):
        self.save()
    def save_user(self):
        self.save()
        
    
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=20)
    neighbourhood_location = models.CharField(max_length=20)
    occupants = models.IntegerField()
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def save_hood(self):
        self.save()
    def delete_hood(self):
        self.delete()
    @classmethod
    def get_hood_id(cls, id):
        hood = Neighbourhood.objects.get(pk=id)
        return hood
    def update_occupants(self, occupants):
        self.occupants = occupants
        self.save()
class Profile(models.Model):
    bio = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    general_location = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_prof_id(cls, id):
        profile = cls.objects.get(pk=id)
        return profile
    def update_bio(self, bio):
        self.bio = bio
        self.save()
        
        
        
class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        self.save()
    
class Business(models.Model):
    business_name = models.CharField(max_length=20)
    business_email = models.CharField(max_length=20)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()
        

class Department(models.Model):
    HEALTH = 'health'
    AUTHORITIES = 'authorities'
    DEPT_TYPE_CHOICES = [
        (HEALTH, 'health'),
        (AUTHORITIES, 'authorities'),
    ]
    contact_number = models.IntegerField()
    dept_name = models.CharField(max_length=20, default="NULL")
    neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    dept_type = models.CharField(max_length=20, choices=DEPT_TYPE_CHOICES, default=HEALTH)
    
    def save_dept(self):
        self.save()
        
    




     
    
    