from django.db import models

class Employee(models.Model):
    eid = models.AutoField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone_No = models.CharField(max_length=20)
    address_Details = models.JSONField(default = {"hno": "null", "street": "null", "city": "null", "state": "null"})
    work_Experience = models.JSONField(default = {"comapny_Name": "null", "fromData": "null", "to_Data": "null", "address": "null"})
    qualifications = models.JSONField(default = {"qualification_Name": "null", "percentage": "null", "projects": "null"})
    projects = models.JSONField(default = {"title": "null", "description": "null"})
    photo = models.ImageField(upload_to = "images", null = True, blank = True)

    def __str__(self):
        return self.name