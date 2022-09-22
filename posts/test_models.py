from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_superuser(
            username='admin',
            password='admin')
        self.post = Post.objects.create(
            title='Title',
            content='Post content',
            owner=user,
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(),
                         f'{self.post.id} {self.post.title}')
