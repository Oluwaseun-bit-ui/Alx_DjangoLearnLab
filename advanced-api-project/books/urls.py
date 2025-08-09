from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView  # <-- import both

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list'),
    path('<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
