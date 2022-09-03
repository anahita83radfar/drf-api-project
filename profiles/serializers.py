from rest_framework import serializers
from .models import Profile
from followers.models import Follower


# The code taken from the Code Institute drf-api project
class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    'get_is_owner' method here check if the currently logged in user is the owner of the profile.
    By adding 'get_following_id' method If I am logged in and follow a profile, I can see the id 
    of the newly created Follower instance in profile’s following_id field on the Profile list. 
    This means that I am following that person’s profile and if I decide to unfollow  them, 
    I know which Follower instance to delete.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None
    
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'email', 'content', 'image', 'is_owner', 'following_id'
        ]
        