from rest_framework.test import APITestCase
from rest_framework import status


class TestPostList(APITestCase):

    def test_list_post(self):
        posts_list = {'title': "Test", 'content': "Test"}
        response = self.client.get('/posts/', posts_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
