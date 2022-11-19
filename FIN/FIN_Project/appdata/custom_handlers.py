from django.http import JsonResponse

def handler200(request, *args, **kwargs):
    data = {"message": "employee already exist.",
            "success": False}