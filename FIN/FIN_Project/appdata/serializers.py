from rest_framework import serializers
from .models import Employee
from drf_extra_fields.fields import Base64ImageField


class EmployeeSerializers(serializers.ModelSerializer):
    photo = Base64ImageField(required = False)
    
    class Meta:
        model = Employee
        fields = ['id','name', 'email', 'age', 'gender', 'phone_No', 'address_Details', 'work_Experience', 'qualifications', 'projects', 'photo']
