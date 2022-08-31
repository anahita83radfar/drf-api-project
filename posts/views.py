from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from drf_api_project.permissions import IsOwnerOrReadOnly


# The code taken from the Code Institute drf-api project
class PostList(generics.ListCreateAPIView):
    """
    List of all posts and create a post if logged in.
    By defining the 'perform_create' method make sure posts
    are associated with a user upon creation.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit and delete a post if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
