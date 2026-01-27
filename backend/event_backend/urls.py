"""event_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from events.views import (
    home,
    booking,
    contact,
    register_user,
    login_user,
    login_page,
    logout_user,
)

def backend_status(request):
    return JsonResponse({
        "status": "ok",
        "service": "EventSphere Backend",
        "message": "Backend is running successfully"
    })

urlpatterns = [
    path("admin/", admin.site.urls),

    # Pages
   path("", backend_status, name="backend_status"),
    path("booking/", booking, name="booking"),
    path("contact/", contact, name="contact"),
    path("login/", login_page, name="login"),
    path("logout/", logout_user, name="logout"),

    # APIs
    path("api/register/", register_user),
    path("api/login/", login_user),
    path("api/status/", backend_status),
   
]









