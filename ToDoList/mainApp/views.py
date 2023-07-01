from django.shortcuts import render
from .models import *
from .serilaized import *
from rest_framework import generics




# CRUD Opreitons

class ListToDO(generics.ListAPIView):   # Read
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers

class DetailToDO(generics.RetrieveUpdateAPIView):  # Update
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers

class CreateToDO(generics.CreateAPIView):  # Create
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers

class DeleteToDO(generics.DestroyAPIView):   # Delete
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers