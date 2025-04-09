from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    publication_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title





