from rest_framework import generics, permissions
from drf_api_project.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# The code taken from the Code Institute drf-api project
class FollowerList(generics.ListCreateAPIView):
    """
    List of all followers and follow a user if logged in.
    By defining the 'perform_create' method make sure followers
    are associated with a user.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a follower.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    