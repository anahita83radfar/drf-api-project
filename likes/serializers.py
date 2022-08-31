from rest_framework import serializers
from .models import Like
from django.db import IntegrityError


# The code taken from the Code Institute drf-api project
class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    We don't need a 'get_is_owner' method here because we don't 
    need to know if the currently logged in user is the owner of a like.
    The 'create' method handles duplicates, the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    
    
    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post', 'created_at'
        ]
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })