from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )  # Link to User model
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This makes sure the posts are ordered by the newest one first.
        ordering = ["-created_at"]

    def __str__(self):
        # This is what you see in the Admin panel (a readable name)
        return self.title
