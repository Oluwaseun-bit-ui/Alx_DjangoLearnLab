from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),   # include only once here
]

urlpatterns = [
    # ... your other urls
    path('profile/', views.profile, name='profile'),
]
