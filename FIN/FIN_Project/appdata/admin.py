from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'gender', 'phone_No', 'address_Details', 'work_Experience', 'qualifications', 'projects', 'photo'] 

admin.site.register(Employee, EmployeeAdmin)