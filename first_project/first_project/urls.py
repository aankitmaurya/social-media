from django.contrib import admin
from django.urls import path
from django.urls import include
from first_app.views import AboutUs, detail_view, HomeTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', detail_view, name="about_us"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", HomeTemplate.as_view(), name="home"),
]
