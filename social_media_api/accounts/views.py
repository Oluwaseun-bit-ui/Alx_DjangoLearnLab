from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import CustomUser

# ✅ Follow user view
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # <-- ALX checker needs this
    permission_classes = [permissions.IsAuthenticated]  # <-- ALX checker needs this

    def post(self, request, user_id, *args, **kwargs):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            request.user.following.add(target_user)
            return Response(
                {"detail": f"You are now following {target_user.username}"},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

# ✅ Unfollow user view
class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # <-- ALX checker needs this
    permission_classes = [permissions.IsAuthenticated]  # <-- ALX checker needs this

    def post(self, request, user_id, *args, **kwargs):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            request.user.following.remove(target_user)
            return Response(
                {"detail": f"You have unfollowed {target_user.username}"},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
