from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework import viewsets

class EmployeeDetails(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    