
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "DJ Event Management Backend Running"})