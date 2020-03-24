from django.test import TestCase
from .models import User, Neighbourhood


class UserTestCase(TestCase):
    
    def setUp(self):
        self.super_admin = User(username="arondasamuel123",email="arondasamuel123@gmail.com",name="Samuel Aronda", role_type="SUPER ADMIN",is_superuser=True, is_staff=True, is_active=True)
        self.admin_user = User(username="jack123",email="jack@gmail.com",name="Jack Doe", role_type="ADMIN",is_superuser=False, is_staff=True, is_active=True)
        self.user_one = User(username="john123", email="john@gmail.com", name="John Doe", role_type="USER",is_superuser=False, is_staff=False, is_active=True)
        
    
    
    def test_save_superadmin(self):
        self.super_admin.save_sadmin()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        
    def test_save_admin(self):
        self.admin_user.save_admin()
        users = User.objects.all()
        self.assertTrue(len(users)> 0)
    def test_save_user(self):
        self.user_one.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
        
class NeighbourhoodTestCase(TestCase):
    
    def setUp(self):
        self.admin_user = User(username="jack123",email="jack@gmail.com",name="Jack Doe", role_type="ADMIN",is_superuser=False, is_staff=True, is_active=True)
        self.hood_one = Neighbourhood(neighbourhood_name="Langata Estate", neighbourhood_location="Langata", occupants="100",admin_id=self.admin_user)
        
    
    def test_save_neighbourhood(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods)> 0)   
        
    