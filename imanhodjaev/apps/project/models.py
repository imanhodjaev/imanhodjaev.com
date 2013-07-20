from django.db import models

from apps.my_auth.models import User


class AbstractDatetime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(AbstractDatetime):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(max_length=255)


class Post(AbstractDatetime):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(max_length=255)
    project = models.ForeignKey(Project, null=True, blank=True)
    author = models.ForeignKey(User)

    images = models.ForeignKey(PostImage, null=True, blank=True)
    files = models.ForeignKey(PostFile, null=True, blank=True)


class PostImage(AbstractDatetime):
    title = models.CharField(max_length=255, default='Image')
    image = models.ImageField(upload_to='uploads/')


class PostFile(AbstractDatetime):
    title = models.CharField(max_length=255, default='File')
    post_file = models.FileField(upload_to='uploads/')
