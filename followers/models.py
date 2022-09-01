from django.db import models
from django.contrib.auth.models import User


# The code taken from the Code Institute drf-api project
class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'
    who both are User model instances.
    'owner' is a User that is following a User.
    'followed' is a User that is followed by 'owner'.
    By adding 'related_name' attribute django can differentiate
    between 'owner' and 'followed'.
    By adding 'unique_together' user can't double follow the same user.
    """
    owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
