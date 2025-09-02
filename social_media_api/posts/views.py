from rest_framework import viewsets, generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Custom permission so only owners can edit/delete their own stuff
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Everyone can view (safe methods)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only owner can edit/delete
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FollowingPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get the users the logged-in user is following
        following_users = self.request.user.following.all()
        # get posts from those users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    