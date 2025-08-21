from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', register, name='register'),

    # Blog post CRUD
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
