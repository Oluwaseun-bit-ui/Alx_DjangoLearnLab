from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # ✅ ALX required
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# --------------------
# Class-based API views
# --------------------

class AuthorListCreateView(APIView):
    """
    Handles listing all authors and creating new authors.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateView(APIView):
    """
    Handles listing all books and creating new books.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------
# Django generic views
# --------------------

class BookListView(ListView):
    """Displays a list of books."""
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    """Displays details for a single book."""
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(CreateView):
    """Form to create a new book."""
    model = Book
    fields = ["title", "author", "published_date", "isbn"]
    template_name = "books/book_form.html"
    success_url = "/books/"


class BookUpdateView(UpdateView):
    """Form to update an existing book."""
    model = Book
    fields = ["title", "author", "published_date", "isbn"]
    template_name = "books/book_form.html"
    success_url = "/books/"


class BookDeleteView(DeleteView):
    """Handles deleting a book."""
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = "/books/"
