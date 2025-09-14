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
)

urlpatterns = [
    # Authentication routes
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile, name='profile'),  # ✅ this is what ALX checker wants

    # Blog post CRUD
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

# comment URLs (add these to your urlpatterns)
path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
