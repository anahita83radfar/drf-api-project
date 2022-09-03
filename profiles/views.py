from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from drf_api_project.permissions import IsOwnerOrReadOnly


# The code taken from the Code Institute drf-api project
class ProfileList(generics.ListAPIView):
    """
    List of all profiles.
    By using the 'annotate' method on Profile can you add some specific fields to the 
    queryset such as 'Count' method to calculate how many model instances of each there are.
    By linking these fields to their relevant model fields, and limited instances being returned
    using distinct = True. To make these fields sortable, needs to create filters. 
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # All profiles that are following a profile
        'owner__following__followed__profile',
        # All profiles that are followed by a profile
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'owner__username',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
