from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


# The code taken from the Code Institute drf-api project
class CurrentUserSerializer(UserDetailsSerializer):
    """
    By adding the 'profile_id' and 'profile_image' to fields,
    we’ll know which profile to link to and what image to
    show in the navigation bar for a logged in user.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
