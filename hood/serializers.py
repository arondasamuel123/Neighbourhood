from rest_framework import serializers
from .models import User,Neighbourhood,Post,Profile,Business, Department
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username','email','name', 'password', 'role_type', 'is_superuser', 'is_staff')
        
    def validate_password(self, value: str) -> str:
        return make_password(value)
    
class HoodSerializer(serializers.ModelSerializer):
    
    admin = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name', 'neighbourhood_location', 'occupants', 'admin')
        
class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    class Meta:
        model = Post
        fields = ('post','user','post_created')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    
    neighbourhood = serializers.PrimaryKeyRelatedField(
        queryset=Neighbourhood.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    class Meta:
        model = Profile
        fields = ('bio','general_location', 'user', 'neighbourhood')
        
class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    neighbourhood = serializers.PrimaryKeyRelatedField(
        queryset=Neighbourhood.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    
    class Meta:
        model = Business
        fields = ('business_name', 'business_email', 'user', 'neighbourhood')
        
class DepartmentSerializer(serializers.ModelSerializer):
    neighbourhood = serializers.PrimaryKeyRelatedField(
        queryset=Neighbourhood.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    class Meta:
        model = Department
        fields = ('contact_number', 'dept_name', 'dept_type', 'neighbourhood')
        
    



        