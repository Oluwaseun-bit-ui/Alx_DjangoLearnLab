from django.urls import path
from .views import BookListCreateView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
