from django.contrib import admin
from django.urls import path, include  # You need include to connect app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This connects to your api/urls.py
]
