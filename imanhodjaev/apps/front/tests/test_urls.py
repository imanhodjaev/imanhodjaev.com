from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.my_auth.models import User
from apps.project.models import Post


class TestFront(TestCase):
    def setUp(self):
        self.user = User(username='test_user')
        self.user.set_password(1)
        self.user.save()

        self.post = Post(title='Test post')
        self.post.body = 'Content of the post'
        self.post.author = self.user
        self.post.save()

    def test_index(self):
        """ Test index page """
        res = self.client.get('front:index')

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Sultan Imanhodjaev')

    def test_post_detail(self):
        """ Test post details """
        res = self.client.get(reverse('front:post_detail', slug=self.post.slug))

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Sultan Imanhodjaev')
