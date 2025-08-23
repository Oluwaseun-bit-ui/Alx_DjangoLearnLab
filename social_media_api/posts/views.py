from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """
    list: List posts (paginated). Supports search by title/content and ordering by created_at/updated_at.
    create: Create a post (authenticated). Author is set to request.user.
    retrieve/update/partial_update/destroy: Standard CRUD with owner-only write.
    """
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Filtering & search
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Example: /api/posts/?author=<user_id>
    filterset_fields = ['author']
    # Example: /api/posts/?search=django (searches title & content)
    search_fields = ['title', 'content']
    # Example: /api/posts/?ordering=created_at  or  -created_at
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    list: List comments. Optionally filter by ?post=<post_id>.
    create: Create a comment linked to a post. Author is set to request.user.
    """
    queryset = Comment.objects.select_related('author', 'post').all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Example: /api/comments/?post=<post_id>
    filterset_fields = ['post']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        post = serializer.validated_data.get('post')
        if not post:
            # enforce that a post must be supplied when creating a comment
            raise ValidationError({"post": "This field is required."})
        serializer.save(author=self.request.user)

