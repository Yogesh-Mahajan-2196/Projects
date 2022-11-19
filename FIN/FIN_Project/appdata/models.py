from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone_No = models.CharField(max_length=20)
    address_Details = models.JSONField(null = True)
    work_Experience = models.JSONField(null = True)
    qualifications = models.JSONField(null = True)
    projects = models.JSONField(null = True)
    photo = models.ImageField(upload_to = "images", null = True, blank = True)

    def __str__(self):
        return self.name