from django.http import JsonResponse
from .model import Employee
from .serializers import EmployeeSerializers


def handler200(request, *args, **kwargs):
    data = {"message": "Employee Created Successfully.",
            "success": True, "status": 200}
    return JsonResponse(data = data)

def handler200(request, *args, **kwargs):
    emp = Employee.objects.get
    data = {"message": "employee already exist.",
            "success": False, "status": 200}
    return JsonResponse(data = data)

def handler200(request, *args, **kwargs):
    data = {"message": "employee already exist.",
        "success": False, "status": 200}
    return JsonResponse(data = data)