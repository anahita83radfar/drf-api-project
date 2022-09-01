from rest_framework import generics, permissions
from drf_api_project.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


# The code taken from the Code Institute drf-api project
class LikeList(generics.ListCreateAPIView):
    """
    List of all likes and create a like if logged in.
    By defining the 'perform_create' method make sure likes
    are associated with a user upon creation.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a like if you own it.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()