from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    login_view,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    edit_comment,
    delete_comment,
)

urlpatterns = [
    # Authentication routes
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile, name='profile'),

    # Post routes
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment routes (ALX-compliant)
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:pk>/update/', edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/comments/<int:pk>/delete/', delete_comment, name='delete_comment'),
]

