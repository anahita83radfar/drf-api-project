from rest_framework import generics, permissions
from drf_api_project.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# The code taken from the Code Institute drf-api project
class CommentList(generics.ListCreateAPIView):
    """
    List of all comments and create a comment if logged in.
    By defining the 'perform_create' method make sure comments
    are associated with a user upon creation.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete a comment by id if you own it.
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    