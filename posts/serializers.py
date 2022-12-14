from rest_framework import serializers
from .models import Post
from likes.models import Like


# The code taken from the Code Institute drf-api project
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    'get_is_owner' method here check if the currently
    logged in user is the owner of the post. 'validate_image'
    method will be validate the uploaded image every time we
    create or update a post. By adding 'get_like_id' method
    we’ll know if the current user has already liked a post.
    If they have, we’ll need a like_id field so that we know
    which one to delete if they wish to unlike it.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'excerpt', 'content', 'image', 'is_owner', 'profile_id',
            'profile_image', 'image_filter', 'like_id', 'comments_count',
            'likes_count'
        ]
