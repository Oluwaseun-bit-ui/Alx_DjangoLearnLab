from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books
class ListView(generics.ListAPIView):
    """
    ListView
    - GET /api/books/ => list all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve a single book by ID
class DetailView(generics.RetrieveAPIView):
    """
    DetailView
    - GET /api/books/<id>/ => retrieve one book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book
class CreateView(generics.CreateAPIView):
    """
    CreateView
    - POST /api/books/create/ => create a new book
    - Requires authentication
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update an existing book
class UpdateView(generics.UpdateAPIView):
    """
    UpdateView
    - PUT/PATCH /api/books/<id>/update/ => update book
    - Requires authentication
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book
class DeleteView(generics.DestroyAPIView):
    """
    DeleteView
    - DELETE /api/books/<id>/delete/ => delete book
    - Requires authentication
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
