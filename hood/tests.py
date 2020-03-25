from django.test import TestCase
from .models import User, Neighbourhood, Profile


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
        
    def test_delete_neighbourhood(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.delete_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) == 0)
        
    def test_get_hoof_id(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.get_hood_id(self.hood_one.id)
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)
        
    def test_update_hood_occupants(self):
        self.admin_user.save_admin()
        self.hood_one.save_hood()
        self.hood_one.get_hood_id(self.hood_one.id)
        self.hood_one.update_occupants("200")
        self.assertTrue(self.hood_one.occupants=="200")
        
class ProfileTestCase(TestCase):
    
    def setUp(self):
         self.admin_user = User(username="jack123",email="jack@gmail.com",name="Jack Doe", role_type="ADMIN",is_superuser=False, is_staff=True, is_active=True)
         self.user_one = User(username="john123", email="john@gmail.com", name="John Doe", role_type="USER",is_superuser=False, is_staff=False, is_active=True)
         self.hood_two = Neighbourhood(neighbourhood_name="Langata Estate", neighbourhood_location="Langata", occupants="100",admin_id=self.admin_user)
         self.profile_one = Profile(bio="I love my neighbourhoood", neighbourhood=self.hood_two, general_location="Langata", user=self.user_one)
         
         
    def test_save_profile(self):
        self.admin_user.save_admin()
        self.user_one.save_user()
        self.hood_two.save_hood()
        self.profile_one.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_profile(self):
        self.admin_user.save_admin()
        self.user_one.save_user()
        self.hood_two.save_hood()
        self.profile_one.save_profile()
        self.profile_one.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)
        
    def test_get_prof_id(self):
        self.admin_user.save_admin()
        self.user_one.save_user()
        self.hood_two.save_hood()
        self.profile_one.save_profile()
        self.profile_one.get_prof_id(self.profile_one.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    def test_update_bio(self):
        self.admin_user.save_admin()
        self.user_one.save_user()
        self.hood_two.save_hood()
        self.profile_one.save_profile()
        self.profile_one.update_bio("This is a new bio")
        self.assertTrue(self.profile_one.bio=="This is a new bio")
        
        
           
        
    