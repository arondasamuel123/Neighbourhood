from rest_framework import serializers
from .models import User,Neighbourhood
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
    



        