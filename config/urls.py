from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Any URL starting with "blog/" will be sent to the blog/urls.py file
    path("blog/", include("blog.urls")),
    # Add this line. This includes all built-in auth URLs.
    path("accounts/", include("django.contrib.auth.urls")),
]
