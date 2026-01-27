from django.shortcuts import render,  redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from .models import Booking
from .models import ContactMessage

def home(request):
    return render(request, "index.html")


def register_user(request):
    if request.method == "POST":
        data = request.POST
        User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "invalid"}, status=400)


def login_user(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            return JsonResponse({"status": "success"})
        return JsonResponse({"status": "failed"}, status=401)

def booking(request):
    event = request.GET.get("event", "Selected Event")
    success = False

    if request.method == "POST":
        Booking.objects.create(
            event=request.POST.get("event"),
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            date=request.POST.get("date"),
            message=request.POST.get("message"),
        )
        success = True

    return render(request, "booking.html", {
        "event": event,
        "success": success
    })


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )
        return render(request, "contact.html", {
            "success": True
        })

    return render(request, "contact.html")

def login_page(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("/login/")

