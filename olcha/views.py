from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category,Group
from .serializers import CategoryModelSerializer,GroupSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

#For Category

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializers = CategoryModelSerializer(categories, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = CategoryModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get_object(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializers = CategoryModelSerializer(category)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        category = self.get_object(slug)
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        category = self.get_object(slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#For Group

class GroupListView(APIView):
    def get(self,request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    serializer_class = GroupSerializer
    def post(self,request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class GroupDetailView(APIView):
    def get_object(self, slug):
        try:
            return Group.objects.get(slug=slug)
        except Group.DoesNotExist:
            return None
        
    def get(self, request, slug):
        group = get_object_or_404(Group, slug=slug)
        serializers = GroupSerializer(group)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        group = self.get_object(slug)
        if group is None:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GroupSerializer(instance=group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, slug):
        group = self.get_object(slug=slug)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
 

