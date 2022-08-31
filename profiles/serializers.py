from rest_framework import serializers
from .models import Profile


# The code taken from the Code Institute drf-api project
class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    'get_is_owner' method here check if the currently logged in user is the owner of the profile.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'email', 'content', 'image', 'is_owner'
        ]
        