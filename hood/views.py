from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Neighbourhood,Profile,Department, Business
from .serializers import UserSerializer, HoodSerializer, PostSerializer, ProfileSerializer,BusinessSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class UserList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self, request,format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HoodList(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def post(self, request, format=None):
        serializers = HoodSerializer(data=request.data)
        if serializers.is_valid():
            
           serializers.save(admin=request.user)
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            
class AllHoodsList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_hoods = Neighbourhood.objects.all()
        serializers = HoodSerializer(all_hoods,many=True)
        return Response(serializers.data)
    
class SingleHoodList(APIView):
    permission_classes = (IsAuthenticated,)
    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404
    def get(self,request,pk,format=None):
        hood = self.get_hood(pk)
        serializers = HoodSerializer(hood)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user, neighbourhood=hood)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    
class CreatePostView(APIView):
    permission_classes  = (IsAuthenticated,)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            
            serializers.save(user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateBusinessView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404
    def get(self,request,pk, format=None):
        businesses = Business.objects.filter(neighbourhood_id=pk)
        serializers = BusinessSerializer(businesses, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
       
    def post(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user,neighbourhood=hood)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class CreateDepartmentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_hood(self, pk):
        try:
            return Neighbourhood.objects.get(pk=pk)
        except Neighbourhood.DoesNotExist:
            return Http404
    def get(self,request,pk, format=None):
        department = Department.objects.filter(neighbourhood_id=pk)
        serializers = DepartmentSerializer(department, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,pk,format=None):
        hood = self.get_hood(pk)
        serializers = DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(neighbourhood=hood)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404
    def get_hood(self, id):
        try:
            return Neighbourhood.objects.get(id=id)
        except Neighbourhood.DoesNotExist:
            return Http404
    def put(self, request,pk,id,format=None):
        profile = self.get_profile(pk)
        hood = self.get_hood(id)
        serializers = ProfileSerializer(profile,data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user, neighbourhood=hood)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
            
    
    