from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_api_project.permissions import IsOwnerOrReadOnly


# The code taken from the Code Institute drf-api project
class ProfileList(generics.ListAPIView):
    """
    List of all profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
