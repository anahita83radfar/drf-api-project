from rest_framework import serializers
from .models import Like


# The code taken from the Code Institute drf-api project
class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    We don't need a 'get_is_owner' method here because 
    we don't need to know if the currently 
    logged in user is the owner of a like.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    
    
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'post', 'created_at'
        ]