from django.shortcuts import render
from rest_framework import viewsets
from .models import StreamingPlatform, WatchList
from .serializers import StreamingPlatformSerializer, WatchListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StreamingPlatformAV(APIView):
    def get(self, request):
        movie=StreamingPlatform.objects.all()
        serializer=StreamingPlatformSerializer(movie, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamingPlatformListAV(APIView):
    def get(self,request,pk):
        try:
           movie=StreamingPlatform.objects.get(pk=pk)
        except movie.DoesNotExist():
           return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=StreamingPlatformSerializer(movie)
        return Response(serializer.data)
        
        
    def put(self,request,pk):
        movie=StreamingPlatform.objects.get(pk=pk)
        serializer=StreamingPlatformListAV(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=StreamingPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########################3


class MovieListAV(APIView):
    def get(self, request):
        movie=WatchList.objects.all()
        serializer=WatchListSerializer(movie, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MovieListDetailAV(APIView):
    def get(self,request,pk):
        try:
           movie=WatchList.objects.get(pk=pk)
        except movie.DoesNotExist():
           return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
        
        
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
